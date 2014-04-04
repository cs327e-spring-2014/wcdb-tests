#!/usr/bin/env python3

"""
To test the program:
    % python TestWCDB.py > TestWCDB.out
    % chmod ugo+x TestWCDB.py
    % TestWCDB.py > TestWCDB.out
"""

#---------
#imports
#---------

import io
import unittest

from xml.etree.ElementTree import Element, fromstring, tostring

from WCDB import wcdb_read, wcdb_solve, wcdb_print, wcdb_element


#----------
#TestWCDB
#----------

class TestWCDB (unittest.TestCase) :

  #----
  #read
  #----

  def test_read (self) :
    r = io.StringIO("<Chocolate><Cake>Hello</Cake></Chocolate>")
    a = ['']
    b = wcdb_read (r,a)
    self.assertTrue(b == True)
    self.assertTrue(a[0] == "<Chocolate><Cake>Hello</Cake></Chocolate>")
        
  def test_read_2 (self) :
    r = io.StringIO("<Cookies>/n/t<Thin Mints></Thin Mints>/n/t<Samoas></Samoas>/n</Cookies>")
    a = ['']
    b = wcdb_read (r,a)
    self.assertTrue(b == True)
    self.assertTrue(a[0] == "<Cookies>/n/t<Thin Mints></Thin Mints>/n/t<Samoas></Samoas>/n</Cookies>")

  def test_read_3 (self) :
    r = io.StringIO("<Dates><Nineties>/t/t</Nineties><Eighties>/t</Eighties></Dates>")
    a = ['']
    b = wcdb_read (r,a)
    self.assertTrue(b == True)
    self.assertTrue(a[0] == "<Dates><Nineties>/t/t</Nineties><Eighties>/t</Eighties></Dates>")


  #------
  #element
  #------

  def test_element (self) :
    a = ['<one><two>three</two></one>']
    b = wcdb_element(a)
    self.assertTrue(b == '<one><two>three</two></one>')

  def test_element_2 (self) :
    a = ['<one></one>']
    b = wcdb_element(a)
    self.assertTrue(b == '<one />')

  def test_element_3 (self) :
    a = ['<one><two><three></three></two></one>']
    b = wcdb_element(a)
    self.assertTrue(b == '<one><two><three /></two></one>')
    

  #-----
  #print
  #-----

  def test_print (self):
    w = io.StringIO()
    root = '<one><two>three</two></one>'
    wcdb_print(w, root)
    self.assertTrue(w.getvalue() == '<one><two>three</two></one>\n\n')

  def test_print_2 (self):
    w = io.StringIO()
    root = '<one />'
    wcdb_print(w, root)
    self.assertTrue(w.getvalue() == '<one />\n\n')

  def test_print_3 (self):
    w = io.StringIO()
    root = '<one><two><three /></two></one>'
    wcdb_print(w, root)
    self.assertTrue(w.getvalue() == '<one><two><three /></two></one>\n\n')

  #-----
  #solve
  #-----

  def test_solve (self) :
    r = io.StringIO('<one><two>five</two></one>')
    w = io.StringIO()
    wcdb_solve(r,w)
    self.assertTrue(w.getvalue() == '<one><two>five</two></one>\n\n')

  def test_solve_2 (self) :
    r = io.StringIO('<one></one>')
    w = io.StringIO()
    wcdb_solve(r,w)
    self.assertTrue(w.getvalue() == '<one />\n\n')

  def test_solve_3 (self) :
    r = io.StringIO('<one><two><three></three></two></one>')
    w = io.StringIO()
    wcdb_solve(r,w)
    self.assertTrue(w.getvalue() == '<one><two><three /></two></one>\n\n')

print('TestWCDB.py')
unittest.main()
print('Done.')
