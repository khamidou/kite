# A very thin layer over leveldb - it mostly serializes JSON back and forth.

import leveldb
import utils

try:
    import json
except ImportError:
    import simplejson as json


class Cabinet(object):
    """Persistent data storage using JSON and berkeley db"""
    def __init__(self, filename, encoder=json.JSONEncoder, decoder=None, *args):
        """Set up a Cabinet object.

        The encoder parameter is the class that will be called by the json encoder to encode python objects.
        decoder is a function which is called for each decoded object to apply special conversions.
        For more informations, see :
        http://docs.python.org/dev/library/json.html?highlight=json#encoders-and-decoders
        """
        self.filename = filename
        self.cache = {}
        self.encoder = encoder
        self.decoder = decoder

    def __getitem__(self, key):
        if self.cache.has_key(key):
            return self.cache[key]
        else:
            db = leveldb.LevelDB(self.filename)
            val = db.Get(key)
            del db
            self.cache[key] = json.loads(val, object_hook=self.decoder)
            return self.cache[key]

    def __setitem__(self, key, item):
        self.cache[key] = item

    def __delitem__(self, key):
        del self.cache[key]
        db = leveldb.LevelDB(self.filename)
        db.Delete(key)
        del db

    def __iter__(self):
        try:
            db = leveldb.LevelDB(self.filename)
            return 
        finally:
            del db

    def __contains__(self, key):
        if self.cache.has_key(key):
            return True
        else:
            try:
                db = leveldb.LevelDB(self.filename)
                db.Get(key)
                del db
                return True
            except KeyError:
                return False

    def sync(self):
        db = leveldb.LevelDB(self.filename)
        for key in self.cache:
            db.Put(key, json.dumps(self.cache[key], cls=self.encoder))
        del db

def DatetimeCabinet(path):
    return Cabinet(path, encoder=utils.DatetimeEncoder, decoder=utils.deserialize_datetime)
