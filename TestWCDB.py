import StringIO
import unittest

from WCDB import *
from xml.etree.ElementTree import Element, fromstring, tostring

class TestXML (unittest.TestCase) :

    def test_toElementTree_1 (self):
        s = "<apple><orange>a</orange></apple>"
        x = toElementTree(s)
        v = tostring(x)
        self.assertTrue(v == "<apple><orange>a</orange></apple>")

    def test_toElementTree_2 (self):
        s = "<apple> <red> this is an apple</red> </apple>"
        x = toElementTree(s)
        v = tostring(x)
        self.assertTrue(v == "<apple> <red> this is an apple</red> </apple>")
    
    def test_toElementTree_3 (self):
        s = "<b><a>comment</a></b>"
        x = toElementTree(s)
        v = tostring(x)
        self.assertTrue(v == "<b><a>comment</a></b>")
    
    def test_toXML_1 (self):
        s = "<apple><orange> apples and oranges </orange></apple>"
        x = fromstring(s)
        l = toXML(x)
        self.assertTrue(l == "<apple><orange> apples and oranges </orange></apple>")

    def test_toXML_2 (self):
        s = "<a> hello </a>"
        x = fromstring(s)
        l = toXML(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<a> hello </a>")

    def test_toXML_3 (self):
        s = "<red><blue><green> yellow </green></blue></red>"
        x = fromstring(s)
        l = toXML(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<red><blue><green> yellow </green></blue></red>")

        
    def test_WCBD_solve_1 (self):
        r = StringIO.StringIO('<parent><child> mom </child></parent>')
        w = StringIO.StringIO()
        WCDB_solve(r, w)
        self.assertTrue(w.getvalue() == '<parent><child> mom </child></parent>\n')

    def test_WCBD_solve_2 (self):
        r = StringIO.StringIO('<parent>daddy</parent>')
        w = StringIO.StringIO()
        WCDB_solve(r, w)
        self.assertTrue(w.getvalue() == '<parent>daddy</parent>\n')

    def test_WCBD_solve_3 (self):
        r = StringIO.StringIO('<parent><child><grandchild>baby</grandchild></child></parent>')
        w = StringIO.StringIO()
        WCDB_solve(r, w)
        self.assertTrue(w.getvalue() == '<parent><child><grandchild>baby</grandchild></child></parent>\n')

print("Testing TestWCDB.py")
unittest.main()
print("Done")
