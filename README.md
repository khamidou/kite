## Kite, a modern webmail

Kite is a webmail designed to look a lot like gmail and to be easily deployable on a single server.
It's written in Javascript with Angularjs for the frontend, and in Python 2 for the backend.

This is very much alpha software, but I hope to have something usable in a couple months.

### How to run it

To run it, you'll need to have [vagrant](http://www.vagrantup.com/) installed.
When it's done, run the following commands :

    vagrant up
    vagrant ssh
    sudo -s -u kite
    cd /home/kite
    python app/back/kite/server.py 

After this, browse to http://192.168.50.4 . You should be greeted by a login window. Use whatever username/password combination to login.

### Contact/Help

I can be reached at contact@khamidou.com. It try to do my best to reply to all incoming email, but sometimes it may slip through.

regards,

Karim Hamidou
