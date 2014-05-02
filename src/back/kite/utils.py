# utils.py : various utilities
import os
import json
import datetime
import time
import dateutil.parser
import dateutil.tz


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)

def serialize_json(obj):
    return json.dumps(obj, cls=DatetimeEncoder)

def deserialize_json(string):
    return json.loads(string, object_hook=deserialize_datetime)

def deserialize_datetime(obj):
    try:
        obj['date'] = dateutil.parser.parse(obj['date'])
    except KeyError:
        pass
    return obj
