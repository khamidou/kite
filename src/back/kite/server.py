#!/usr/bin/env python
import bottle
import json
import jsonfile
import sys
from jsonfile import JsonFile, serialize_json
from bottle import route, template, response, abort
from maildir import *

@route('/kite/<user>/mail')
def index(user):
            # FIXME: input sanitization - check permissions for user
            try:
                threads_index = JsonFile("/home/kite/Maildirs/%s/threads_index.json" % user)
            except IOError:
                response.status = 400
                return

            ret_threads = []
            for thread in threads_index.data[-50:]:
                ret_threads.append(thread)

            response.content_type = "application/json"
            return serialize_json(ret_threads)

@route('/kite/<user>/mail/<id>')
def index(user, id):
            # FIXME: input sanitization check perms
            threads_index = JsonFile("/home/kite/Maildirs/%s/threads_index.json" % user)
            thread = None

            for thr in threads_index.data:
                if thr["id"] == id:
                    thread = thr

            if thread == None:
                abort(404, "Thread not found.")

            thr["unread"] = False
            threads_index.save() # FIXME: race condition here

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
