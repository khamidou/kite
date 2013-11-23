# serialize and deserialize to json.
# reading and writing is locking
import os
import json
from lockfile import FileLock

class JsonFile(object):
    def __init__(self, path=None):
        self.path = path
        self.data = None
        self.refresh()

    def refresh(self):
        if self.path != None:
            try:
                with FileLock(self.path):
                    fd = open(self.path, "r")
                    self.data = json.load(fd)
                    fd.close()
            except IOError:
                pass

    def save(self):
        def save_proper():
            with open(self.path, "w+") as fd:
                json.dump(self.data, fd)

        # Lock the file only if it already exists
        if os.path.exists(self.path):
            with FileLock(self.path):
                save_proper()
        else:
            save_proper()
        
