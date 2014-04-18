import StringIO
import unittest

from WCDB import *
from xml.etree.ElementTree import Element, fromstring, tostring

class TestWCDB3 (unittest.TestCase) :

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
     
    def test_getElement (self):
        t = "<red><blue> yellow </blue></red>"
        x = fromstring(t)
        y = getElement(x, 'blue')
        z = "\' yellow \'"
        self.assertTrue(y == z)

    def test_getElement_2 (self):
        t = "<baby><dicks> breakfast </dicks></baby>"
        x = fromstring(t)
        y = getElement(x, 'dicks')
        z = "\' breakfast \'"
        self.assertTrue(y == z)

    def test_getElement_3 (self):
        t = "<smoke><weed> dogg </weed></smoke>"
        x = fromstring(t)
        y = getElement(x, 'weed')
        z = "\' dogg \'"
        self.assertTrue(y == z)

    def test_getElement_4 (self):
        t = "<jam><bread> cheese </bread></jam>"
        x = fromstring(t)
        y = getElement(x, 'bread')
        z = "\' cheese \'"
        self.assertTrue(y == z)
        
    def test_getElement_5 (self):
        t = "<cat><mouse> lick </mouse></cat>"
        x = fromstring(t)
        y = getElement(x, 'mouse')
        z = "\' lick \'"
        self.assertTrue(y == z)  
    
    def test_getSQLsubclass_1 (self):
        st = "Crises"
        y = getSQLsubclass(st)
        self.assertTrue(y == "crisis")
        
    def test_getSQLsubclass_2 (self):
        st = "Citations"
        y = getSQLsubclass(st)
        self.assertTrue(y == "citationPair")
        
    def test_getSQLsubclass_3 (self):
        st = "OrgPeople"
        y = getSQLsubclass(st)
        self.assertTrue(y == "orgPersonPair")

    def test_getSQLsubclass_4 (self):
        st = "CrisisOrgs"
        y = getSQLsubclass(st)
        self.assertTrue(y == "crisisOrgPair")
    def test_getSQLsubclass_5 (self):
        st = "OrgContactInfos"
        y = getSQLsubclass(st)
        self.assertTrue(y == "orgContactInfoPair")


print("Testing TestWCDB.py")
unittest.main()
print("Done")
