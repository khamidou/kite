from fcntl import flock, LOCK_EX, LOCK_UN

class LockingException(Exception):
    pass

class FileLock(object):
    def __init__(self, name, mode="rw+"):
        self.name = name
        self.fd = open(name, mode)

    def acquire(self):
        flock(self.fd.fileno(), LOCK_EX)

    def release(self):
        flock(self.fd.fileno(), LOCK_UN)
        self.fd.close()
        self.fd = None 

    def __enter__(self):
        self.acquire() # flock is blocking, so there's no need to handle a timeout
        return self

    def __exit__(self, type, value, traceback):
        self.release()
