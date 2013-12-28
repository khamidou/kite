import kite.maildir
import unittest
import types

mockdata = {"from": {"address": "gerard", "name": ""}, "subject": "test", "contents": "empty", "to": "gerard", "date": "November 13, 2007"}

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
    def __init__(self):
        self.mi = MockMailItem()
    def iteritems(self):
        return [("randomId", self.mi)]

    def get(self, id):
        if id == "randomId":
            return self.mi

# FIXME: write a better test
#class TestMailDir(unittest.TestCase):
#    def test_extract_email(self):
#        mi = MockMailItem()
#        self.assertEqual(kite.maildir.extract_email(mi), mockdata)
#          
#    def test_get_emails(self):
#        md = MockMailDir()
#        parsedMaildir = kite.maildir.get_emails(md)
#        self.assertEqual(len(parsedMaildir), 1)
#
#    def test_get_email(self):
#        md = MockMailDir()
#        parsedEmail = kite.maildir.get_email(md, "randomId")
#        self.assertEqual(parsedEmail, mockdata)
