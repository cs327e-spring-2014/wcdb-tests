#!/usr/bin/env python3

"""
To test the program:
    % python3 TestWCDB.py > TestWCDB.out
    % chmod ugo+x TestWCDB.py
    % TestWCDB.py > TestWCDB.out
"""

#---------
#imports
#---------

import io
import unittest

import mysql.connector

from xml.etree.ElementTree import Element, fromstring, tostring

from WCDB import wcdb_read, wcdb_solve, wcdb_print, wcdb_element, wcdb_create_tables, wcdb_insert, wcdb_import, wcdb_export, wcdb_login


#----------
#TestWCDB
#----------

class TestWCDB (unittest.TestCase) :
  
  #-----
  #login
  #-----
  def test_login (self):
    c = wcdb_login()
    self.assertTrue(type(c)  == mysql.connector.connection.MySQLConnection)
	
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
    r = io.StringIO("<Cookies>\n\t<Thin Mints></Thin Mints>\n\t<Samoas></Samoas>\n</Cookies>")
    a = ['']
    b = wcdb_read (r,a)
    self.assertTrue(b == True)
    self.assertTrue(a[0] == "<Cookies><Thin Mints></Thin Mints><Samoas></Samoas></Cookies>")

  def test_read_3 (self) :
    r = io.StringIO("<Dates><Nineties>\t\t</Nineties><Eighties>\t</Eighties></Dates>")
    a = ['']
    b = wcdb_read (r,a)
    self.assertTrue(b == True)
    self.assertTrue(a[0] == "<Dates><Nineties></Nineties><Eighties></Eighties></Dates>")

  def test_read_4 (self) :
    r = io.StringIO("<one>\t\t\t<two>\n\t\t</two></one>")
    a = ['']
    b = wcdb_read (r,a)
    self.assertTrue(b == True)
    self.assertTrue(a[0] == "<one><two></two></one>")

  def test_read_5 (self) :
    r = io.StringIO("\t<one>\t\t</one>\n")
    a = ['']
    b = wcdb_read (r,a)
    self.assertTrue(b == True)
    self.assertTrue(a[0] == '<one></one>')

  def test_read_6 (self) :
    r = io.StringIO("<one></one>")
    a = ['']
    b = wcdb_read (r,a)
    self.assertTrue(b == True)
    self.assertTrue(a[0] == '<one></one>')

  #------
  #element
  #------

  def test_element (self) :
    a = ['<one><two>three</two></one>']
    b = wcdb_element(a)
    self.assertTrue(b.tag == 'one')

  def test_element_2 (self) :
    a = ['<kinderder></kinderder>']
    b = wcdb_element(a)
    self.assertTrue(b.tag == 'kinderder')

  def test_element_3 (self) :
    a = ['<six><two><three></three></two></six>']
    b = wcdb_element(a)
    self.assertTrue(b.tag == 'six')

  def test_element_4 (self) :
    a = ['<one></one>']
    b = wcdb_element(a)
    self.assertTrue(b.tag == 'one')
    
  #-------------
  #create_tables
  #-------------
  def test_create_tables (self):
    wcdb_create_tables()
    c = wcdb_login()
    cur = c.cursor(buffered = True)
    cur.execute("show tables")
    b = cur.fetchall()
    #print(b)
		

  #-------
  #insert
  #-------
  def test_insert (self):
    c = wcdb_login()
    cur = c.cursor(buffered = True)
    cur.execute("DELETE from crises")
    wcdb_insert('crises',"crisisId","'CRI_001'")
    c = wcdb_login()
    cur = c.cursor(buffered = True)
    cur.execute("select * from crises")
    b = cur.fetchall()
    self.assertTrue(b == [('CRI_001', '', 'Natural Disaster', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)])
                
  def test_insert_2 (self):
    c = wcdb_login()
    cur = c.cursor(buffered = True)            
    cur.execute("DELETE from crises")
    wcdb_insert('crises',"crisisId,kind","'CRI_001','Natural Disaster'")           
    cur.execute("select * from crises")
    b = cur.fetchall()
    self.assertTrue(b == [('CRI_001', '', 'Natural Disaster', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)])
                

  def test_insert_3 (self):
    c = wcdb_login()
    cur = c.cursor(buffered = True)
    cur.execute("DELETE from crises")
    wcdb_insert('crises',"crisisId","'CRI_705'")
    cur.execute("select * from crises")
    b = cur.fetchall()
    self.assertTrue(b == [('CRI_705', '', 'Natural Disaster', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)])

  def test_insert_4 (self):
    c = wcdb_login()
    cur = c.cursor(buffered = True)
    cur.execute("DELETE from crises")
    wcdb_insert('crises',"crisisId,kind","'CRI_55','Act of Terrorism'")
    cur.execute("select * from crises")
    b = cur.fetchall()
    self.assertTrue(b == [('CRI_55', '', 'Act of Terrorism', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)])

  def test_insert_5 (self):
    c = wcdb_login()
    cur = c.cursor(buffered = True)
    cur.execute("DELETE from crises")
    wcdb_insert('crises',"crisisId,kind,name","'CRI_90','Act of Terrorism', 'Bill'")
    cur.execute("select * from crises")
    b = cur.fetchall()
    self.assertTrue(b == [('CRI_90', 'Bill', 'Act of Terrorism', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)])            

  #------
  #import
  #------
	
  def test_import (self):
    a = ("<root><crises><crisis><crisisId>WHAT</crisisId></crisis></crises></root>")
    b = fromstring(a)
    c, d = wcdb_import(b)
    self.assertTrue(c == "crisisId")
    self.assertTrue(d == "'WHAT'")
    
    
	
  def test_import_2 (self):
    a = ("<root><crises><crisis><kind>Natural Disaster</kind></crisis></crises></root>")
    b = fromstring(a)
    c, d = wcdb_import(b)
    self.assertTrue(c == "kind")
    self.assertTrue(d == "'Natural Disaster'")
	
  def test_import_3 (self):
    a = ("<root><crises><crisis><crisisId>0</crisisId></crisis></crises></root>")
    b = fromstring(a)
    c, d = wcdb_import(b)
    self.assertTrue(c == "crisisId")
    self.assertTrue(d == "'0'")
		
  #------
  #export
  #------
	
  def test_export (self):
    a = wcdb_export()
    self.assertTrue(a.tag == 'root')
    self.assertTrue(type(a) == Element)
	
  #-----
  #print
  #-----

  def test_print (self):
    w = io.StringIO()
    root = fromstring('<one><two>three</two></one>')
    wcdb_print(w, root)
    a=(w.getvalue())
    self.assertTrue(w.getvalue() == '<one>\n\t<two>three</two>\n</one>\n\n')
  
  def test_print_2 (self):
    w = io.StringIO()
    root = fromstring('<one></one>')
    wcdb_print(w, root)
    self.assertTrue(w.getvalue() == '<one/>\n\n')

  def test_print_3 (self):
    w = io.StringIO()
    root = fromstring('<one><two><three>six</three></two></one>')
    wcdb_print(w, root)
    self.assertTrue(w.getvalue() == '<one>\n\t<two>\n\t\t<three>six</three>\n\t</two>\n</one>\n\n')

  def test_print_4 (self):
    w = io.StringIO()
    root = fromstring('<one><two><three><four></four></three></two></one>')
    wcdb_print(w, root)
    self.assertTrue(w.getvalue() == '<one>\n\t<two>\n\t\t<three>\n\t\t\t<four/>\n\t\t</three>\n\t</two>\n</one>\n\n')

  def test_print_5 (self):
    w = io.StringIO()
    root = fromstring('<one><two></two><three></three><four><five></five></four></one>')
    wcdb_print(w, root)
    self.assertTrue(w.getvalue() == '<one>\n\t<two/>\n\t<three/>\n\t<four>\n\t\t<five/>\n\t</four>\n</one>\n\n')
                    
  def test_print_6 (self) :
    w = io.StringIO()
    root = fromstring('<one><two>yes</two><three>yes</three><four>yes</four></one>')
    wcdb_print(w,root)
    self.assertTrue(w.getvalue() == "<one>\n\t<two>yes</two>\n\t<three>yes</three>\n\t<four>yes</four>\n</one>\n\n")

  #-----
  #solve
  #-----

  def test_solve (self) :
    r = io.StringIO('''<root>
        <citations/>
        <crises>
                <crisis>
                        <crisisId>Natural Disaster</crisisId>
                        <name>None</name>
                        <kind>None</kind>
                        <streetAddress>None</streetAddress>
                        <city>None</city>
                        <stateOrProvince>None</stateOrProvince>
                        <postalCode>None</postalCode>
                        <country>None</country>
                        <dateAndTime>None</dateAndTime>
                        <fatalities>None</fatalities>
                        <injuries>None</injuries>
                        <populationIll>None</populationIll>
                        <populationInjured>None</populationInjured>
                        <populationDisplaced>None</populationDisplaced>
                        <environmentalImpact>None</environmentalImpact>
                        <politicalChanges>None</politicalChanges>
                        <culturalChanges>None</culturalChanges>
                        <jobsLost>None</jobsLost>
                        <damageInUSD>None</damageInUSD>
                </crisis>
        </crises>
        <crisisCitations/>
        <crisisOrgs/>
        <crisisPeople/>
        <crisisResources/>
        <crisisUrls/>
        <crisisWaysToHelp/>
        <orgCitations/>
        <orgPeople/>
        <orgUrls/>
        <orgs/>
        <people/>
        <personCitations/>
        <personUrls/>
        <resources/>
        <urls/>
        <waysToHelp/>
</root>''')
    w = io.StringIO()
    wcdb_solve(r,w)
    self.assertTrue(w.getvalue() == ('''<root>
	<citations/>
	<contactInfos/>
	<crises>
		<crisis>
			<citation>Natural</citation>
			<citationId>NULL</citationId>
			<contactInfoId/>
			<crisisId>NULL</crisisId>
			<name>NULL</name>
			<kind>NULL</kind>
			<streetAddress>0</streetAddress>
			<city>NULL</city>
			<stateOrProvince>NULL</stateOrProvince>
			<postalCode>0</postalCode>
			<country>0</country>
			<dateAndTime>0</dateAndTime>
			<fatalities>0</fatalities>
			<injuries>0</injuries>
			<populationIll>NULL</populationIll>
			<populationInjured>NULL</populationInjured>
			<populationDisplaced>NULL</populationDisplaced>
			<environmentalImpact>0</environmentalImpact>
			<politicalChanges>0</politicalChanges>
			<culturalChanges>None</culturalChanges>
			<jobsLost>None</jobsLost>
		</crisis>
	</crises>
	<crisisCitations/>
	<crisisOrgs/>
	<crisisPeople/>
	<crisisResources/>
	<crisisUrls/>
	<crisisWaysToHelp/>
	<orgCitations/>
	<orgContactInfos/>
	<orgPeople/>
	<orgUrls/>
	<orgs/>
	<people/>
	<personCitations/>
	<personUrls/>
	<resources/>
	<urls/>
	<waysToHelp/>
</root>

'''))

print('TestWCDB.py')
unittest.main(warnings='ignore')
print('Done.')


