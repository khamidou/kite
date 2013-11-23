# filterdaemon.py 
# This background process creates metadata files for threads and filters.
#
import sys
import pyinotify
import threads
from jsonfile import JsonFile

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname

def init(path):
    handler = EventHandler()
    notifier = pyinotify.Notifier(wm, handler)
    wdd = wm.add_watch(path, mask, rec=True)
    threads_index = JsonFile(os.path.join(path, "threads_index.json"))
    if threads_index.data == None:
        threads_index.data = {}


    notifier.loop()

if __name__ == "__main__":
    init(sys.argv[1])
