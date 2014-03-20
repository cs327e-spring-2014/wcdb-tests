import io
import unittest

from WCBD import toElementTree, toString
from xml.etree.ElementTree import Element, fromstring

class TestXML (unittest.TestCase) :
    def test_toElementTree_1 (self):

    def test_toElementTree_2 (self):

    def test_toElementTree_3 (self):

    def test_toString_1 (self):
        s = "<apple><orange></orange></apple>"
        x = fromstring(s)
        l = toString(x)
        self.assertTrue(l == "<apple><orange></orange></apple>")

    def test_toString_2 (self):
        s = "<a></a>"
        x = fromstring(s)
        l = toString(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<a></a>")

    def test_toString_3 (self):
        s = "<red><blue><green></green></blue></red>"
        x = fromstring(s)
        l = toString(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<red><blue><green></green></blue></red>")
        
    def test_WCBD_solve_1 (self):
        r = StringIO.StringIO("<parent><child></child></parent>")
        w = StringIO.StringIO()
        WCBD_solve(r, w)
        self.assertTrue(w.getValue() == "<parent><child></child></parent>")

    def test_WCBD_solve_2 (self):
        r = StringIO.StringIO("<parent></parent>")
        w = StringIO.StringIO()
        WCBD_solve(r, w)
        self.assertTrue(w.getValue() == "<parent></parent>")

    def test_WCBD_solve_3 (self):
        r = StringIO.StringIO("<parent><child><grandchild></grandchild></child></parent>")
        w = StringIO.StringIO()
        WCBD_solve(r, w)
        self.assertTrue(w.getValue() == "<parent><child><grandchild></grandchild></child></parent>")
