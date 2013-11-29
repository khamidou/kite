import unittest
import kite.filterdaemon as filterdaemon


class TestEmailProcessor(unittest.TestCase):
    def test_process_email(self):
        threads_index = {"data": {}}
        filterdaemon.process_new_email("mocks/test_process_email.txt", threads_index)
        self.assertTrue("Hey, How are you ?" in threads_index["data"])
