#!/usr/bin/env python3

# -------------------------------
# projects/WCDB/TestWCDB.py
# Copyright (C) 2014
# Noel Thomas
# -------
"""
To test the program:
    % python TestWCDB.py > TestWCDB.out
    % chmod ugo+x TestWCDB.py
"""

# -------
# imports
# -------

import io

import unittest

from xml.etree.ElementTree import Element, fromstring, tostring

from WCDB import xmlRead, xmlSolve
# -------
# classes
# -------

class TestWCDB(unittest.TestCase):
  
# -------
# Test Functions
# -------

    #normal
    def test_read1(self):
        r = io.StringIO("<A><B></B><C></C></A>")
        w = io.StringIO()
        st = xmlRead(r,w)
        self.assertTrue(st == "<A><B></B><C></C></A>")
    
    #tabs    
    def test_read2(self):
        r = io.StringIO("<A>\t<B>\t</B>\t<C>\t</C>\t</A>")
        w = io.StringIO()
        st = xmlRead(r,w)
        self.assertTrue(st =="<A>\t<B>\t</B>\t<C>\t</C>\t</A>")
        
    #newline character
    def test_read3(self):
        r = io.StringIO("<A>\n<B>\n</B>\n<C>\n</C>\n</A>")
        w = io.StringIO()
        st = xmlRead(r,w)
        self.assertTrue(st == "<A>\n<B>\n</B>\n<C>\n</C>\n</A>")
    
    #normal   
    def test_solve1(self):
        r = "<A><B></B><C></C></A>"
        st = fromstring("<xml>"+r+"</xml>")
        t = tostring(st, encoding ="utf-8")
        s1 = bytes.decode(t)
        s2 = s1[5:len(s1)-6]+"\n"
        w = io.StringIO()
        xmlSolve(r,w)
        self.assertTrue(w.getvalue() == s2)
    
    #tabs   
    def test_solve2(self):
        r = "<A>\t<B>\t</B>\t<C>\t</C>\t</A>"
        st = fromstring("<xml>"+r+"</xml>")
        t = tostring(st, encoding ="utf-8")
        s1 = bytes.decode(t)
        s2 = s1[5:len(s1)-6]+"\n"
        w = io.StringIO()
        xmlSolve(r,w)
        self.assertTrue(w.getvalue() == s2)
    
    #newline character     
    def test_solve3(self):
        r = "<A>\n<B>\n</B>\n<C>\n</C>\n</A>"
        st = fromstring("<xml>"+r+"</xml>")
        t = tostring(st, encoding ="utf-8")
        s1 = bytes.decode(t)
        s2 = s1[5:len(s1)-6]+"\n"
        w = io.StringIO()
        xmlSolve(r,w)
        self.assertTrue(w.getvalue() == s2)
  
print ("TestWCDB.py")
unittest.main()
print ("Done.")
