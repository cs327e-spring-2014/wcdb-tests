#!/usr/bin/env python3

"""
To test the program:
% python TestWCDB.py >& TestWCDB.out
% chmod ugo+x TestWCDB.py
% TestWCDB.py >& TestWCDB.out
"""

# -------
# imports
# -------

import io
import unittest
import WCDB

from xml.etree.ElementTree import Element, fromstring, tostring
from WCDB import WCDB_import, WCDB_export, WCDB_solve


# -----------
# TestWCDB
# -----------

class TestWCDB (unittest.TestCase) :

    # ----
    # WCDB_import
    # ----
    
    def test_import_1 (self) :
        nodes = WCDB_import('<xml></xml>')
        self.assertTrue(type(nodes) is Element)

    def test_import_2 (self) :
        nodes = WCDB_import('<crises><crisis>\
            <crisisId>CRI_000</crisisId> \
            <name>Katrina</name>\
            <kind>Natural Disaster</kind>\
            <streetAddress>1234 Broad Street</streetAddress>\
            <city>Austin</city>\
            <stateOrProvince>TX</stateOrProvince>\
            <postalCode>78731</postalCode>\
            <country>USA</country>\
            <dateAndTime>2012-12-13T05:40:00</dateAndTime>\
            <fatalities>1</fatalities>\
            <injuries>3</injuries>\
            <populationIll>5</populationIll>\
            <populationDisplaced>3</populationDisplaced>\
            <environmentalImpact>Oil spill</environmentalImpact>\
            <politicalChanges>Regime changes</politicalChanges>\
            <culturalChanges>Lost generation</culturalChanges>\
            <jobsLost>999</jobsLost>\
            <damageInUSD>999</damageInUSD>\
            <reparationCost>999</reparationCost>\
            <regulatoryChanges>Stricter levy building codes</regulatoryChanges>\
        </crisis></crises>')
        self.assertTrue(type(nodes) is Element)

    def test_import_3(self) :
        nodes = WCDB_import('<xml><xml><xml><xml></xml></xml></xml></xml>')
        self.assertTrue(type(nodes) is Element)
    
    # ----
    # WCDB_export
    # ----
    
    def test_export_1 (self) :
        xml = fromstring('<xml>stuff</xml>')
        string = WCDB_export(xml)
        self.assertTrue(string == '<xml>stuff</xml>')

    def test_export_2 (self) :
        xml = fromstring('<orgPersonPair><orgId>ORG_000</orgId><personId>PER_000</personId></orgPersonPair>')
        string = WCDB_export(xml)
        self.assertTrue(string == '<orgPersonPair><orgId>ORG_000</orgId><personId>PER_000</personId></orgPersonPair>')

    def test_export_3 (self) :
        xml = fromstring('<xml><THU><Team><ACRush><Jelly>morestuff</Jelly></ACRush></Team></THU></xml>')
        string = WCDB_export(xml)
        self.assertTrue(string == '<xml><THU><Team><ACRush><Jelly>morestuff</Jelly></ACRush></Team></THU></xml>')

    # ----
    # WCDB_solve
    # ----

    def test_solve_1 (self) :
        w = io.StringIO()
        r = io.StringIO('<xml><THU><Team><ACRush><Jelly>morestuff</Jelly></ACRush></Team></THU></xml>')
        WCDB_solve(r,w)
        self.assertTrue(w.getvalue() =='<xml><THU><Team><ACRush><Jelly>morestuff</Jelly></ACRush></Team></THU></xml>')
        
    def test_solve_2 (self) :
        w = io.StringIO()
        r = io.StringIO('<orgPersonPair><orgId>ORG_000</orgId><personId>PER_000</personId></orgPersonPair>')
        WCDB_solve(r,w)
        self.assertTrue(w.getvalue() == '<orgPersonPair><orgId>ORG_000</orgId><personId>PER_000</personId></orgPersonPair>')

    def test_solve_3 (self) :       
        w = io.StringIO()
        r = io.StringIO('<xml>stuff</xml>')
        WCDB_solve(r,w)
        self.assertTrue(w.getvalue() == '<xml>stuff</xml>')
        
        
        
# ----
# main
# ----

print("TestWCDB.py")
unittest.main()
print("Done.")
