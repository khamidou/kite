# filterdaemon.py 
# This background process creates metadata files for threads and filters.
#
import sys
import os
import pyinotify
import threading
import time
import email.parser

import threads
from jsonfile import JsonFile

# The architecture is pretty simple. This program is multithreaded.
# One thread is the producer. It uses inotify to detect changes to the
# fs. It writes in the events_queue.
#
# Another thread is the consumers. It processes the files.
events_queue = []
threads_index = {} # the email thread index - this is a dictionnary pointing to the threads filenames

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
        wm = pyinotify.WatchManager()  # Watch Manager
        mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events
        handler = WatcherThread.EventHandler()
        notifier = pyinotify.Notifier(wm, handler)
        wdd = wm.add_watch(self.path, mask, rec=True)
        notifier.loop()

class ProcessorThread(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)
        self.path = path

    def run(self):
        threads_index = JsonFile(os.path.join(self.path, "threads_index.json"))
        if threads_index.data == None:
            threads_index.data = {}

        while True:
            while len(events_queue) != 0:
                print "Found an event!"
                event = events_queue.pop(0)
                if event["type"] == "create":
                    try:
                        with open(event["path"], "r") as fd:
                            headers = email.parser.Parser()
                            headers.parse(fd, headersonly=True)
                            for header in headers:
                                print header
                    except IOError:
                        pass
                    
            time.sleep(10)


if __name__ == "__main__":
    watcher_thread = WatcherThread(sys.argv[1])
    processor_thread = ProcessorThread(sys.argv[1])

    watcher_thread.start()
    processor_thread.start()
