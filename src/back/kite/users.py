# users.py - user management functions + commandline tool
import os
import jsonfile

class UserError(Exception):
    pass

def get_username_from_folder(email_path):
    """This function get the username from a maildir.
    ex: get_username_from_folder("/home/kite/Maildirs/testuser/new/1234563.mail") => "testuser" """
    # FIXME: refactor this monstrosity
    return os.path.basename(os.path.normpath(os.path.abspath(os.path.join(os.path.dirname(email_path), os.path.pardir))))

def auth_user(username, password):
    return True    

def gen_token(username, password):
    return "BLAHBLAH"
