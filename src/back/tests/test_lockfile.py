import kite.lockfile
from kite.lockfile import FileLock
import unittest
import tempfile
import fcntl
import tmpdir

class TestLockfile(tmpdir.TestCaseWithTempFile):
    def test_lock(self):
        with FileLock(self.tmpfile, "r+w"):
            try:
                fcntl.flock(self.tmpfd, fcntl.LOCK_EX | fcntl.LOCK_NB) 
                assert False, "Flock should have failed"
            except IOError:
                pass
        
    

