import bottle
import json
from bottle import route, template, response
from maildir import *

@route('/kite/<user>/mail')
def index(user):
            response.content_type = "application/json"
            mdir = read_mail("/home/kite/Maildir")
            return json.dumps(get_mails(mdir))

bottle.run(host='localhost', port='8080')
