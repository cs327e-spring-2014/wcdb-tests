#!/usr/bin/env python

from xml.etree.ElementTree import fromstring
import unittest
from StringIO import StringIO
import _mysql

from WCDB import getElement, importXML, exportXML


def truncateAllTables(dbConnection):
    dbConnection.query("SET FOREIGN_KEY_CHECKS=0")
    dbConnection.query("TRUNCATE TABLE ContactInfos")
    dbConnection.query("TRUNCATE TABLE Citations")
    dbConnection.query("TRUNCATE TABLE Crises")
    dbConnection.query("TRUNCATE TABLE CrisisCitations")
    dbConnection.query("TRUNCATE TABLE CrisisOrgs")
    dbConnection.query("TRUNCATE TABLE CrisisPeople")
    dbConnection.query("TRUNCATE TABLE CrisisResources")
    dbConnection.query("TRUNCATE TABLE CrisisUrls")
    dbConnection.query("TRUNCATE TABLE CrisisWaysToHelp")
    dbConnection.query("TRUNCATE TABLE OrgCitations")
    dbConnection.query("TRUNCATE TABLE OrgContactInfos")
    dbConnection.query("TRUNCATE TABLE OrgPeople")
    dbConnection.query("TRUNCATE TABLE OrgUrls")
    dbConnection.query("TRUNCATE TABLE Orgs")
    dbConnection.query("TRUNCATE TABLE OrgUrls")
    dbConnection.query("TRUNCATE TABLE People")
    dbConnection.query("TRUNCATE TABLE PersonCitations")
    dbConnection.query("TRUNCATE TABLE PersonUrls")
    dbConnection.query("TRUNCATE TABLE Resources")
    dbConnection.query("TRUNCATE TABLE Urls")
    dbConnection.query("TRUNCATE TABLE WaysToHelp")
    dbConnection.query("SET FOREIGN_KEY_CHECKS=1")


# Class defining various unit tests
class XMLUnitTests(unittest.TestCase):
    # Testing of getElement
    def test_getElement1(self):
        row = fromstring("<crisis>\
                          <crisisId>CRI_001</crisisId>\
                          <name>Katrina</name>\
                          <kind>Natural Disaster</kind>\
                          <streetAddress />\
                          <city>New Orleans</city>\
                          <stateOrProvince>Louisiana</stateOrProvince>\
                          <postalCode />\
                          <country>United States</country>\
                          <dateAndTime>2005-08-26T09:00:00</dateAndTime>\
                          <fatalities>1300</fatalities>\
                          <injuries>-1</injuries>\
                          <populationIll>-1</populationIll>\
                          <populationDisplaced />\
                          <environmentalImpact />\
                          <politicalChanges />\
                          <culturalChanges />\
                          <jobsLost>-1</jobsLost>\
                          <damageInUSD>10000000000</damageInUSD>\
                          <reparationCost>-1</reparationCost>\
                          <regulatoryChanges>-1</regulatoryChanges>\
                          </crisis>")
        testElement = getElement(row, 'crisisId')
        self.assert_(testElement == "CRI_001")

    def test_getElement2(self):  #test case where returns 'NULL'
        row = fromstring("<org>\
                          <orgId>ORG_001</orgId>\
                          <name>FEMA</name>\
                          <kind>Government Agency</kind>\
                          <streetAddress>500 C Street SW</streetAddress>\
                          <city>Washington, D.C.</city>\
                          <stateOrProvince />\
                          <postalCode>20472</postalCode>\
                          <country>USA</country>\
                          <foundingMission>Support and protect citizens including during disaster or recovery</foundingMission>\
                          <dateFounded>1979-04-01</dateFounded>\
                          <dateAbolished>0001-01-01</dateAbolished>\
                          <majorEvents>First establishment of a federal emergency management in U.S. by Congressional Act of 1803</majorEvents>\
                          </org>")
        testElement = getElement(row, 'stateOrProvince')
        self.assert_(testElement == "NULL")

    def test_getElement3(self):  # test if cannot find a match
        row = fromstring("<crisisResourcePair>\
                          <crisisId>CRI_001</crisisId>\
                          <resourceId>RES_001</resourceId>\
                          </crisisResourcePair>")
        testElement = getElement(row, 'stateOrProvince')
        self.assert_(testElement == "NULL")

    def test_getElement4(self):
        row = fromstring("<person>\
                          <personId>PER_001</personId>\
                          <name>George Clooney</name>\
                          <kind>Actor / Actress </kind>\
                          <streetAddress>8817 Lookout Mountain Ave</streetAddress>\
                          <city>Los Angeles</city>\
                          <stateOrProvince>California</stateOrProvince>\
                          <postalCode>90046-1819</postalCode>\
                          <country>USA</country>\
                          </person>")
        testElement = getElement(row, 'stateOrProvince')
        self.assert_(testElement == "California")

    def test_getElement5(self):
        row = fromstring("<citationPair>\
                          <citationId>CIT_101</citationId>\
                          <citation>http://www.ncdc.noaa.gov/extremeevents/specialreports/Hurricane-Katrina.pdf</citation>\
                          </citationPair>")
        testElement = getElement(row, 'citation')
        self.assert_(testElement == "http://www.ncdc.noaa.gov/extremeevents/specialreports/Hurricane-Katrina.pdf")

    def test_getElement6(self):
        row = fromstring("<url>\
                          <urlId>URL_101</urlId>\
                          <type>Image</type>\
                          <urlAddress>http://web.mit.edu/12.000/www/m2010/images/katrina-08-28-2005.jpg</urlAddress>\
                          </url>")
        testElement = getElement(row, 'stateOrProvince')
        self.assert_(testElement == "NULL")


    # Testing of importXML
    def test_importXML1(self):
        db = _mysql.connect(host="z", user="wigu", passwd="U865dZpL0E", db="cs327e_wigu")
        truncateAllTables(db)

        inputString = StringIO("""<root>
                                      <crises>
                                          <crisis>
                                              <crisisId>CRI_001</crisisId>
                                              <name>Katrina</name>
                                              <kind>Natural Disaster</kind>
                                              <city>New Orleans</city>
                                              <stateOrProvince>Louisiana</stateOrProvince>
                                              <country>United States</country>
                                              <dateAndTime>2005-08-26T09:00:00</dateAndTime>
                                              <fatalities>1300</fatalities>
                                              <damageInUSD>10000000000</damageInUSD>
                                          </crisis>
                                      </crises>
                                  </root>""")
        importXML(inputString)

        db.query("SELECT * FROM Crises")
        result = db.store_result()
        rows = result.fetch_row(maxrows=0, how=1)
        self.assert_(rows[0] == {"crisisId" : "1",
                                 "name" : "Katrina",
                                 "kind" : "Natural Disaster",
                                 "streetAddress" : None,
                                 "city" : "New Orleans",
                                 "stateOrProvince" : "Louisiana",
                                 "postalCode" : None,
                                 "country" : "United States",
                                 "dateAndTime" : "2005-08-26 09:00:00",
                                 "fatalities" : "1300",
                                 "injuries" : None,
                                 "populationIll" : None,
                                 "populationDisplaced" : None,
                                 "environmentalImpact" : None,
                                 "politicalChanges" : None,
                                 "culturalChanges" : None,
                                 "jobsLost" : None,
                                 "damageInUSD" : "10000000000",
                                 "reparationCost" : None,
                                 "regulatoryChanges" : None})

    def test_importXML2(self):
        db = _mysql.connect(host="z", user="wigu", passwd="U865dZpL0E", db="cs327e_wigu")
        truncateAllTables(db)

        inputString = StringIO("""<root>
                                      <orgs>
                                          <org>
                                              <orgId>ORG_001</orgId>
                                              <name>FEMA</name>
                                              <kind>Government Agency</kind>
                                              <streetAddress>500 C Street SW</streetAddress>
                                              <city>Washington, D.C.</city>
                                              <postalCode>20472</postalCode>
                                              <country>USA</country>
                                              <foundingMission>Support and protect citizens including during disaster or recovery</foundingMission>
                                              <dateFounded>1979-04-01</dateFounded>
                                              <majorEvents>First establishment of a federal emergency management in U.S. by Congressional Act of 1803</majorEvents>
                                          </org>
                                      </orgs>
                                  </root>""")
        importXML(inputString)

        db.query("SELECT * FROM Orgs")
        result = db.store_result()
        rows = result.fetch_row(maxrows=0, how=1)
        self.assert_(rows[0] == {"orgId" : "1",
                                 "name" : "FEMA",
                                 "kind" : "Government Agency",
                                 "streetAddress" : "500 C Street SW",
                                 "city" : "Washington, D.C.",
                                 "stateOrProvince" : None,
                                 "postalCode" : "20472",
                                 "country" : "USA",
                                 "foundingMission" : "Support and protect citizens including during disaster or recovery",
                                 "dateFounded" : "1979-04-01",
                                 "dateAbolished" : None,
                                 "majorEvents" : "First establishment of a federal emergency management in U.S. by Congressional Act of 1803"})

    def test_importXML3(self):
        db = _mysql.connect(host="z", user="wigu", passwd="U865dZpL0E", db="cs327e_wigu")
        truncateAllTables(db)

        inputString = StringIO("""<root>
                                      <people>
                                          <person>
                                              <personId>PER_001</personId>
                                              <name>George Clooney</name>
                                              <kind>Actor / Actress</kind>
                                              <streetAddress>8817 Lookout Mountain Ave</streetAddress>
                                              <city>Los Angeles</city>
                                              <stateOrProvince>California</stateOrProvince>
                                              <postalCode>90046-1819</postalCode>
                                              <country>USA</country>
                                            </person>
                                      </people>
                                  </root>""")
        importXML(inputString)

        db.query("SELECT * FROM People")
        result = db.store_result()
        rows = result.fetch_row(maxrows=0, how=1)
        self.assert_(rows[0] == {"personId" : "1",
                                 "name" : "George Clooney",
                                 "kind" : "Actor / Actress",
                                 "streetAddress" : "8817 Lookout Mountain Ave",
                                 "city" : "Los Angeles",
                                 "stateOrProvince" : "California",
                                 "postalCode" : "90046-1819",
                                 "country" : "USA"})

    def test_importXML4(self):
        db = _mysql.connect(host="z", user="wigu", passwd="U865dZpL0E", db="cs327e_wigu")
        truncateAllTables(db)

        inputString = StringIO("""<root>
                                      <urls>
                                          <url>
                                              <urlId>URL_101</urlId>
                                              <type>Image</type>
                                              <urlAddress>http://web.mit.edu/12.000/www/m2010/images/katrina-08-28-2005.jpg</urlAddress>
                                          </url>
                                      </urls>
                                  </root>""")
        importXML(inputString)

        db.query("SELECT * FROM Urls")
        result = db.store_result()
        rows = result.fetch_row(maxrows=0, how=1)
        self.assert_(rows[0] == {"urlId" : "101",
                                 "type" : "Image",
                                 "urlAddress" : "http://web.mit.edu/12.000/www/m2010/images/katrina-08-28-2005.jpg"})

    def test_importXML5(self):
        db = _mysql.connect(host="z", user="wigu", passwd="U865dZpL0E", db="cs327e_wigu")
        truncateAllTables(db)

        inputString = StringIO("""<root>
                                      <citations>
                                          <citationPair>
                                              <citationId>CIT_101</citationId>
                                              <citation>http://www.ncdc.noaa.gov/extremeevents/specialreports/Hurricane-Katrina.pdf</citation>
                                          </citationPair>
                                      </citations>
                                  </root>""")
        importXML(inputString)

        db.query("SELECT * FROM Citations")
        result = db.store_result()
        rows = result.fetch_row(maxrows=0, how=1)
        self.assert_(rows[0] == {"citationId" : "101",
                                 "citation" : "http://www.ncdc.noaa.gov/extremeevents/specialreports/Hurricane-Katrina.pdf"})


    # Testing of exportXML
    def test_exportXML1(self):
        db = _mysql.connect(host="z", user="wigu", passwd="U865dZpL0E", db="cs327e_wigu")
        truncateAllTables(db)

        db.query("INSERT INTO Crises (crisisId, name, kind, "
                                     "streetAddress, city, stateOrProvince, postalCode, country, "
                                     "dateAndTime, fatalities, injuries, populationIll, populationDisplaced, "
                                     "environmentalImpact, politicalChanges, culturalChanges, "
                                     "jobsLost, damageInUSD, reparationCost, regulatoryChanges) "
                 "VALUES (001, 'Katrina', 'Natural Disaster', NULL, 'New Orleans', 'Louisiana', NULL, 'United States', STR_TO_DATE('2005-08-26T09:00:00', '%Y-%m-%dT%H:%i:%s'), 1300, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 10000000000, NULL, NULL)")

        writer = StringIO()
        exportXML(writer)

        self.assert_(writer.getvalue() == u"<?xml version=\"1.0\" ?>\n"\
                                          u"<root>\n"\
                                          u"    <crises>\n"\
                                          u"        <crisis>\n"\
                                          u"            <crisisId>CRI_1</crisisId>\n"\
                                          u"            <name>Katrina</name>\n"\
                                          u"            <kind>Natural Disaster</kind>\n"\
                                          u"            <city>New Orleans</city>\n"\
                                          u"            <stateOrProvince>Louisiana</stateOrProvince>\n"\
                                          u"            <country>United States</country>\n"\
                                          u"            <dateAndTime>2005-08-26T09:00:00</dateAndTime>\n"\
                                          u"            <fatalities>1300</fatalities>\n"\
                                          u"            <damageInUSD>10000000000</damageInUSD>\n"\
                                          u"        </crisis>\n"\
                                          u"    </crises>\n"\
                                          u"    <orgs/>\n"\
                                          u"    <people/>\n"\
                                          u"    <resources/>\n"\
                                          u"    <crisisResources/>\n"\
                                          u"    <waysToHelp/>\n"\
                                          u"    <crisisWaysToHelp/>\n"\
                                          u"    <contactInfos/>\n"\
                                          u"    <orgContactInfos/>\n"\
                                          u"    <citations/>\n"\
                                          u"    <crisisCitations/>\n"\
                                          u"    <orgCitations/>\n"\
                                          u"    <personCitations/>\n"\
                                          u"    <urls/>\n"\
                                          u"    <crisisUrls/>\n"\
                                          u"    <orgUrls/>\n"\
                                          u"    <personUrls/>\n"\
                                          u"    <crisisOrgs/>\n"\
                                          u"    <crisisPeople/>\n"\
                                          u"    <orgPeople/>\n"\
                                          u"</root>\n")

    def test_exportXML2(self):
        db = _mysql.connect(host="z", user="wigu", passwd="U865dZpL0E", db="cs327e_wigu")
        truncateAllTables(db)

        db.query("INSERT INTO Orgs (orgId, name, kind, "
                                   "streetAddress, city, stateOrProvince, postalCode, country, "
                                   "foundingMission, dateFounded, dateAbolished, majorEvents) "\
                 "VALUES (001, 'FEMA', 'Government Agency', '500 C Street SW', 'Washington, D.C.', NULL, '20472', 'USA', 'Support and protect citizens including during disaster or recovery', STR_TO_DATE('1979-04-01', '%Y-%m-%d'), STR_TO_DATE(NULL, '%Y-%m-%d'), 'First establishment of a federal emergency management in U.S. by Congressional Act of 1803')")

        writer = StringIO()
        exportXML(writer)

        self.assert_(writer.getvalue() == u"<?xml version=\"1.0\" ?>\n"\
                                          u"<root>\n"\
                                          u"    <crises/>\n"\
                                          u"    <orgs>\n"\
                                          u"        <org>\n"\
                                          u"            <orgId>ORG_1</orgId>\n"\
                                          u"            <name>FEMA</name>\n"\
                                          u"            <kind>Government Agency</kind>\n"\
                                          u"            <streetAddress>500 C Street SW</streetAddress>\n"\
                                          u"            <city>Washington, D.C.</city>\n"\
                                          u"            <postalCode>20472</postalCode>\n"\
                                          u"            <country>USA</country>\n"\
                                          u"            <foundingMission>Support and protect citizens including during disaster or recovery</foundingMission>\n"\
                                          u"            <dateFounded>1979-04-01</dateFounded>\n"\
                                          u"            <majorEvents>First establishment of a federal emergency management in U.S. by Congressional Act of 1803</majorEvents>\n"\
                                          u"        </org>\n"\
                                          u"    </orgs>\n"\
                                          u"    <people/>\n"\
                                          u"    <resources/>\n"\
                                          u"    <crisisResources/>\n"\
                                          u"    <waysToHelp/>\n"\
                                          u"    <crisisWaysToHelp/>\n"\
                                          u"    <contactInfos/>\n"\
                                          u"    <orgContactInfos/>\n"\
                                          u"    <citations/>\n"\
                                          u"    <crisisCitations/>\n"\
                                          u"    <orgCitations/>\n"\
                                          u"    <personCitations/>\n"\
                                          u"    <urls/>\n"\
                                          u"    <crisisUrls/>\n"\
                                          u"    <orgUrls/>\n"\
                                          u"    <personUrls/>\n"\
                                          u"    <crisisOrgs/>\n"\
                                          u"    <crisisPeople/>\n"\
                                          u"    <orgPeople/>\n"\
                                          u"</root>\n")

    def test_exportXML3(self):
        db = _mysql.connect(host="z", user="wigu", passwd="U865dZpL0E", db="cs327e_wigu")
        truncateAllTables(db)

        db.query("INSERT INTO People (personId, name, kind, streetAddress, city, stateOrProvince, postalCode, country) "\
                 "VALUES (001, 'George Clooney', 'Actor / Actress', '8817 Lookout Mountain Ave', 'Los Angeles', 'California', '90046-1819', 'USA')")

        writer = StringIO()
        exportXML(writer)

        self.assert_(writer.getvalue() == u"<?xml version=\"1.0\" ?>\n"\
                                          u"<root>\n"\
                                          u"    <crises/>\n"\
                                          u"    <orgs/>\n"\
                                          u"    <people>\n"\
                                          u"        <person>\n"\
                                          u"            <personId>PER_1</personId>\n"\
                                          u"            <name>George Clooney</name>\n"\
                                          u"            <kind>Actor / Actress</kind>\n"\
                                          u"            <streetAddress>8817 Lookout Mountain Ave</streetAddress>\n"\
                                          u"            <city>Los Angeles</city>\n"\
                                          u"            <stateOrProvince>California</stateOrProvince>\n"\
                                          u"            <postalCode>90046-1819</postalCode>\n"\
                                          u"            <country>USA</country>\n"\
                                          u"        </person>\n"\
                                          u"    </people>\n"\
                                          u"    <resources/>\n"\
                                          u"    <crisisResources/>\n"\
                                          u"    <waysToHelp/>\n"\
                                          u"    <crisisWaysToHelp/>\n"\
                                          u"    <contactInfos/>\n"\
                                          u"    <orgContactInfos/>\n"\
                                          u"    <citations/>\n"\
                                          u"    <crisisCitations/>\n"\
                                          u"    <orgCitations/>\n"\
                                          u"    <personCitations/>\n"\
                                          u"    <urls/>\n"\
                                          u"    <crisisUrls/>\n"\
                                          u"    <orgUrls/>\n"\
                                          u"    <personUrls/>\n"\
                                          u"    <crisisOrgs/>\n"\
                                          u"    <crisisPeople/>\n"\
                                          u"    <orgPeople/>\n"\
                                          u"</root>\n")

    def test_exportXML4(self):
        db = _mysql.connect(host="z", user="wigu", passwd="U865dZpL0E", db="cs327e_wigu")
        truncateAllTables(db)

        db.query("INSERT INTO Citations (citationId, citation) "\
                 "VALUES ('101', 'http://www.ncdc.noaa.gov/extremeevents/specialreports/Hurricane-Katrina.pdf')")

        writer = StringIO()
        exportXML(writer)

        self.assert_(writer.getvalue() == u"<?xml version=\"1.0\" ?>\n"\
                                          u"<root>\n"\
                                          u"    <crises/>\n"\
                                          u"    <orgs/>\n"\
                                          u"    <people/>\n"\
                                          u"    <resources/>\n"\
                                          u"    <crisisResources/>\n"\
                                          u"    <waysToHelp/>\n"\
                                          u"    <crisisWaysToHelp/>\n"\
                                          u"    <contactInfos/>\n"\
                                          u"    <orgContactInfos/>\n"\
                                          u"    <citations>\n"\
                                          u"        <citationPair>\n"\
                                          u"            <citationId>CIT_101</citationId>\n"\
                                          u"            <citation>http://www.ncdc.noaa.gov/extremeevents/specialreports/Hurricane-Katrina.pdf</citation>\n"\
                                          u"        </citationPair>\n"\
                                          u"    </citations>\n"\
                                          u"    <crisisCitations/>\n"\
                                          u"    <orgCitations/>\n"\
                                          u"    <personCitations/>\n"\
                                          u"    <urls/>\n"\
                                          u"    <crisisUrls/>\n"\
                                          u"    <orgUrls/>\n"\
                                          u"    <personUrls/>\n"\
                                          u"    <crisisOrgs/>\n"\
                                          u"    <crisisPeople/>\n"\
                                          u"    <orgPeople/>\n"\
                                          u"</root>\n")

unittest.main()
