#!/usr/bin/env python3

# -----------
# TestWCDB.py
# Brigadeiros
# -----------

'''
Testing this program :
 % python3 TestWCDB.py >& TestWCDB.out
'''

# -------
# imports
# -------

import io
import unittest

from WCDB import importXML, exportXML, query, login, create, escapeStrings, importToSQL, create_xml
from xml.etree.ElementTree import Element, fromstring, tostring, tostringlist

# --------
# TestWCDB
# --------

class TestWCDB (unittest.TestCase) :
	# ---------
	# importXML
	# ---------

	def test_importXML_1 (self):
		xml = io.StringIO (unicode('<?xml version="1.0" encoding="utf-8"?><root><crises>Barrack Obama</crises></root>'))
		out = importXML (xml) 
		self.assertTrue(type(out) is Element)

	def test_importXML_2 (self):
		xml = io.StringIO (unicode('<?xml version="1.0" encoding="utf-8"?><root> </root>'))
		out = importXML (xml)
		self.assertTrue(type(out) is Element)
	
	def test_importXML_3 (self):
		xml = io.StringIO (unicode('<?xml version="1.0" encoding="utf-8"?><root><crises><crisis>1</crisis></crises></root>'))
		out = importXML (xml) 
		self.assertTrue(type(out) is Element)
 	
	# ---------
	# exportXML
	# --------
	'''
	!!!!!!!!
	These functions can't be tested!!!

	'''
# ----
# query
# ----	
        def test_query_1(self):
                c = login()
                t = query(c, "show Databases;")
                self.assertTrue(str(type(t)) == "<type 'tuple'>")
        def test_query_2(self):
                c = login()
                create(c)
                t = query(c, "show tables;")
                self.assertTrue(str(type(t)) == "<type 'tuple'>")
        def test_query_3(self):
                c = login()
                create(c)
                t = query(c, "select * from crises;")
                self.assertTrue(str(type(t)) == "<type 'tuple'>")
	
	
# ----
# login
# ---

	def test_login_1(self):
		h = "z"
		u = "abatista"
		p = "TCgfNXdb.p"
		d =  "cs327e_abatista" 
		out=login(h, u, p, d)
		self.assertTrue(str(type(out)) == "<type '_mysql.connection'>")
		
	def test_login_2(self):
		h = "z"
		u = "ofac90"
		p = "MMVAIRmfJ6"
		d = "cs327e_ofac90"
		out=login(h, u, p, d)
		self.assertTrue(str(type(out)) == "<type '_mysql.connection'>")
		
	def test_login_3(self):
		h = "z"
		u = "lucascf"
		p = "Lrk9S1IA91"
		d = "cs327e_lucascf"
		out=login(h, u, p, d)
		self.assertTrue(str(type(out)) == "<type '_mysql.connection'>")

		
	# ----
	# create
	# ----

	def test_create_1(self):
		h= "z"
		u = "abatista"
		p = "TCgfNXdb.p"
		d = "cs327e_abatista"
		c=login(h, u, p, d)
		create(c)
		t = query(
		c, 
		"select * from crises")
		self.assertFalse(t is None)
		
	def test_create_2(self):
		h= "z"
		u = "abatista"
		p = "TCgfNXdb.p"
		d = "cs327e_abatista"
		c = login(h, u, p, d)
		create(c)
		t = query(
		c, 
		"select * from orgs")
		self.assertFalse(t is None)
		
	def test_create_3(self):
		h= "z"
		u = "abatista"
		p = "TCgfNXdb.p"
		d = "cs327e_abatista"
		c = login(h, u, p, d)
		create(c)
		t = query(
		c, 
		"select * from people")
		self.assertFalse(t is None)
		
	 
	# ----
	# escapeStrings
	# ----

	def test_escapeStrings_1(self):
			myStr = "pork's foot" 
			out=escapeStrings(myStr)
			self.assertTrue(out == "pork''s foot")

	def test_escapeStrings_2(self):
		myStr = "Lucas' sunglasses"
		out = escapeStrings(myStr)
		self.assertTrue(out == "Lucas'' sunglasses")

	def test_escapeStrings_3(self): 
		 myStr = "Today's menu"
		 out = escapeStrings(myStr)
		 self.assertTrue(out == "Today''s menu")
		 
	# ----
	# importToSQL
	# ----
	def test_importToSql_1(self):
		string="""<root><crises>
        <crisis>
            <crisisId>CRI_000</crisisId>
            <name>Great Depression in US</name>
			<kind>Human Error Disaster</kind>
            <streetAddress></streetAddress>
            <city></city>
            <stateOrProvince></stateOrProvince>
            <postalCode></postalCode>
            <country>USA</country>
            <dateAndTime>1929-10-29T00:00:00</dateAndTime>
            <fatalities>40000</fatalities>
            <injuries>0</injuries>
            <populationIll>0</populationIll>
            <populationDisplaced>200000</populationDisplaced>
            <environmentalImpact></environmentalImpact>
            <politicalChanges>New Deal, Increased Size of Government, creation of the Securities and Exchange Commission (SEC) and the Federal Deposit Insurance Corporation (FDIC)</politicalChanges>
            <culturalChanges>Generaton that lived through the Great Depression stayed frugal, wary of banks, and suspicious of the stock market</culturalChanges>
            <jobsLost>11000000</jobsLost>
            <damageInUSD>0</damageInUSD>
            <reparationCost>160000000</reparationCost>
            <regulatoryChanges>Strict trading and banking regulations</regulatoryChanges>
        </crisis>
	</crises></root>"""

		inputstr = fromstring(string)
		c = login()
		create(c)
                importToSQL(inputstr)
		t = query(
		c, 
		"select crisisID from crises where crisisID=0;")
		self.assertTrue(int(t[0][0]) == 0)

	def test_importToSql_2(self):
		string="""<root><crises>
        <crisis>
            <crisisId>CRI_001</crisisId>
            <name>Great Depression in US</name>
			<kind>Human Error Disaster</kind>
            <streetAddress></streetAddress>
            <city></city>
            <stateOrProvince></stateOrProvince>
            <postalCode></postalCode>
            <country>USA</country>
            <dateAndTime>1929-10-29T00:00:00</dateAndTime>
            <fatalities>40000</fatalities>
            <injuries>0</injuries>
            <populationIll>0</populationIll>
            <populationDisplaced>200000</populationDisplaced>
            <environmentalImpact></environmentalImpact>
            <politicalChanges>New Deal, Increased Size of Government, creation of the Securities and Exchange Commission (SEC) and the Federal Deposit Insurance Corporation (FDIC)</politicalChanges>
            <culturalChanges>Generaton that lived through the Great Depression stayed frugal, wary of banks, and suspicious of the stock market</culturalChanges>
            <jobsLost>11000000</jobsLost>
            <damageInUSD>0</damageInUSD>
            <reparationCost>160000000</reparationCost>
            <regulatoryChanges>Strict trading and banking regulations</regulatoryChanges>
        </crisis>
	</crises></root>"""

		inputstr = fromstring(string)
		c = login()
		create(c)
	        importToSQL(inputstr)
		t = query(
		c, 
		"select fatalities from crises where fatalities=40000;")
		self.assertTrue(int(t[0][0]) == 40000)

	def test_importToSql_3(self):
		string="""<root><crises>
        <crisis>
            <crisisId>CRI_003</crisisId>
            <name>Great Depression in US</name>
			<kind>Human Error Disaster</kind>
            <streetAddress></streetAddress>
            <city></city>
            <stateOrProvince></stateOrProvince>
            <postalCode></postalCode>
            <country>USA</country>
            <dateAndTime>1929-10-29T00:00:00</dateAndTime>
            <fatalities>40000</fatalities>
            <injuries>0</injuries>
            <populationIll>0</populationIll>
            <populationDisplaced>200000</populationDisplaced>
            <environmentalImpact></environmentalImpact>
            <politicalChanges>New Deal, Increased Size of Government, creation of the Securities and Exchange Commission (SEC) and the Federal Deposit Insurance Corporation (FDIC)</politicalChanges>
            <culturalChanges>Generaton that lived through the Great Depression stayed frugal, wary of banks, and suspicious of the stock market</culturalChanges>
            <jobsLost>11000000</jobsLost>
            <damageInUSD>0</damageInUSD>
            <reparationCost>160000000</reparationCost>
            <regulatoryChanges>Strict trading and banking regulations</regulatoryChanges>
        </crisis>
	</crises></root>"""

		inputstr = fromstring(string)
		c = login()
		create(c)
	        importToSQL(inputstr)
		t = query(
		c, 
		"select country from crises where country='USA';")
		self.assertTrue(str(t[0][0]) == str('USA'))
	# ----
	# main
	# ----

print("TestWCDB.py")
unittest.main()
print("Done.")
