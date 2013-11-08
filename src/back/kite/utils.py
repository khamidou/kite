# utils.py : various utilities

import os

def stat(fd):
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
    ret = {}
    ret["atime"] = atime
    ret["ctime"] = ctime
    ret["mtime"] = mtime
    return ret
