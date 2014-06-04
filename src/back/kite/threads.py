# threads management functions
import jsonfile
import datetime
import uuid
import base64
import os

def generate_random_id():
    # FIXME: maybe use better function ?
    return base64.b32encode(os.urandom(32))
    
def create_thread_structure():
    return {"date": datetime.datetime.utcnow(), "messages": [], "subject": "", "id": generate_random_id(), "unread": True}
