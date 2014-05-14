#!/usr/bin/env python
# add an user to Kite and Postfix
import sys
import os
import getopt
import config
from cabinet import DatetimeCabinet

def usage():
    print "%s: Add an user to kite and postfix. required arguments: --username user --password pass" % sys.argv[0]
    sys.exit(-1)

def add_kite_user(username, password):
    usersdb = DatetimeCabinet("/home/kite/users.db")
    usersdb[username] = {"password": password} # FIXME: hash password
    usersdb.sync()
   
def add_postfix_user(username):
    # FIXME: do something a little more serious than a superficial grep
    # for instance, slurp the file, get the first column and check the 
    # username isn't in it.
    with open('/etc/postfix/vmaps', 'r') as fd: 
        if username in fd.read():
            print "User already exists"
            return

    with open('/etc/postfix/vmaps', 'a') as fd:
        fd.write("%s@%s %s/\n" % (username, config.SERVER_NAME, username))

    os.system("postmap /etc/postfix/vmaps") 
    os.system("service postfix reload")

try:
    opts, args = getopt.getopt(sys.argv[1:], 'u:p:', ['username=', 'password='])
except getopt.GetoptError:
    usage()

username = None
password = None

for opt, arg in opts:
    if opt in ('-u', '--username'):
        username = arg
    elif opt in ('-p', '--password'):
        password = arg

if username == None or password == None:
    usage()

add_postfix_user(username)
add_kite_user(username, password)
