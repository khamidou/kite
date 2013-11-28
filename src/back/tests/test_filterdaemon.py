import unittest
import kite.filterdaemon as filterdaemon

threads_index = {"data": {}}

class TestEmailProcessor(unittest.TestCase):
    def test_process_email(self):
        global threads_index
        filterdaemon.process_new_email("mocks/test_process_email.txt")
        self.assertTrue("Hey, How are you ?" in threads_index["data"])
