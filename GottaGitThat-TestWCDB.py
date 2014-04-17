# ---------------------------------
# projects/WCDB(phase2)/TestWCDB.py
# Author: Xiaoqin LI
# Date: 04/01/2014
#----------------------------------

"""
To test the program:
python/python2 TestWCDB.py > TestWCDB.out
"""

# -------
# imports
# -------

from StringIO import StringIO
import MySQLdb
import unittest
import sys
import _mysql
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
from WCDB import *

# ----------------------------------
# TestWCDB.py,  unit tests in total
# including some major corner tests 
# ----------------------------------

class TestWCDB(unittest.TestCase):
  # -----------------------------------------------
  # login fuction test 4 in total
  # first one shall be the correct one of us 
  # options:
  # 1 ["z","lxq0906","2ra6bMUV+7","cs327e_lxq0906"]
  # 2 ["z","yj2946","2SU~j.WF7Z","cs327e_yj2946"]
  # 3 ["z","joshen","pb6bKYnCDs","cs327e_joshen"]
  # -----------------------------------------------
  def test_wcdb_login1 (self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen")
    login = wcdb_login(*a)
    self.assertTrue(str(type(login)) == "<type '_mysql.connection'>")

  def test_wcdb_login2 (self):
    a = ("localhost","root","121315","cs327e-wcdb")
    login = wcdb_login(*a)
    self.assertTrue(str(type(login)) != "<type '_mysql.connection'>")
        
  def test_wcdb_login3 (self):
    a = ("localhost","roott","121314","cs327e-wcdb")
    login = wcdb_login(*a)
    self.assertTrue(str(type(login)) != "<type '_mysql.connection'>")
    
  def test_wcdb_login4 (self):
    a = ("localhost","roott","121314","cs327e-wcdbb")
    login = wcdb_login(*a)
    self.assertTrue(str(type(login)) != "<type '_mysql.connection'>")
  
  #---------------------------
  # query function 3 in total
  #---------------------------
  def test_wcdb_query1(self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen") # this should be changed before submittion
    s = "drop table if exists Crises"
    login = wcdb_login(*a)
    t = wcdb_query(login,s)
    self.assertTrue(t == None)

  def test_wcdb_query2(self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen") # this should be changed before submittion
    s = "drop table if exists Crises"
    login = wcdb_login(*a)
    t = wcdb_query(login,s)
    s = """CREATE TABLE Crises (
    crisisId varchar(20) COLLATE utf8_unicode_ci NOT NULL)"""
    login = wcdb_login(*a)
    t = wcdb_query(login,s)
    self.assertTrue(t == None)

  def test_wcdb_query3(self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen") # this should be changed before submittion
    s = """ select *
	from Crises;
	"""
    login = wcdb_login(*a)
    t = wcdb_query(login,s)
    self.assertTrue(t != None)
    
  #----------------------------
  # creatDB function 3 in total
  #----------------------------
  def test_createDB1(self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen") # this should be changed before submittion 
    login_var = wcdb_login(*a)
    createDB(login_var)
    db = MySQLdb.connect(*a) # this should be changed before submittion 
    curs = db.cursor()
    self.assertTrue(curs.execute('SELECT * from Crises') == 0)
    self.assertTrue(type(curs.fetchall()) is tuple)

  def test_createDB2(self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen") # this should be changed before submittion 
    login_var = wcdb_login(*a)
    createDB(login_var)
    db = MySQLdb.connect(*a) # this should be changed before submittion 
    curs = db.cursor()
    self.assertTrue(curs.execute('SELECT * from People') == 0)
    self.assertTrue(type(curs.fetchall()) is tuple)

  def test_createDB3(self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen") # this should be changed before submittion 
    login_var = wcdb_login(*a)
    createDB(login_var)
    db = MySQLdb.connect(*a) # this should be changed before submittion 
    curs = db.cursor()
    self.assertTrue(curs.execute('SELECT * from Orgs') == 0)
    self.assertTrue(type(curs.fetchall()) is tuple)
    
# -----------------------------------------
  # test_wcdb_import fuction test 3 in total
  # -----------------------------------------
  def test_wcdb_import1(self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen") # this should be changed before submittion 
    login_var = wcdb_login(*a)
    createDB(login_var)
    tree = ET.parse(StringIO("<WorldCrisis></WorldCrisis>"))
    wcdb_import(login_var, tree)
    self.assertTrue(len(wcdb_query(login_var, "select * from Crises;")) == 0)

  def test_wcdb_import2(self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen") # this should be changed before submittion 
    login_var = wcdb_login(*a)
    createDB(login_var)
    tree = ET.parse(StringIO("""
                                <root>
                                  <crises>
                                    <crisis>
                                      <crisisId>CRI_001</crisisId>
                                          <name>Chernobyl Accident</name>
                                          <kind>Human Error Disaster</kind>
                                          <streetAddress>NULL</streetAddress>
                                          <city>Chernobyl</city>
                                          <stateOrProvince>NULL</stateOrProvince>
                                          <country>Ukraine</country>
                                          <dateAndTime>1986-04-26T01:23:48</dateAndTime>
                                          <fatalities>290000</fatalities>
                                          <injuries>270000</injuries>
                                          <populationIll>270000</populationIll>
                                          <populationDisplaced>335000</populationDisplaced>
                                          <environmentalImpact>Up to 60 sq. mi. of farmland is likely to remain contaminated for decades</environmentalImpact>
                                          <politicalChanges>Big impact on the fall of the USSR</politicalChanges>
                                          <culturalChanges>NULL</culturalChanges>
                                          <jobsLost>600</jobsLost>
                                          <damageInUSD>0</damageInUSD>
                                          <reparationCost>235000000000</reparationCost>
                                          <regulatoryChanges>Tightening of nuclear power plant safety regulations</regulatoryChanges>
                                    </crisis>
                                  </crises>
                                </root>"""))
    wcdb_import(login_var, tree)
    self.assertTrue(len(wcdb_query(login_var, "select * from Crises;")) == 1)

  def test_wcdb_import3(self):
    a = ("z","joshen","pb6bKYnCDs","cs327e_joshen") # this should be changed before submittion 
    login_var = wcdb_login(*a)
    createDB(login_var)
    tree = ET.parse(StringIO("""
                                <root>
                                  <resources>
                                    <resourcePair>
                                      <resourceId>RES_000</resourceId>
                                      <resource>Food</resource>
                                    </resourcePair>
                                  </resources>
                                </root>"""))
    wcdb_import(login_var, tree)
    self.assertTrue(len(wcdb_query(login_var, "select * from Resources;")) == 1)

  # -----------------------------------------
  # test_tree_builder fuction test 3 in total
  # -----------------------------------------
  def test_tree_builder1(self):
    tag = 'crises'
    content = 'abc'
    root = tree_builder(tag,content)
    self.assertTrue(type(root) is ET.Element)
    self.assertTrue(root.tag == 'crises')
    self.assertTrue(root.text == 'abc')
    
  def test_tree_builder2(self):
    tag = 'crises'
    content = 'abc'
    root = tree_builder(tag,content)
    self.assertTrue(type(root) is ET.Element)
    self.assertTrue(root.tag != 'crisis')
    self.assertTrue(root.text != 'abcd')
    
  def test_tree_builder3(self):
    tag = 'crisis'
    content = 'abcd'
    root = tree_builder(tag,content)
    self.assertTrue(type(root) is ET.Element)
    self.assertTrue(root.tag == 'crisis')
    self.assertTrue(root.text != 'abc')

  # -----------------------------------
  # wcdb_read fuction test 3 in total
  # tested reading tag, text and atttib
  # ----------------------------------- 
  def test_wcdb_read_tag(self):
    r = StringIO("<WorldCrises><apple><bear><clear /><dog /></bear></apple></WorldCrises>")
    root = wcdb_read(r)
    self.assertTrue(root.tag == "WorldCrises")
    self.assertTrue(root[0].tag == "apple")
    self.assertTrue(root[0][0].tag == "bear")
    self.assertTrue(root[0][0][0].tag == "clear")

  def test_wcdb_read_text(self):
    r = StringIO("<root><apple>hey hey<b /><c> </c></apple></root>")
    root = wcdb_read(r)
    self.assertTrue(root[0].text == "hey hey")
    self.assertTrue(root[0][0].text is None)
    self.assertTrue(root[0][1].text == " ")
    self.assertTrue(root.attrib == {})

  def test_wcdb_read_attrib(self):
    r = StringIO("<root><Book ISBN='ISBN-0-13-713526-2' Price='100'><Title ID = 'CS327'>Database</Title></Book></root>")
    root = wcdb_read(r)
    self.assertTrue(root[0].attrib == {'ISBN': 'ISBN-0-13-713526-2', 'Price': '100'})
    self.assertTrue(root[0][0].attrib == {'ID': 'CS327'})
    self.assertTrue(root[0][0].text == "Database")

  # ----------------------------------------------------
  # wcdb_write function test 3 in total
  # tested writing tag, text, atttib and nested elements
  # ----------------------------------------------------

  def test_wcdb_write_single_ele(self):
      w = StringIO()
      a = ET.Element('WorldCrises')
      b = ET.SubElement(a,'apple')
      wcdb_write(w, a)
      self.assertTrue(w.getvalue() =='<?xml version="1.0" ?>\n<WorldCrises>\n\t<apple/>\n</WorldCrises>\n')
      
  def test_wcdb_write_attrib_text(self):
      w = StringIO()
      a = ET.Element('WorldCrises')
      b = ET.SubElement(a,'apple')
      b.text = "hey hey"
      b.attrib = {'aa':'bb','price':'3'}
      wcdb_write(w, a)
      self.assertTrue(w.getvalue() == '<?xml version="1.0" ?>\n<WorldCrises>\n\t<apple aa=\"bb\" price=\"3\">hey hey</apple>\n</WorldCrises>\n')

  def test_wcdb_write_nested_ele(self):
      w = StringIO()
      a = ET.Element('WorldCrises')
      b = ET.SubElement(a, 'apple')
      c = ET.SubElement(b, 'bear')
      d = ET.SubElement(c, 'dog')
      e = ET.SubElement(b, 'clear')
      wcdb_write(w, a)
      self.assertTrue(w.getvalue() == '<?xml version="1.0" ?>\n<WorldCrises>\n\t<apple>\n\t\t<bear>\n\t\t\t<dog/>\n\t\t</bear>\n\t\t<clear/>\n\t</apple>\n</WorldCrises>\n')

  # ----------------------------------------------------
  # wcdb_solve function test 3 in total
  # ----------------------------------------------------
  # a simple test on nested tag
  def test_wcdb_solve_1(self):
      w1 = StringIO()
      w2 = StringIO()
      r = StringIO("<apple><bear><clear /><dog /></bear></apple>")
      wcdb_solve(r, w1)
      r2 = StringIO(w1.getvalue())
      wcdb_solve(r2, w2)
      self.assertTrue(w1.getvalue() == w2.getvalue())
      
  # test on tag, text and white space
  def test_wcdb_solve_2(self):
      w1 = StringIO()
      w2 = StringIO()
      r = StringIO("""
                      <THU>
                            <Team>
                                    <ACRush>clear</ACRush>
                                    <Jelly>dog</Jelly>
                                    <Cooly> \napple  </Cooly>
                            </Team>
                            <JiaJia>clear
                                    <Team> \t clear
                                            <Ahyangyi>  bear  </Ahyangyi>
                                            <Dragon> dog!@#</Dragon>
                                            <Cooly><Amber></Amber></Cooly>
                                    </Team>
                            </JiaJia>
                      </THU>""")
      wcdb_solve(r, w1)
      r2 = StringIO(w1.getvalue())
      wcdb_solve(r2, w2)
      self.assertTrue(w1.getvalue() == w2.getvalue())
      
  # adding attributes
  def test_wcdb_solve_3(self):
      w1 = StringIO()
      w2 = StringIO()
      r = StringIO("""
                      <Bookstore>
                           <Book ISBN="ISBN-0-13-713526-2" Price="100">
                              <Title>A First Course in Database Systems</Title>
                              <Authors>
                                 <Auth authIdent="JU" />
                                 <Auth authIdent="JW" />
                              </Authors>
                           </Book>
                           <Book ISBN="ISBN-0-13-815504-6" Price="85">
                              <Title>Database Systems: The Complete Book</Title>
                              <Authors>
                                 <Auth authIdent="HG" />
                                 <Auth authIdent="JU" />
                                 <Auth authIdent="JW" />
                              </Authors>
                              <Remark>
                                Amazon.com says: Buy this book bundled with
                                <BookRef book="ISBN-0-13-713526-2" /> - a great deal!
                              </Remark>
                           </Book>
                           <Author Ident="HG">
                              <First_Name>Hector</First_Name>
                              <Last_Name>Garcia-Molina</Last_Name>
                           </Author>
                           <Author Ident="JU">
                              <First_Name>Jeffrey</First_Name>
                              <Last_Name>Ullman</Last_Name>
                           </Author>
                           <Author Ident="JW">
                              <First_Name>Jennifer</First_Name>
                              <Last_Name>Widom</Last_Name>
                           </Author>
                      </Bookstore>""")
      wcdb_solve(r, w1)
      r2 = StringIO(w1.getvalue())
      wcdb_solve(r2, w2)
      self.assertTrue(w1.getvalue() == w2.getvalue())
# ----------------------------------------------------
# wcdb_solve function test 3 in total
# ----------------------------------------------------

  def test_wcdb_export1(self):
      a = ("z","joshen","pb6bKYnCDs","cs327e_joshen")
      login_var = wcdb_login(*a)
      createDB(login_var)

      r = """<root>
    <crises>
        <crisis>
            <crisisId>CRI_001</crisisId>
            <name>Chernobyl Accident</name>
            <kind>Human Error Disaster</kind>
            <streetAddress>NULL</streetAddress>
            <city>Chernobyl</city>
            <stateOrProvince>NULL</stateOrProvince>
            <country>Ukraine</country>
            <dateAndTime>1986-04-26T01:23:48</dateAndTime>
            <fatalities>290000</fatalities>
            <injuries>270000</injuries>
			<populationIll>270000</populationIll>
			<populationDisplaced>335000</populationDisplaced>
            <environmentalImpact>Up to 60 sq. mi. of farmland is likely to remain contaminated for decades</environmentalImpact>
			<politicalChanges>Big impact on the fall of the USSR</politicalChanges>
			<culturalChanges>NULL</culturalChanges>
			<jobsLost>600</jobsLost>
			<damageInUSD>0</damageInUSD>
			<reparationCost>235000000000</reparationCost>
            <regulatoryChanges>Tightening of nuclear power plant safety regulations</regulatoryChanges>
        </crisis></crises></root>"""
		
      a = ET.fromstring(r) 
      wcdb_import(login_var, a)
	  
      root = wcdb_export(login_var)
      self.assertTrue(len(root[0][0]) == 19)
      
  def test_wcdb_export2(self):
      a = ("z","joshen","pb6bKYnCDs","cs327e_joshen")
      login_var = wcdb_login(*a)
      createDB(login_var)

      r = """<root><orgs><org>
            <orgId>ORG_001</orgId>
            <name>International Nuclear Safety Group (INSAG)</name>
            <kind>Intergovernmental Agency</kind>
            <streetAddress>Vienna International Center, PO Box 100, 1400</streetAddress>
            <city>Vienna</city>
            <stateOrProvince>Null</stateOrProvince>
            <postalCode>NULL</postalCode>
            <country>Austria</country>
            <foundingMission>The group was founded in 1985 by the International Atomic Energy Agency (IAEA)as an advisory committee in the area of nuclear safety.</foundingMission>
            <dateFounded>1985-01-01</dateFounded>
            <majorEvents>First investigation was the Chernobyl Accident</majorEvents>
        </org></orgs></root>"""
		
      a = ET.fromstring(r) 
      wcdb_import(login_var, a)
	  
      root = wcdb_export(login_var)
      self.assertTrue(len(root[1][0]) == 11)
      
  def test_wcdb_export3(self):
      a = ("z","joshen","pb6bKYnCDs","cs327e_joshen")
      login_var = wcdb_login(*a)
      createDB(login_var)

      r = """<root><people><person>
            <personId>PER_004</personId>
            <name>Michele Pierre Louis</name>
            <kind>President</kind>
            <streetAddress>NULL</streetAddress>
            <city>Jeremie</city>
            <stateOrProvince>NULL</stateOrProvince>
            <postalCode>NULL</postalCode>
            <country>Haiti</country>
        </person></people></root>"""
		
      a = ET.fromstring(r) 
      wcdb_import(login_var, a)
	  
      root = wcdb_export(login_var)
      self.assertTrue(len(root[2][0]) == 8)


print("TestWCDB.py")
print("Done.")
unittest.main()



