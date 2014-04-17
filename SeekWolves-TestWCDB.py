#!/usr/bin/env python

# -------------------------------
# projects/WCDB2/TestWCDB2.py
# Copyright (C) 2014
# Andrea Curo, Nathanael Bonney
# -------
"""
To test the program:
% python TestWCDB2.py > TestWCDB2.out
% chmod ugo+x TestWCDB2.py
"""

# -------
# imports
# -------

import StringIO
import unittest
import _mysql
from xml.etree.ElementTree import Element, fromstring, tostring
from WCDB import createTables, login, query, dropAll, xmlRead, xmlElementTree, iterTree, xmlInsert, xmlExport, dataExist, clean, normTableTracker, removeDuplicates, subInsert 
import WCDB

# -------
# globals
# -------

c = _mysql.connect(host = "z", user = "python1", passwd = "VEXYOWWk7X", db = "cs327e_python1")

# -------
# classes
# -------

class TestWCDB3(unittest.TestCase):

    # --------
    # setUp - Runs before every test to ensure the database is consistent
    # --------

    def setUp(self):
        w = StringIO.StringIO()
        xmlRead(open("RunWCDB.in.xml" , "r"), c, w)

    # ------------
    # createTables
    # ------------

    def test_createTables_1(self):
        self.assertTrue(createTables(c))

    def test_createTables_2(self):
        t = query(c, "Show Tables")
        st = (('citations',), ('contactInfos',), ('crises',), ('crisisCitations',), ('crisisOrgs',), ('crisisPeople',), ('crisisResources',), ('crisisUrls',), ('crisisWaysToHelp',), ('orgCitations',), ('orgContactInfos',), ('orgPeople',), ('orgUrls',), ('orgs',), ('people',), ('personCitations',), ('personUrls',), ('resources',), ('urls',), ('waysToHelp',))
        self.assertTrue(sorted(t) == sorted(st))

    def test_createTables3(self):
        self.assertTrue(not createTables(1))

    # --------
    # dropAll
    # --------

    def test_dropAll_1(self):
        self.assertTrue(dropAll(c))

    def test_dropAll_2(self):
        dropAll(c)
        self.assertTrue(WCDB.activeTables == [])

    def test_dropAll_3(self):
        dropAll(c)
        self.assertTrue(WCDB.syntax == {})

    def test_dropAll_4(self):
        dropAll(c)
        self.assertTrue(WCDB.values == {})


    # --------
    # login
    # --------
    
    def test_login_1(self):
        self.assertTrue(str(type(login()) == "<type '_mysql.connection'>"))

    # --------
    # query
    # --------

    def test_query_1(self):
        s = "drop table if exists crisis"
        t = query(c, s)
        self.assertTrue(t == None)

    def test_query_2(self):
        s = "Show Tables"
        t = query(c, s)
        self.assertTrue(t == (('citations',), ('contactInfos',), ('crises',), ('crisisCitations',), ('crisisOrgs',), ('crisisPeople',), ('crisisResources',), ('crisisUrls',), ('crisisWaysToHelp',), ('orgCitations',), ('orgContactInfos',), ('orgPeople',), ('orgUrls',), ('orgs',), ('people',), ('personCitations',), ('personUrls',), ('resources',), ('urls',), ('waysToHelp',)))

    def test_query_3(self):
        s = "Show Databases"
        t = query(c, s)
        self.assertTrue(t == (('information_schema',), ('cs327e_python1',)))

    # --------
    # xmlRead 
    # --------
    def test_read1(self):
        t = "<A><B></B></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B></A>")

    def test_read2(self):
        t = "<A><B><C></C></B></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B><C></C></B></A>")

    def test_read3(self):
        t = "<A><B><C><D></D></C></B></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B><C><D></D></C></B></A>")

    def test_read4(self):
        t = "<A><B><C><D><E></E></D></C></B></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B><C><D><E></E></D></C></B></A>")

    def test_read5(self):
        t = "<A><B><C><D><E><F></F></E></D></C></B></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B><C><D><E><F></F></E></D></C></B></A>")

    def test_read6(self):
        t = "<A><B></B><C></C></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C></A>")

    def test_read7(self):
        t = "<A><B></B><C></C><D></D></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D></A>")

    def test_read8(self):
        t = "<A><B></B><C></C><D></D><E></E></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E></A>")

    def test_read9(self):
        t = "<A><B></B><C></C><D></D><E></E><F></F></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E><F></F></A>")

    def test_read10(self):
        t = "<A><B></B><C></C><D></D><E></E><F></F><G></G></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E><F></F><G></G></A>")

    def test_read11(self):
        t = "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H></A>")

    def test_read12(self):
        t = "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I></A>")

    def test_read13(self):
        t = "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J></A>")

    def test_read14(self):
        t = "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J><K></K></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J><K></K></A>")

    def test_read15(self):
        t = "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J><K></K><L></L></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J><K></K><L></L></A>")

    def test_read16(self):
        t = "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J><K></K><L></L><M></M></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J><K></K><L></L><M></M></A>")

    def test_read17(self):
        t = "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J><K></K><L></L><M></M><N></N></A>"
        w = StringIO.StringIO()
        result = xmlRead(t, c, w)
        st = str(result)
        self.assertTrue(st == "<A><B></B><C></C><D></D><E></E><F></F><G></G><H></H><I></I><J></J><K></K><L></L><M></M><N></N></A>")

    # --------
    # xmlElementTree
    # --------

    def test_xmlElementTree_1(self):
        st = "<A><B></B></A>"
        w = StringIO.StringIO()
        self.assertTrue(xmlElementTree(st, w, c))


    # -------
    # iterTree
    # -------

    def test_iterTree_1(self):
        x = fromstring("<A><B></B></A>")
        self.assertTrue(iterTree(x, ""))
    
    # ---------
    # xmlInsert
    # ---------

    def test_xmlInsert_1(self):
        self.assertTrue(xmlInsert(c))

    # ---------
    # xmlsubInsert
    # ---------

    def test_subInsert_1(self):
        self.assertTrue(subInsert(0, "", c, "'PER_002', 'CIT_010',,", "personCitations") == 1)

    def test_subInsert_2(self):
        self.assertTrue(subInsert(12, "", c, "'PER_004', 'CIT_050',,", "personCitations") == 13)

    def test_subInsert_3(self):
        self.assertFalse(subInsert(0, 0, 0, 0, 0))

    # ---------
    # xmlImport
    # ---------
    def test_xmlExport_1(self):
        w = StringIO.StringIO()
        self.assertTrue(xmlExport(c,w))

    # ---------
    # removeDuplicates
    # ---------
    def test_removeDuplicates_1(self):
        self.assertTrue(removeDuplicates(c))

    def test_removeDuplicates_2(self):
        removeDuplicates(c)
        s = "select * from crises;"
        t = query(c, s)
        viewedRows = []
        for row in t:
            self.assertNotIn(row, viewedRows)
            viewedRows.append(row)
        self.assertTrue(True)

    def test_removeDuplicates_3(self):
        removeDuplicates(c)
        s = "select * from people;"
        t = query(c, s)
        viewedRows = []
        for row in t:
            self.assertNotIn(row, viewedRows)
            viewedRows.append(row)
        self.assertTrue(True)
        
    def test_removeDuplicates_4(self):
        removeDuplicates(c)
        s = "select * from orgs;"
        t = query(c, s)
        viewedRows = []
        for row in t:
            self.assertNotIn(row, viewedRows)
            viewedRows.append(row)
        self.assertTrue(True)

    # ---------
    # clean (normalize)
    # ---------
    def test_clean_1(self):
        self.assertTrue(clean(c))

    # ---------
    # dataExist
    # ---------
    def test_dataExists_1(self):
        name = "UT Tower Shooting"
        table = "crises"
        column = "name"
        self.assertTrue(dataExist(name, table, c, column))

    def test_dataExists_2(self):
        name = "Lehman Brothers"
        table = "orgs"
        column = "name"
        self.assertTrue(dataExist(name, table, c, column))
        
    def test_dataExists_3(self):
        name = "Barack Obama"
        table = "people"
        column = "name"
        self.assertTrue(dataExist(name, table, c, column))

    def test_dataExists_4(self):
        name = "Financial Crisis of 2038"
        table = "crises"
        column = "name"
        self.assertFalse(dataExist(name, table, c, column))

    # ---------
    # normTableTracker
    # ---------
    def test_normTableTracker_1(self):
        self.assertTrue(normTableTracker("orgContactInfos", 0, "URL", "ORG_002", c, 0))


print ("TestWCDB.py")
unittest.main()
print ("Done.")
