import kite.maildir
import unittest
import types

mockdata = {"from": "gerard", "subject": "test", "contents": "empty", "to": "gerard"}

class EmptyObject(object):
    """Empty class used by mocks. Required because python doesn't let us add attributes
    to an empty object()"""
    pass

class MockMailItem(object):
    def __init__(self):
        self.fp = EmptyObject()
        self.fp.read = types.MethodType(lambda self: mockdata["contents"], self.fp)

    def getheaders(self, header):
        hd = header.lower()
        if hd in mockdata:
            return (mockdata[hd], "Nulltuple")
    
class MockMailDir(object):
    def iteritems(self):
        mi = MockMailItem()
        return [("randomId", mi)]


class TestMaildir(unittest.TestCase):
    def test_get_mails(self):
        md = MockMailDir()
        parsedMaildir = kite.maildir.get_mails(md)
        self.assertEqual(len(parsedMaildir), 1)

        firstEmail = parsedMaildir[0]
        self.assertEqual(firstEmail["id"], 0)

        del firstEmail["id"] 
        self.assertEqual(firstEmail, mockdata)
