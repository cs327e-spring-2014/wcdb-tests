#!/usr/bin/env python

# -------------------------------
# Copyright (C) 2014
# Eric Poulter, Anthony Oliveri, Derek Perez,
#   Jesse Vo, Jasmine Mann, and Ksenia Kolesnikova
# -------------------------------


# -------
# imports
# -------


import StringIO
import unittest
import xml.etree.ElementTree as ET
from WCDB import wcdb_read, wcdb_login_mysql, query, wcdb_importToMySQL, wcdb_exportToXML


# -----------
# TestWCDB
# -----------

class TestWCDB (unittest.TestCase) :


    # ------------
    # wcdb_login_mysql
    # ------------

    def test_login(self) :
        connection = wcdb_login_mysql("cs327e_awo84")
        self.assertTrue(str(type(connection)) == "<type '_mysql.connection'>")


    # ----
    # wcdb_read
    # ----

    def test_read_1 (self) :
        reader = StringIO.StringIO("<outer1><inner1></inner1><inner2></inner2></outer1>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree)
        self.assertTrue(treeStr == "<outer1><inner1 /><inner2 /></outer1>")

    def test_read_2 (self) :
        reader = StringIO.StringIO("<a><b><c></c><d></d><e></e></b></a>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree)
        self.assertTrue(treeStr == "<a><b><c /><d /><e /></b></a>")

    def test_read_spacing (self) :
        reader = StringIO.StringIO("<one>   <two>        </two> </one>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree)
        self.assertTrue(treeStr == "<one>   <two>        </two> </one>")

    def test_read_newlines(self):
        reader = StringIO.StringIO("<one>   <two>   \n\n     </two> \n</one>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree)
        self.assertTrue(treeStr == "<one>   <two>   \n\n     </two> \n</one>")

    def test_read_tabs(self):
        reader = StringIO.StringIO("<one>   \t<two>   \t     </two> \n</one>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree)
        self.assertTrue(treeStr == "<one>   \t<two>   \t     </two> \n</one>")

    def test_read_3 (self):
        reader = StringIO.StringIO("<W><C><D><B></B></D></C></W>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree)
        self.assertTrue(treeStr == "<W><C><D><B /></D></C></W>")

    def test_read_4 (self):
        reader = StringIO.StringIO("<Mathematics><Physics><Chemistry></Chemistry></Physics></Mathematics>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree)
        self.assertTrue(treeStr == "<Mathematics><Physics><Chemistry /></Physics></Mathematics>")

    def test_read_5 (self):
        reader = StringIO.StringIO("<Herp><Derp></Derp></Herp>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree)
        self.assertTrue(treeStr == "<Herp><Derp /></Herp>")
    
    # --------
    # Query.py
    # --------

    def test_query_show(self):
        connection = wcdb_login_mysql("cs327e_awo84")
        t = query(connection, "show databases;")
        self.assertTrue(str(t) == "(('information_schema',), ('cs327e_awo84',), ('cs329e_awo84',), ('cs329e_overflow',))")

    def test_query_select(self):
        connection = wcdb_login_mysql("cs327e_awo84")
        t = query(connection, "select crisisId from crises;")
        self.assertTrue(str(t) == "(('0',), ('1',), ('2',), ('3',), ('4',), ('5',), ('6',), ('7',), ('8',), ('9',))")

    def test_query_drop(self):
        connection = wcdb_login_mysql("cs327e_awo84")
        query(connection, "use cs329e_awo84;")
        t = query(connection, "drop table if exists testwcdb;")
        self.assertTrue

    def test_query_create(self):
        connection = wcdb_login_mysql("cs327e_awo84")
        query(connection, "use cs329e_awo84;")
        query(connection, "drop table if exists testwcdb;")
        t = query(connection, "create table testwcdb (one int);")
        self.assertTrue(t is None)
        query(connection, "drop table if exists testwcdb;")

    # ------------
    # wcdb_exportToXML
    # ------------
    
    def test_export(self):
        connection = wcdb_login_mysql("cs329e_overflow")
        query(connection, "use cs329e_overflow;")
        connection.close()
        allTableNames = ["test_import_1"]
        allRowNames = ["col1", "col2"]
        self.assertTrue(wcdb_exportToXML(allTableNames, allRowNames, "cs329e_overflow") == True )


    # ------------
    # wcdb_importToMySQL
    # ------------

    def test_import(self):
        connection = wcdb_login_mysql("cs329e_overflow")
        query(connection, "use cs329e_overflow;")
        query(connection, "drop table if exists test_import_1;")
        query(connection, "create table test_import_1 (col1 varchar(10), col2 varchar(10))  ;")
        reader = StringIO.StringIO("<outer1><inner1></inner1><inner2></inner2></outer1>")
        self.assertTrue(wcdb_importToMySQL(reader, "cs327e_awo84"))

# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
