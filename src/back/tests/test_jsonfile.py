import unittest
import tempfile
import fcntl
import os
import datetime
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

    def test_datetime_serialization(self):
        d = datetime.datetime.now()
        json_file = JsonFile()
        json_file.data = {"date": d} 
        json_file.save(self.tmpfile)

        json_file2 = JsonFile(self.tmpfile)
        self.assertTrue(isinstance(json_file2.data["date"], datetime.datetime), msg="Datetime value is not deserialized correctly")
