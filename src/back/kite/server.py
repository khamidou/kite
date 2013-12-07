#!/usr/bin/env python
import bottle
import json
from bottle import route, template, response
from maildir import *

@route('/kite/<user>/mail')
def index(user):
            response.content_type = "application/json"
            mdir = read_mail("/home/kite/Maildir")
            return json.dumps(get_emails(mdir))

@route('/kite/<user>/mail/<id>')
def index(user, id):
            response.content_type = "application/json"
            mdir = read_mail("/home/kite/Maildir")
            return json.dumps([get_email(mdir, id)])

bottle.run(host='localhost', port='8080', reloader=True)
