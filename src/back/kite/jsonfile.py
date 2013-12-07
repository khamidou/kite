# serialize and deserialize to json.
# reading and writing is locking
import os
import json
import datetime
import dateutil.parser
from lockfile import FileLock

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%y-%m-%dT%H:%M:%S+00:00")

        return json.JSONEncoder.default(self, obj)

def deserialize_datetime(obj):
    try:
        obj['date'] = dateutil.parser.parse(obj['date'])
    except KeyError:
        pass
    return obj

 
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
                    self.data = json.load(fd, object_hook=deserialize_datetime)
                    fd.close()
            except IOError:
                pass

    def save(self, path=None):
        if path == None:
            path = self.path

        def save_proper():
            with open(path, "w+") as fd:
                json.dump(self.data, fd, cls=DatetimeEncoder)

        # Lock the file only if it already exists
        # FIXME: this is maybe a race condition
        if os.path.exists(path):
            with FileLock(path):
                save_proper()
        else:
            save_proper()
        
