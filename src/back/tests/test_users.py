import unittest
import kite.users as users

class TestUsers(unittest.TestCase):
    def test_path_cleanups(self):
        s = users.get_threads_index_folder("/home/kite/Maildirs/testuser/new/1234563.mail")
        self.assertEqual(s, "/home/kite/Maildirs/testuser")

        s = users.get_threads_index_folder("/home/kite/Maildirs/example.com/testuser/new/1234563.mail")
        self.assertEqual(s, "/home/kite/Maildirs/example.com/testuser")

        s = users.get_username_from_folder("/home/kite/Maildirs/testuser/new/1234563.mail")
        self.assertEqual(s, "testuser")

        s = users.get_username_from_folder("/home/kite/Maildirs/testuser/new/")
        self.assertEqual(s, "testuser")

