import unittest
import kite.filterdaemon as filterdaemon


class TestEmailProcessor(unittest.TestCase):
    def test_process_email(self):
        class MockThreadsIndex(object):
            def __init__(self):
                self.data = []

        threads_index = MockThreadsIndex()
        filterdaemon.process_new_email("mocks/test_process_email.txt", threads_index)
        self.assertTrue("Hey, How are you ?" == threads_index.data[0]["subject"])
