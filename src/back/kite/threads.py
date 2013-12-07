# threads management functions
import jsonfile
import datetime
import uuid
import os

def save_thread(parent_dir, name):
    path = os.path.join(parent_dir, name)
    jfile = jsonfile.JsonFile(path)
    jfile.save()

def create_thread(parent_dir):
    name = str(uuid.uuid4()) + ".json"
    save_thread(parent_dir, name)
    return name

def load_thread(parent_dir, uuid):
    path = os.path.join(parent_dir, name)

def create_thread_structure():
    return {"date": datetime.datetime.utcnow(), "messages": [], "subject": ""}

    


