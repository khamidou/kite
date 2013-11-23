# base class for tests who need a temporary directory
import unittest
import shutil
import tempfile
import os

class TestCaseWithTempDir(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

class TestCaseWithTempFile(unittest.TestCase):
    def setUp(self):
        self.tmpfd, self.tmpfile = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.tmpfile)


