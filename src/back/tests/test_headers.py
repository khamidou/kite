import unittest
import kite.headers as headers

class TestCleanup(unittest.TestCase):
    def test_subject_cleanup(self):
        s = headers.cleanup_subject("Your question")
        self.assertEqual(s, "Your question")

        s = headers.cleanup_subject("Re: Re: Your question")
        self.assertEqual(s, "Your question")

        s = headers.cleanup_subject("Re: RE: FWD: Your question")
        self.assertEqual(s, "Your question")
