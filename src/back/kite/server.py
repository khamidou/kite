#!/usr/bin/env python
import bottle
import json
import jsonfile
from jsonfile import JsonFile
from bottle import route, template, response, abort
from maildir import *

@route('/kite/<user>/mail')
def index(user):
            threads_index = JsonFile("/home/kite/Maildirs/kitebox.dev/testuser/threads_index.json")
            ret_threads = []
            for thread in threads_index.data[-50:]:
                ret_threads.append(thread)

            response.content_type = "application/json"
            return json.dumps(ret_threads, cls=jsonfile.DatetimeEncoder)

@route('/kite/<user>/mail/<id>')
def index(user, id):
            threads_index = JsonFile("/home/kite/Maildirs/kitebox.dev/testuser/threads_index.json")
            thread = None

            for thr in threads_index.data:
                if thr["id"] == id:
                    thread = thr

            if thread == None:
                abort(404, "Thread not found.")

            response.content_type = "application/json"

            ret_json = []
            mdir = read_mail("/home/kite/Maildir")
            for mail_id in thread["messages"]:
                print "BOOYA %s\n!!" % mail_id
                ret_json.append(get_email(mdir, mail_id)) 

            return json.dumps(ret_json)

bottle.run(host='localhost', port='8080', reloader=True)
