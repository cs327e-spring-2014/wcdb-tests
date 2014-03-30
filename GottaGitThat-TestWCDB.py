# ---------------------------------
# projects/WCDB(phase1)/TestWCDB.py
# Author: Xiaoqin LI
# Date: 03/09/2014
#----------------------------------

"""
To test the program:
python/python3 TestWCDB.py > TestWCDB.out
"""

# -------
# imports
# -------

import io
import unittest
import xml.etree.ElementTree as ET
from WCDB import *

# ----------------------------------
# TestWCDB.py, 9 unit tests in total
# including some major corner tests 
# ----------------------------------

class TestWCDB(unittest.TestCase):
  # -----------------------------------
  # wcdb_read fuction test 3 in total
  # tested reading tag, text and atttib
  # -----------------------------------
  
  def test_wcdb_read_tag(self):
    r = io.StringIO("<apple><bear><clear /><dog /></bear></apple>")
    root = wcdb_read(r)
    self.assertTrue(root.tag == "apple")
    self.assertTrue(root[0].tag == "bear")
    self.assertTrue(root[0][0].tag == "clear")
    self.assertTrue(root[0][1].tag == "dog")

  def test_wcdb_read_text(self):
    r = io.StringIO("<apple>hey hey<b /><c> </c></apple>")
    root = wcdb_read(r)
    self.assertTrue(root.text == "hey hey")
    self.assertTrue(root[0].text is None)
    self.assertTrue(root[1].text == " ")
    self.assertTrue(root.attrib == {})

  def test_wcdb_read_attrib(self):
    r = io.StringIO("<Book ISBN='ISBN-0-13-713526-2' Price='100'><Title ID = 'CS327'>Database</Title></Book>")
    root = wcdb_read(r)
    self.assertTrue(root.attrib == {'ISBN': 'ISBN-0-13-713526-2', 'Price': '100'})
    self.assertTrue(root[0].attrib == {'ID': 'CS327'})
    self.assertTrue(root[0].text == "Database")

  # ----------------------------------------------------
  # wcdb_write function test 3 in total
  # tested writing tag, text, atttib and nested elements
  # ----------------------------------------------------

  def test_wcdb_write_single_ele(self):
      w = io.StringIO()
      a = ET.Element('apple')
      wcdb_write(w, a)
      self.assertTrue(w.getvalue() == "<apple />")
      
  def test_wcdb_write_attrib_text(self):
      w = io.StringIO()
      a = ET.Element('apple')
      a.text = "hey hey"
      a.attrib = {'aa':'bb','price':'3'}
      wcdb_write(w, a)
      self.assertTrue(w.getvalue() == "<apple aa=\"bb\" price=\"3\">hey hey</apple>")

  def test_wcdb_write_nested_ele(self):
      w = io.StringIO()
      a = ET.Element('apple')
      b = ET.SubElement(a, 'bear')
      c = ET.SubElement(a, 'clear')
      d = ET.SubElement(b, 'dog')
      wcdb_write(w, a)
      self.assertTrue(w.getvalue() == "<apple><bear><dog /></bear><clear /></apple>")

  # ----------------------------------------------------
  # wcdb_solve function test 3 in total
  # ----------------------------------------------------
  
  # a simple test on nested tag
  def test_wcdb_solve_1(self):
      w1 = io.StringIO()
      w2 = io.StringIO()
      r = io.StringIO("<apple><bear><clear /><dog /></bear></apple>")
      wcdb_solve(r, w1)
      r2 = io.StringIO(w1.getvalue())
      wcdb_solve(r2, w2)
      self.assertTrue(w1.getvalue() == w2.getvalue())
      
  # test on tag, text and white space
  def test_wcdb_solve_2(self):
      w1 = io.StringIO()
      w2 = io.StringIO()
      r = io.StringIO("""
                      <THU>
                            <Team>
                                    <ACRush>clear</ACRush>
                                    <Jelly>dog</Jelly>
                                    <Cooly> \napple  </Cooly>
                            </Team>
                            <JiaJia>clear
                                    <Team> \t clear
                                            <Ahyangyi>  bear  </Ahyangyi>
                                            <Dragon> dog!@#</Dragon>
                                            <Cooly><Amber></Amber></Cooly>
                                    </Team>
                            </JiaJia>
                      </THU>""")
      wcdb_solve(r, w1)
      r2 = io.StringIO(w1.getvalue())
      wcdb_solve(r2, w2)
      self.assertTrue(w1.getvalue() == w2.getvalue())
      
  # adding attributes
  def test_wcdb_solve_3(self):
      w1 = io.StringIO()
      w2 = io.StringIO()
      r = io.StringIO("""
                      <Bookstore>
                           <Book ISBN="ISBN-0-13-713526-2" Price="100">
                              <Title>A First Course in Database Systems</Title>
                              <Authors>
                                 <Auth authIdent="JU" />
                                 <Auth authIdent="JW" />
                              </Authors>
                           </Book>
                           <Book ISBN="ISBN-0-13-815504-6" Price="85">
                              <Title>Database Systems: The Complete Book</Title>
                              <Authors>
                                 <Auth authIdent="HG" />
                                 <Auth authIdent="JU" />
                                 <Auth authIdent="JW" />
                              </Authors>
                              <Remark>
                                Amazon.com says: Buy this book bundled with
                                <BookRef book="ISBN-0-13-713526-2" /> - a great deal!
                              </Remark>
                           </Book>
                           <Author Ident="HG">
                              <First_Name>Hector</First_Name>
                              <Last_Name>Garcia-Molina</Last_Name>
                           </Author>
                           <Author Ident="JU">
                              <First_Name>Jeffrey</First_Name>
                              <Last_Name>Ullman</Last_Name>
                           </Author>
                           <Author Ident="JW">
                              <First_Name>Jennifer</First_Name>
                              <Last_Name>Widom</Last_Name>
                           </Author>
                      </Bookstore>""")
      wcdb_solve(r, w1)
      r2 = io.StringIO(w1.getvalue())
      wcdb_solve(r2, w2)
      self.assertTrue(w1.getvalue() == w2.getvalue())
     
     
print("TestWCDB.py")
print("Done.")
unittest.main()


