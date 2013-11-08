# users.py - user management functions + commandline tool
import os

class UserError(Exception):
    pass


def create_user(name, _base_folder=os.path.expanduser("~")):
    """Create the basic structure for an user. Note: _base_folder is only used for testing"""
    try:
        os.mkdir(os.path.join(_base_folder, name))
    except OSError:
        raise UserError("Folder %s already exists" % name)
    
    
