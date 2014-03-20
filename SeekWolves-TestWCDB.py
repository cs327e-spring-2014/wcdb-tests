#Unit tests for project 3 - WCDB
#Nathanael Bonney 3-18-14

"""
To test the program:
    % python TestWCDB.py > TestWCDB.out
    % chmod ugo+x TestWCDB.py
"""

# -------
# imports
# -------

import StringIO
import unittest
import WCDB

from xml.etree.ElementTree import Element, fromstring, tostring, ParseError

# -------
# classes
# -------

class TestWCDB(unittest.TestCase):
  
# -------
# Test Functions
# -------

  #importXML
  def testImportXML1(self):
      sInput = StringIO.StringIO()
      sOutput = StringIO.StringIO()
      WCDB.importXML(sInput, sOutput)
      self.assert_(sOutput.getvalue() == "There was an error with your XML. Please submit well formed XML.")

  def testImportXML2(self):
      sInput = StringIO.StringIO("<xml><tag1><tag2 /></tag1><tag3 /></xml>")
      sOutput = StringIO.StringIO()
      WCDB.importXML(sInput, sOutput)
      self.assert_(sOutput.getvalue() == sInput.getvalue())

  def testImportXML3(self):
      sInput = StringIO.StringIO("<xml><1><2></2></1><3></xml>")
      sOutput = StringIO.StringIO()
      WCDB.importXML(sInput, sOutput)
      self.assert_(sOutput.getvalue() == "There was an error with your XML. Please submit well formed XML.")

  def testImportXML4(self):
      sOutput = StringIO.StringIO()
      WCDB.importXML(1, sOutput)
      self.assert_(sOutput.getvalue() == "Error. Could not read input.")

def main():
  print "TestWCDB.py"
  unittest.main()
  print "Done."

main()
