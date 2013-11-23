import unittest
import tempfile
import fcntl
import os
import kite.jsonfile
import tmpdir
from kite.jsonfile import JsonFile

class TestJsonfile(tmpdir.TestCaseWithTempFile):
    def test_locked_loading(self):
        fd = os.fdopen(self.tmpfd, "w")
        fd.write("{}")
        fd.close()
        json_file = JsonFile(self.tmpfile)
        self.assertEqual(json_file.data, {}, msg="Value is not deserialized correctly")

        fd = open(self.tmpfile, "w+")
        fd.write("[]")
        fd.close()
        json_file.refresh()
        self.assertEqual(json_file.data, [], msg="Value is not refreshed correctly")
