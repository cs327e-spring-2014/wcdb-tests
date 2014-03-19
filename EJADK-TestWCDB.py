#!/usr/bin/env python3

# -------------------------------
# Copyright (C) 2014
# Eric Poulter, Anthony Oliveri, Derek Perez,
#   Jesse Vo, Jasmine Mann, and Ksenia Kolesnikova
# -------------------------------


# -------
# imports
# -------

import io
import unittest
import xml.etree.ElementTree as ET
from WCDB import wcdb_read, wcdb_write


# -----------
# TestWCDB
# -----------

class TestWCDB (unittest.TestCase) :

    # ----
    # wcdb_read
    # ----

    def test_read_1 (self) :
        reader = io.StringIO("<outer1><inner1></inner1><inner2></inner2></outer1>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<outer1><inner1 /><inner2 /></outer1>")

    def test_read_2 (self) :
        reader = io.StringIO("<a><b><c></c><d></d><e></e></b></a>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<a><b><c /><d /><e /></b></a>")

    def test_read_spacing (self) :
        reader = io.StringIO("<one>   <two>        </two> </one>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<one>   <two>        </two> </one>")

    def test_read_newlines(self):
        reader = io.StringIO("<one>   <two>   \n\n     </two> \n</one>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<one>   <two>   \n\n     </two> \n</one>")

    def test_read_tabs(self):
        reader = io.StringIO("<one>   \t<two>   \t     </two> \n</one>")
        tree = wcdb_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<one>   \t<two>   \t     </two> \n</one>")


    # -----
    # write
    # -----

    def test_write_1 (self) :
        writer = io.StringIO()
        reader = io.StringIO("<outer1><inner1></inner1><inner2></inner2></outer1>")
        tree = wcdb_read(reader)
        wcdb_write(writer, tree)
        self.assertTrue(writer.getvalue() == "<outer1><inner1 /><inner2 /></outer1>")

    def test_write_2 (self) :
        writer = io.StringIO()
        reader = io.StringIO("<a><b><c></c><d></d><e></e></b></a>")
        tree = wcdb_read(reader)
        wcdb_write(writer, tree)
        self.assertTrue(writer.getvalue() == "<a><b><c /><d /><e /></b></a>")

    def test_write_spacing (self) :
        writer = io.StringIO()
        reader = io.StringIO("<one>   <two>        </two> </one>")
        tree = wcdb_read(reader)
        wcdb_write(writer, tree)
        self.assertTrue(writer.getvalue() == "<one>   <two>        </two> </one>")

    def test_write_newlines(self):
        writer = io.StringIO()
        reader = io.StringIO("<one>   <two>   \n\n     </two> \n</one>")
        tree = wcdb_read(reader)
        wcdb_write(writer, tree)
        self.assertTrue(writer.getvalue() == "<one>   <two>   \n\n     </two> \n</one>")

    def test_write_tabs(self):
        writer = io.StringIO()
        reader = io.StringIO("<one>   \t<two>   \t     </two> \n</one>")
        tree = wcdb_read(reader)
        wcdb_write(writer, tree)
        self.assertTrue(writer.getvalue() == "<one>   \t<two>   \t     </two> \n</one>")


# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")