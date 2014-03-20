import io
import unittest

from WCBD import toElementTree, toString
from xml.etree.ElementTree import Element, fromstring

class TestXML (unittest.TestCase) :
    def test_toElementTree_1 (self):

    def test_toElementTree_2 (self):

    def test_toElementTree_3 (self):

    def test_toString_1 (self):
        r = StringIO.StringIO("<parent><child></child></parent>")
        w = StringIO.StringIO()
        WCBD_solve(r, w)
        self.assertTrue(w.getValue() == "<parent><child></child></parent>")

    def test_toString_2 (self):
        r = StringIO.StringIO("<parent></parent>")
        w = StringIO.StringIO()
        WCBD_solve(r, w)
        self.assertTrue(w.getValue() == "<parent></parent>")

    def test_toString_3 (self):
        r = StringIO.StringIO("<parent><child><grandchild></grandchild></child></parent>")
        w = StringIO.StringIO()
        WCBD_solve(r, w)
        self.assertTrue(w.getValue() == "<parent><child><grandchild></grandchild></child></parent>")
