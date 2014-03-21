import io
import unittest

from WCDB import *
from xml.etree.ElementTree import Element, fromstring, tostring

class TestXML (unittest.TestCase) :
    def test_toElementTree_1 (self):
        s= "<apple><orange></orange></apple>"
        x = toElementTree(s)
        v = tostring(x)
        self.assertTrue(v == "<apple><orange></orange></apple>")

    def test_toElementTree_2 (self):
        s= "<apple> this is an apple </apple>"
        x = toElementTree(s)
        v = tostring(x)
        self.assertTrue(v == "<apple> this is an apple </apple>")
    def test_toElementTree_3 (self):
        s= "<a>comment</a>"
        x = toElementTree(s)
        v = tostring(x)
        self.assertTrue(v == "<a>comment</a>")

    def test_toXML_1 (self):
        s = "<apple><orange></orange></apple>"
        x = fromstring(s)
        l = toXML(x)
        self.assertTrue(l == "<apple><orange></orange></apple>")

    def test_toXML_2 (self):
        s = "<a></a>"
        x = fromstring(s)
        l = toXML(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<a></a>")

    def test_toXML_3 (self):
        s = "<red><blue><green></green></blue></red>"
        x = fromstring(s)
        l = toXML(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<red><blue><green></green></blue></red>")

    def test_WCBD_solve_1 (self):
        r = io.StringIO("<parent><child></child></parent>")
        w = io.StringIO()
        WCDB_solve(r, w)
        self.assertTrue(w.getValue() == "<parent><child></child></parent>")

    def test_WCBD_solve_2 (self):
        r = io.StringIO("<parent></parent>")
        w = io.StringIO()
        WCDB_solve(r, w)
        self.assertTrue(w.getValue() == "<parent></parent>")

    def test_WCBD_solve_3 (self):
        r = io.StringIO("<parent><child><grandchild></grandchild></child></parent>")
        w = io.StringIO()
        WCDB_solve(r, w)
        self.assertTrue(w.getValue() == "<parent><child><grandchild></grandchild></child></parent>")

print("Testing TestWCDB.py")
unittest.main()
print("Done")