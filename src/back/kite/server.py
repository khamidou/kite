#!/usr/bin/env python
import bottle
import json
import sys
from cabinet import DatetimeCabinet
from bottle import route, template, response, abort
from maildir import *
from utils import serialize_json

@route('/kite/<user>/mail')
def index(user):
            # FIXME: input sanitization - check permissions for user
            try:
                threads_index = DatetimeCabinet("/home/kite/threads.db")
            except IOError:
                response.status = 400
                return

            ret_threads = []
            try:
                threads = threads_index[user]["threads_index"]
            except KeyError:
                threads = []
             
            for thread in threads:
                ret_threads.append(thread)

            response.content_type = "application/json"
            return serialize_json(ret_threads)

@route('/kite/<user>/mail/<id>')
def index(user, id):
            # FIXME: input sanitization check perms
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

            thr["unread"] = False
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

            return serialize_json(ret_json)

bottle.run(host='localhost', port='8080', reloader=True)
