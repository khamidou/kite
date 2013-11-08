import os
import unittest
import tempfile
import fcntl
import kite.users

class TestLockfile(unittest.TestCase):
    def test_creation(self):
        tmpdir = tempfile.mkdtemp()
        kite.users.create_user("charles", _base_folder=tmpdir)
        self.assertTrue(os.path.exists(os.path.join(tmpdir, "charles")))

        try:
            # Creating the file twice raises an error
            kite.users.create_user("charles", _base_folder=tmpdir)
            assert False, "Exception should have been raised"
        except kite.users.UserError:
            pass
