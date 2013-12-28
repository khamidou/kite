# users.py - user management functions + commandline tool
import os
import jsonfile

class UserError(Exception):
    pass


def create_user(name, _base_folder=os.path.expanduser("~")):
    """Create the basic structure for an user. Note: _base_folder is only used for testing"""
    try:
        os.mkdir(os.path.join(_base_folder, name))
    except OSError:
        raise UserError("Folder %s already exists" % name)
    
def get_threads_index_folder(email_path):
    """This function gets the directory where the threads_index file of an user is located.
    It's called by the inotify daemon with the full path of a new email.
    ex: get_threads_index_folder("/home/kite/Maildirs/testuser/new/1234563.mail") => "/home/kite/Maildirs/testuser"
    """
    return os.path.abspath(os.path.join(os.path.dirname(email_path), os.path.pardir))

def get_username_from_folder(email_path):
    """This function get the username from a maildir.
    ex: get_username_from_folder("/home/kite/Maildirs/testuser/new/1234563.mail") => "testuser" """
    fullpath = get_threads_index_folder(email_path)
    return os.path.basename(os.path.normpath(fullpath))

def get_user_threads_index(email_path):
    folder_name = get_threads_index_folder(email_path)
    fullpath = os.path.join(folder_name, "threads_index.json")

    jfile = jsonfile.JsonFile(fullpath)

    if not os.path.exists(fullpath): # the threads_index file doesn't exists yet
        jfile.data = []

    return jfile
