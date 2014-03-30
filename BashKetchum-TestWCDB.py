#!/usr/bin/env python

from xml.etree.ElementTree import Element, fromstring, ParseError
from WCDB import importXML, exportXML
import unittest
import StringIO


# Class defining various unit tests
class XMLUnitTests(unittest.TestCase):
    # Testing of importXML
    def test_importXML1(self):
        try:
            rootElement = importXML(StringIO.StringIO("<red><green><blue>Hello</blue><yellow>Goodbye</yellow></green></red>"))
        except ParseError:
            self.fail("importXML1 failed to parse")
        else:
            self.assert_(type(rootElement) == Element)

    def test_importXML2(self):
        try:
            rootElement = importXML(StringIO.StringIO("<Team><ACRush>Hello</ACRush><Jelly>Goodbye</Jelly><Cooly>Bonjour</Cooly></Team>"))
        except ParseError:
            self.fail("importXML2 failed to parse")
        else:
            self.assert_(type(rootElement) == Element)

    def test_importXML3(self):
        try:
            rootElement = importXML(StringIO.StringIO("<THU><Team><ACRush>Hello</ACRush><Jelly>Godlike</Jelly><Cooly>Massacre</Cooly></Team><JiaJia><Team><Ahyangyi>Vengeful</Ahyangyi><Dragon>Flamboyant</Dragon><Cooly><Amber>Jessie</Amber></Cooly></Team></JiaJia></THU>"))
        except ParseError:
            self.fail("importXML3 failed to parse")
        else:
            self.assert_(type(rootElement) == Element)

    # Testing of exportXML
    def test_exportXML1(self):
        startElement = fromstring("<red><green><blue>Hello</blue><yellow>Goodbye</yellow></green></red>")
        writer = StringIO.StringIO("")
        exportXML(startElement, writer)
        self.assert_(writer.getvalue() == "<red><green><blue>Hello</blue><yellow>Goodbye</yellow></green></red>")

    def test_exportXML2(self):
        startElement = fromstring("<Team><ACRush>Hello</ACRush><Jelly>Goodbye</Jelly><Cooly>Bonjour</Cooly></Team>")
        writer = StringIO.StringIO("")
        exportXML(startElement, writer)
        self.assert_(writer.getvalue() == "<Team><ACRush>Hello</ACRush><Jelly>Goodbye</Jelly><Cooly>Bonjour</Cooly></Team>")

    def test_exportXML3(self):
        startElement = fromstring("<THU><Team><ACRush>Hello</ACRush><Jelly>Godlike</Jelly><Cooly>Massacre</Cooly></Team><JiaJia><Team><Ahyangyi>Vengeful</Ahyangyi><Dragon>Flamboyant</Dragon><Cooly><Amber>Jessie</Amber></Cooly></Team></JiaJia></THU>")
        writer = StringIO.StringIO("")
        exportXML(startElement, writer)
        self.assert_(writer.getvalue() == "<THU><Team><ACRush>Hello</ACRush><Jelly>Godlike</Jelly><Cooly>Massacre</Cooly></Team><JiaJia><Team><Ahyangyi>Vengeful</Ahyangyi><Dragon>Flamboyant</Dragon><Cooly><Amber>Jessie</Amber></Cooly></Team></JiaJia></THU>")


# Call the test
unittest.main()
