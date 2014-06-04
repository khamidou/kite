#!/usr/bin/env python
import bottle
import json
import sys
import users
import datetime
from cabinet import DatetimeCabinet
from bottle import route, template, request, response, abort, get, post
from maildir import *
from utils import serialize_json

token_dict = {} # a dict to store auth tokens temporarily
                # it's not yet necessary to use memcached

def with_valid_token(fn):
    def check(**kwargs):

        cookie = request.get_cookie('XSRF-TOKEN')
        if cookie == None:
            abort(401, "Authentication error")

        header = request.get_header('X-XSRF-TOKEN', None)
        if header == None:
            abort(401, "Authentication error")

        header = header[1:-1] # seems like the header is between quotes
        if header != cookie:
            print "HEADER %s CO %s" % (header, cookie)
            # CSRF protection
            abort(401, "Authentication error")

        token_data = token_dict.get(cookie, None)
        if token_data == None:
            abort(401, "Authentication error")

        # if token is older than four hours, invalidate it
        if token_data["creation_date"] - datetime.datetime.now() > datetime.timedelta(0, 4 * 60 * 60):
            response.status = 401
            del token_dict[cookie]
            return

        return fn(**kwargs)

    return check

@post('/kite/auth')
def index():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username == None or password == None:
        abort(401, "Authentication error")
        return

    if users.auth_user(username, password):
        response.status = 200
        token = users.gen_token()
        token_dict[token] = {"creation_date": datetime.datetime.now(), "user": username}
        response.set_cookie('XSRF-TOKEN', token, path="/") # FIXME: set HTTPOnly when we enable SSL
        return

@get('/kite/<user>/mail')
@with_valid_token
def index(user):
            try:
                threads_index = DatetimeCabinet("/home/kite/threads.db")
            except IOError:
                abort(500, "Invalid thread")
                return

            ret_threads = []
            try:
                threads = threads_index[user]["threads_index"]
            except KeyError:
                threads = []
             
            for thread in threads:
                ret_threads.append(thread)

            response.content_type = "application/json"
            return serialize_json(ret_threads, protection=False)

@get('/kite/<user>/mail/<id>')
@with_valid_token
def index(user, id):
            try:
                threads_index = DatetimeCabinet("/home/kite/threads.db")
                thread = None
            except IOError:
                response.status = 400
                return

            # FIXME: use an index for threads entries ?
            for thr in threads_index[user]["threads_index"]:
                if thr["id"] == id:
                    thread = thr

            if thread == None:
                abort(404, "Thread not found.")

            thread["unread"] = False
            threads_index.sync()

            response.content_type = "application/json"

            ret_json = {"messages": [], 
                        "subject": thread["subject"],
                        "date": thread["date"], 
                        "id": thread["id"]
            }

            mdir = read_mail("/home/kite/Maildirs/%s" % user)
            for mail_id in thread["messages"]:
                ret_json["messages"].append(get_email(mdir, mail_id)) 

            return serialize_json(ret_json, protection=False)

bottle.run(host='localhost', port='8080', reloader=True)
