import bottle
import json
from bottle import route, template, response

@route('/kite/<user>/mail')
def index(user):
            response.content_type = "application/json"
            return json.dumps([
            {"from": "random.spam@spam.com",
             "to": "you",
             "subject": "-50% promo on everything !",
             "contents": "Everything must go !",
             "date": "2013-23-9"
            },
 
            {"from": "nigerian.prince@spam.com",
             "to": "user@mail.com",
             "subject": "I need your urgent help",
             "contents": "Hi my dear friend. I need your help urgently in a matter of financial problems.",
             "date": " 1992-04-05",
            },
            {"from": "team@kitemail",
             "name": "Kite team",
             "to": "user@mail.com",
             "subject": "Welcome to Kite !",
             "contents": "This is the basic inbox page. As you can see, it looks a lot like a famous email service.",
             "date": "1995-05-30"
            }])
    

bottle.run(host='localhost', port='8080')
