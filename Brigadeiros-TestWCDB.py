#!/usr/bin/env python3

# -----------
# TestWCDB.py
# Brigadeiros
# -----------

'''
Testing this program :
 % python3 TestWCDB.py >& TestWCDB.out
'''

# -------
# imports
# -------

import io
import unittest

from WCDB import importXML, exportXML
from xml.etree.ElementTree import Element, fromstring, tostring, tostringlist

# --------
# TestWCDB
# --------

class TestWCDB (unittest.TestCase) :
  # ---------
  # importXML
  # ---------

  def test_importXML_1 (self):
    xml = io.StringIO ("<root> <crises> Barrack Obama </crises> </root>")
    out = importXML (xml) 
    self.assertTrue(type(out) is Element)

  def test_importXML_2 (self):
    xml = io.StringIO ("<root> </root>")
    out = importXML (xml) 
    self.assertTrue(type(out) is Element)
  
  def test_importXML_3 (self):
    xml = io.StringIO ("<root> <crises> <crisis> 1 </crisis> </crises> </root>")
    out = importXML (xml) 
    self.assertTrue(type(out) is Element)
 
  # ---------
  # exportXML
  # ---------
  def test_exportXML_1 (self):
    w = io.StringIO ()
    xml = "<root> <crises> Barrack Obama </crises> </root>"
    elt = fromstring(xml)
    exportXML(elt, w)
    s = w.getvalue()
    self.assertTrue(s == xml)

  def test_exportXML_2 (self):
    w = io.StringIO ()
    xml = "<root> </root>"
    elt = fromstring(xml)
    exportXML(elt, w)
    s = w.getvalue()
    self.assertTrue(s == xml)

  def test_exportXML_3 (self):
    w = io.StringIO ()
    xml = "<root> <crises> <crisis> 1 </crisis> </crises> </root>"
    elt = fromstring(xml)
    exportXML(elt, w)
    s = w.getvalue()
    self.assertTrue(s == xml)

# ----
# main
# ----

print("TestWCDB.py")
unittest.main()
print("Done.")
