import kite.lockfile
from kite.lockfile import FileLock
import unittest
import tempfile
import fcntl

class TestLockfile(unittest.TestCase):
    def test_lock(self):
        fd, path = tempfile.mkstemp()
        print "PATH ", path
        with FileLock(path, "r+w"):
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB) 
                assert False, "Flock should have failed"
            except IOError:
                pass
        
    

