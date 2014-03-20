import io
import unittest

from WCBD import toElementTree, toString
from xml.etree.ElementTree import Element, fromstring

class TestXML (unittest.TestCase) :
    def test_toElementTree_1 (self):

    def test_toElementTree_2 (self):

    def test_toElementTree_3 (self):

    def test_toString_1 (self):
        s = "<parent><child></child></parent>"
        x = fromstring(s)
        l = toString(x)
        self.assertTrue(l == "<parent><child></child></parent>")

    def test_toString_2 (self):
        s = "<parent></parent>"
        x = fromstring(s)
        l = toString(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<parent></parent>")

    def test_toString_3 (self):
        s = "<parent><child><grandchild></grandchild></child></parent>"
        x = fromstring(s)
        l = toString(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<parent><child><grandchild></grandchild></child></parent>")

