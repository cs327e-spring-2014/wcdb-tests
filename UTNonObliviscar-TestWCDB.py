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

import StringIO
import unittest
import WCDB

from xml.etree.ElementTree import Element, fromstring, tostring
from WCDB import WCDB_login, WCDB_query, WCDB_create, WCDB_import, WCDB_solve


# -----------
# TestWCDB
# -----------

class TestWCDB (unittest.TestCase) :

    # ----
    # WCDB_login
    # ----

    def test_login_1 (self):
        connection = WCDB_login()
        assert str(type(connection)) == "<class 'MySQLdb.connections.Connection'>"
        
    # ----
    # WCDB_query
    # ----

    def test_query_1 (self):
        c = WCDB_login()
        t = WCDB_query(c,'drop table if exists Test1;')
        t = WCDB_query(c,
        """
create table Test1(
crisisID int unsigned,
personID int unsigned)
;

""")
        self.assertTrue(t == None)    
        
    def test_query_2 (self):
        c = WCDB_login()
        t = WCDB_query(c,'select * from Crises;')
        self.assertTrue(t != None)
        self.assertTrue(type(t) is tuple)

    def test_query_3 (self):
        c = WCDB_login()
        t = WCDB_query(c,'drop table if exists Test3;')
        t = WCDB_query(c,
        """
create table Test3(
orgID int unsigned,
contactInfoID int unsigned)
;

""")
        self.assertTrue(t == None)
        

    def test_query_4 (self):
        c = WCDB_login()
        t = WCDB_query(c,'show databases;')
        self.assertTrue(t != None)
        self.assertTrue(type(t) is tuple)
        
        
    def test_query_5 (self):
        c = WCDB_login()
        t = WCDB_query(c,'show tables;')
        self.assertTrue(t != None)
        self.assertTrue(type(t) is tuple)
     
    # ----
    # WCDB_create
    # ----
    
    def test_create_1(self):
        c = WCDB_login()
        WCDB_create(c)
        t = WCDB_query(c,'select name from Crises;')
        self.assertTrue(t == ())
        
    def test_create_2(self):
        c = WCDB_login()
        WCDB_create(c)
        t = WCDB_query(c,'select * from Orgs;')
        self.assertTrue(t == ())
        
    def test_create_3(self):
        c = WCDB_login()
        WCDB_create(c)
        t = WCDB_query(c,'select * from People;')
        self.assertTrue(t == ())
    
    def test_create_4(self):
        c = WCDB_login()
        WCDB_create(c)
        t = WCDB_query(c,'select * from Resources;')
        self.assertTrue(t == ())
    
    
    # ----
    # WCDB_import
    # ----
    
    def test_import_1 (self) :
        c = WCDB_login()
        nodes = WCDB_import('<xml></xml>',c)
        self.assertTrue(type(nodes) is str)

    def test_import_2 (self) :
        c = WCDB_login()
        nodes = WCDB_import('<root><crises><crisis>\
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
</crisis></crises></root>',c)
        self.assertTrue(type(nodes) is str)
        

    def test_import_3(self) :
        c = WCDB_login()
        nodes = WCDB_import('<xml><xml><xml><xml></xml></xml></xml></xml>',c)
        self.assertTrue(type(nodes) is str)
    
    # ----
    # WCDB_export #can't right tests for this
    # ----

    # ----
    # WCDB_solve
    # ----

    def test_solve_1 (self) :
        w1 = StringIO.StringIO()
        w2 = StringIO.StringIO()
        r1 = StringIO.StringIO(u'<xml><THU><Team><ACRush><Jelly>morestuff</Jelly></ACRush></Team></THU></xml>')
        WCDB_solve(r1,w1)
        r2 = StringIO.StringIO(w1.getvalue())        
        WCDB_solve(r2,w2)
        self.assertTrue(w1.getvalue() == w2.getvalue())
        
    def test_solve_2 (self) :        
        w1 = StringIO.StringIO()
        w2 = StringIO.StringIO()
        r1 = StringIO.StringIO(u'<orgPersonPair><orgId>ORG_000</orgId><personId>PER_000</personId></orgPersonPair>')
        WCDB_solve(r1,w1)
        r2 = StringIO.StringIO(w1.getvalue())        
        WCDB_solve(r2,w2)
        self.assertTrue(w1.getvalue() == w2.getvalue())

    def test_solve_3 (self) :        
        w1 = StringIO.StringIO()
        w2 = StringIO.StringIO()
        r1 = StringIO.StringIO(u'<xml>stuff</xml>')
        WCDB_solve(r1,w1)
        r2 = StringIO.StringIO(w1.getvalue())        
        WCDB_solve(r2,w2)
        self.assertTrue(w1.getvalue() == w2.getvalue())
    
    def test_solve_4 (self) :  
        w1 = StringIO.StringIO()
        w2 = StringIO.StringIO()
        r1 = StringIO.StringIO(u'<team><xml>stuff</xml></team>')
        WCDB_solve(r1,w1)
        r2 = StringIO.StringIO(w1.getvalue())        
        WCDB_solve(r2,w2)
        self.assertTrue(w1.getvalue() == w2.getvalue())
    def test_solve_5 (self) :
        w1 = StringIO.StringIO()
        w2 = StringIO.StringIO()
        r1 = StringIO.StringIO(u'<person><president>obama</president></person>')
        WCDB_solve(r1,w1)
        r2 = StringIO.StringIO(w1.getvalue())        
        WCDB_solve(r2,w2)
        self.assertTrue(w1.getvalue() == w2.getvalue())
    
    
        
                
# ----
# main
# ----

print("TestWCDB.py")
unittest.main()
print("Done.")
