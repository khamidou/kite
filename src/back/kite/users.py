# users.py - user management functions
import os
import base64
import M2Crypto
from cabinet import DatetimeCabinet

class UserError(Exception):
    pass

def get_username_from_folder(email_path):
    """This function get the username from a maildir.
    ex: get_username_from_folder("/home/kite/Maildirs/testuser/new/1234563.mail") => "testuser" """
    # FIXME: refactor this monstrosity
    return os.path.basename(os.path.normpath(os.path.abspath(os.path.join(os.path.dirname(email_path), os.path.pardir))))

def auth_user(username, password):
    usersdb = DatetimeCabinet("/home/kite/users.db")
    if username not in usersdb:
        return False
    
    user = usersdb[username] 
    print user["password"]
    if user["password"] != password:
        return False

    return True    

def gen_token():
    return base64.b64encode(M2Crypto.m2.rand_bytes(32))
