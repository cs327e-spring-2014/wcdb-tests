import io
import unittest

from WCBD import toElementTree, toTheString, WCBD_solve
from xml.etree.ElementTree import Element, ElementTree, fromstring, tostring

class TestXML (unittest.TestCase) :
    def test_toElementTree_1 (self):
        print()

    def test_toElementTree_2 (self):
        print()
    def test_toElementTree_3 (self):
        print()

    #Tried renaming methods so as not to conflict with ElementTree's tostring method
    #ElementTree's tostring ended up returning bytes instead of a string
    #These are the remains of my attempt.
    def test_toTheString_1 (self):
        s = "<apple><orange></orange></apple>"
        x = fromstring(s)
        print(x)

        l = toTheString(x)
        self.assertTrue(l == "<apple><orange></orange></apple>")

    def test_toTheString_2 (self):
        s = "<a></a>"
        x = fromstring(s)
        l = toTheString(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<a></a>")

    def test_toTheString_3 (self):
        s = "<red><blue><green></green></blue></red>"
        x = fromstring(s)
        l = toTheString(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<red><blue><green></green></blue></red>")
        print("Yo finished toTheString")

    """
    Commented out solve methods for time being.
    """
    #def test_WCBD_solve_1 (self):
     #   r = io.StringIO("<parent><child></child></parent>")
      #  w = io.StringIO()
       # WCBD_solve(r, w)
        #self.assertTrue(w.getValue() == "<parent><child></child></parent>")

    #def test_WCBD_solve_2 (self):
     #   r = io.StringIO("<parent></parent>")
      #  w = io.StringIO()
       # WCBD_solve(r, w)
        #self.assertTrue(w.getValue() == "<parent></parent>")

    #def test_WCBD_solve_3 (self):
     #   r = io.StringIO("<parent><child><grandchild></grandchild></child></parent>")
      #  w = io.StringIO()
       # WCBD_solve(r, w)
        #self.assertTrue(w.getValue() == "<parent><child><grandchild></grandchild></child></parent>")
        #print("Yo i finished solve")

print("TestWCBD.py")

#Added unittest so it would actually run.
unittest.main()
print("Done.")