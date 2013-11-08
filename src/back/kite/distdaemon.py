# distdaemon.py 
# Postfix forwards all the emails sent and received by the machine
# to one maildir.
#
# This background process distributes the emails to each user.
#
# It also handles email threads and filters.

import time
import fcntl
import os
import signal
import utils
import time

# FIXME: swap this out someday with inotify, or python-watchdog
watched_dirs = {}
last_check_time = 0

def handler(signum, frame):
    for dirname in watched_dirs:
        dir = watched_dirs[dirname]
        mtime = os.path.getmtime(dirname)
        if mtime > last_check_time:
            print "found modified folder"
        last_check_time = int(time.time())

signal.signal(signal.SIGIO, handler)

def watch_dir(dirname):
    if dirname in watched_dirs:
        return
    
    fd = os.open(dirname,  os.O_RDONLY)
    watched_dirs[dirname] = {fd: fd}
    watched_dirs[dirname]["mtime"] = os.path.getmtime(dirname)

    fcntl.fcntl(fd, fcntl.F_SETSIG, 0)
    fcntl.fcntl(fd, fcntl.F_NOTIFY,
                fcntl.DN_MODIFY | fcntl.DN_CREATE | fcntl.DN_MULTISHOT)

def find_modified_files(folder):
    for file in os.listdir(folder):
        if os.path.getmtime(os.path.join(folder, file)) >= dir_mtime:
            print "file %s modified" % file

watch_dir("/tmp/t")
while True:
    time.sleep(10000)
