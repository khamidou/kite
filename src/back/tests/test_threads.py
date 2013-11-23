import unittest
import fcntl
import os
import tmpdir
import kite.threads as threads

class TestJsonfile(tmpdir.TestCaseWithTempDir):
    def test_saving(self):
        id = threads.create_thread(self.tmpdir)
        file_path = os.path.join(self.tmpdir, id)
        self.assertTrue(os.path.exists(file_path))
        
        

