#!/usr/bin/env python
# filterdaemon.py 
# This background process creates indexes files for threads and filters.
#
# What is an index file ?
# =======================
#
# An index file is a JSON list which holds the paths to files in a conversation.
# The file name of an index file is of the form UUID4.json
#
# Why is it used ?
# ================
#
# Because building a list of the emails in a thread at each server request would 
# be madness.
#
# FIXME: support multiple users


import sys
import os
import pyinotify
import threading
import time
import email.parser

import threads
import headers
from jsonfile import JsonFile

# The architecture is pretty simple. This program is multithreaded.
# One thread is the producer. It uses inotify to detect changes to the
# fs. It writes in the events_queue.
#
# Another thread is the consumer. It processes the files to build an index of 
# threads (threads_index).
#
# Finally, there's a thread which periodically dumps the thread index.
events_queue = []

DUMPER_SLEEP_DURATION=20
EVENTS_QUEUE_PROCESSING_DELAY=10

class WatcherThread(threading.Thread):
    class EventHandler(pyinotify.ProcessEvent):
        def process_IN_CREATE(self, event):
            events_queue.append({"type": "create", "path": event.pathname})

        def process_IN_DELETE(self, event):
            events_queue.append({"type": "delete", "path": event.pathname})

    def __init__(self, path):
        threading.Thread.__init__(self)
        self.path = path

    def run(self):
        wm = pyinotify.WatchManager()
        mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE
        handler = WatcherThread.EventHandler()
        notifier = pyinotify.Notifier(wm, handler)
        wdd = wm.add_watch(self.path, mask, rec=True)
        notifier.loop()

class DumperThread(threading.Thread):
    def __init__(self, path, threads_index):
        threading.Thread.__init__(self)
        self.path = path
        self.threads_index = threads_index

    def run(self):
        while True:
            time.sleep(DUMPER_SLEEP_DURATION)
            print "Dumping threads index"
            self.threads_index.save()
            
def process_new_email(path, threads_index):
    with open(path, "r") as fd:
        parser = email.parser.HeaderParser()
        email_headers = parser.parse(fd)
        subject = email_headers.get("Subject")

        if subject != None:
            subject = headers.cleanup_subject(subject)
            if subject in threads_index.data:
                threads_index.data[subject].append(path)
            else:
                # create a new thread
                threads_index.data[subject] = [path]


class ProcessorThread(threading.Thread):
    def __init__(self, path, threads_index):
        threading.Thread.__init__(self)
        self.path = path

        self.threads_index = threads_index
    def run(self):
        while True:
            while len(events_queue) != 0:
                event = events_queue.pop(0)
                if event["type"] == "create":
                    try:
                        process_new_email(event["path"], self.threads_index)
                    except IOError:
                        # This may be a Postfix/Dovecot temporary file. Ignore it.
                        pass
                    
            time.sleep(EVENTS_QUEUE_PROCESSING_DELAY)


if __name__ == "__main__":
    path = sys.argv[1]
    print "Watching %s..." % path

    threads_index = JsonFile(os.path.join(path, "threads_index.json"))
    if threads_index.data == None:
            threads_index.data = {}

    watcher_thread = WatcherThread(path)
    processor_thread = ProcessorThread(path, threads_index)
    dumper_thread = DumperThread(path, threads_index)

    processor_thread.start()
    watcher_thread.start()
    dumper_thread.start()
