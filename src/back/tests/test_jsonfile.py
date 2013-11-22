import unittest
import tempfile
import fcntl
import os
import kite.jsonfile
from kite.jsonfile import JsonFile

class TestJsonfile(unittest.TestCase):
    def test_locked_loading(self):
        fd, path = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        fd.write("{}")
        fd.close()
        json_file = JsonFile(path)
        self.assertEqual(json_file.data, {}, msg="Value is not deserialized correctly")

        fd = open(path, "w+")
        fd.write("[]")
        fd.close()
        json_file.refresh()
        self.assertEqual(json_file.data, [], msg="Value is not refreshed correctly")
