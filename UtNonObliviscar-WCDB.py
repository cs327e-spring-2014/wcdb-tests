#!/usr/bin/env python

from xml.etree.ElementTree import fromstring, tostring, Element


def WCDB_import(nodes):
    """
Import takes in a string containing an XML document and
returns an xml Element Tree element to be put into SQL
"""
    xml = fromstring(nodes)
    assert(type(xml) is Element)
    return xml

def WCDB_export(xml):
    """
Export takes and xml element and calls tosting, forming it
into an xml document and returns the xml string
"""
    string = str(tostring(xml),'UTF-8')
    return string


def WCDB_solve(r,w):
    """
Solve is a helper function that calls import and export
to manipulate xml documents. r is a reader and w is a writer
Later this will be the main driver of the WCDB code
"""
    nodes = r.read()
    xml = WCDB_import(nodes)
    string = WCDB_export(xml)
    w.write(string)
