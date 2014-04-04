#!/usr/bin/env python

from xml.etree.ElementTree import Element, fromstring, tostring

import _mysql

def login () :
    c = _mysql.connect(
            host = "z",
            user = "ksombra",
            passwd = "QAUG7bpXD2",
            db = "cs327e_ksombra")
    assert str(type(c)) == "<type '_mysql.connection'>"
    return c

# --------
# Query.py
# --------

def query (c, s) :
    assert(str(type(c)) == "<type '_mysql.connection'>")
    assert(type(s) is str)
    c.query(s)
    r = c.use_result()
    if r is None :
        return None
    assert(str(type(r)) == "<type '_mysql.result'>")
    t = r.fetch_row(maxrows = 0)
    assert(type(t) is tuple)
    return t

# --------
# WCDB1
# --------

def toElementTree (s):
    """
transforms a string into an ElementTree
s is a string
a is an element
return an Element
"""
    assert(type(s) is str)
    a = fromstring(s)
    assert(type(a) is Element)
    return a

def toXML (x):
    """
traverses an ElementTree and creates a concatenation of its tags in a string
x is an element
l is a string
return a string
"""
    assert(type(x) is Element)
    l = tostring(x)
    assert(type(l) is str)
    return l

# ---------
# WCDB2
# ---------

def getElement(row, elementName, isString=True):
    element = row.find(elementName)
    if (element is None or element.text is None):
        return "NULL"
    else:
        return "'" + element.text.replace("'", "\\'") + "'" if isString else element.text

def setSQLClassification (c, ele) :
    """
Utilizes brute force (since python doesn't have switch statements) to determine which classification the element
given in the data system is (ie, is it in crises table, or is it in persons table, etc)
It then executes a function based on which it's in to write all of its children to the table
c is a mysql connection object (already set up generally)
e is an element (designed for reference in the direct children of root)
"""
    st=ele.tag
    if st == "crises" :
        setSQLcrises(c, ele)
    elif st == "orgs" :
        setSQLorgs(c, ele)
    elif st == "people" :
        setSQLpeople(c, ele)
    elif st == "crisisKinds" :
        setSQLcrisisKinds(c, ele)
    elif st == "orgKinds" :
        setSQLorgKinds(c, ele)
    elif st == "personKinds" :
        setSQLpersonKinds(c, ele)
    elif st == "resources" :
        setSQLresources(c, ele)
    elif st == "crisisResources" :
        setSQLcrisisResources(c, ele)
    elif st == "waysToHelp" :
        setSQLwaysToHelp(c, ele)
    elif st == "crisisWaysToHelp" :
        setSQLwaysToHelp(c, ele)
    elif st == "contactInfos" :
        setSQLcontactInfos(c, ele)
    elif st == "orgContactInfos" :
        setSQLorgContactInfos(c, ele)
    elif st == "citations" :
        setSQLcitations(c, ele)
    elif st == "crisisCitations" :
        setSQLcrisisCitations(c, ele)
    elif st == "orgCitations" :
        setSQLorgCitations(c, ele)
    elif st == "personCitations" :
        setSQLpersonCitations(c, ele)
    elif st == "urls" :
        setSQLurls(c, ele)
    elif st == "crisisUrls" :
        setSQLcrisisUrls(c, ele)
    elif st == "orgUrls" :
        setSQLorgUrls(c, ele)
    elif st == "personUrls" :
        setSQLpersonUrls(c, ele)
    elif st == "crisisOrgs" :
        setSQLcrisisOrgs(c, ele)
    elif st == "crisisPeople" :
        setSQLcrisisPeople(c, ele)
    elif st == "orgPeople" :
        setSQLorgPeople(c, ele)
    
    # Rest of them, add these as you go along!
    
# --------
# The following block of functions each take an element from the children
# of the root element in our xml trees
# as well as a connection c
# --------


# Note to self: use different builder function for the strings (one linked on piazza should work)

def setSQLcrises (c, ele) :
    for i in ele :
        s = "Insert into Crises values("
        s+= "'" + getElement(i,'crisisId')[5:] + ","
        s+= getElement(i,'name') + ","
        s+= getElement(i,'streetAddress') + ","
        s+= getElement(i,'city') + ","
        s+= getElement(i,'stateOrProvince') + ","
        s+= getElement(i,'postalCode') + ","
        s+= getElement(i,'country') + ","
        s+= getElement(i,'dateAndTime') + ","
        s+= getElement(i,'fatalities') + ","
        s+= getElement(i,'injuries') + ","
        s+= getElement(i,'populationIll') + ","
        s+= getElement(i,'populationDisplaced') + ","
        s+= getElement(i,'environmentalImpact') + ","
        s+= getElement(i,'politicalChanges') + ","
        s+= getElement(i,'culturalChanges') + ","
        s+= getElement(i,'jobsLost') + ","
        s+= getElement(i,'damageInUSD') + ","
        s+= getElement(i,'reparationCost') + ","
        s+= getElement(i,'regulatoryChanges') + ");"

        query(c, s)
        
        
def setSQLorgs (c, ele) :
    for i in ele :
        s = "Insert into Orgs values("
        s+= "'" + getElement(i,'orgId')[5:] + ","
        s+= getElement(i,'name') + ","
        s+= getElement(i,'streetAddress') + ","
        s+= getElement(i,'city') + ","
        s+= getElement(i,'stateOrProvince') + ","
        s+= getElement(i,'postalCode') + ","
        s+= getElement(i,'country') + ","
        s+= getElement(i,'foundingMission') + ","
        s+= getElement(i,'dateFounded') + ","
        s+= getElement(i,'dateAbolished') + ","
        s+= getElement(i,'majorEvents') + ");"

        query(c, s)
        
def setSQLpeople (c, ele) :
    for i in ele :
        s = "Insert into People values("
        s+= "'" + getElement(i,'personId')[5:] + ","
        s+= getElement(i,'name') + ","
        s+= getElement(i,'streetAddress') + ","
        s+= getElement(i,'city') + ","
        s+= getElement(i,'stateOrProvince') + ","
        s+= getElement(i,'postalCode') + ","
        s+= getElement(i,'country') + ");"

        query(c, s)

def setSQLcrisisKinds (c, ele) :
    for i in ele :
        s = "Insert into CrisisKinds values("
        s+= "'" + getElement(i,'crisisId')[5:] + ","
        s+= getElement(i,'kind') + ");"

        query(c, s)

def setSQLorgKinds (c, ele) :
    for i in ele :
        s = "Insert into OrgKinds values("
        s+= "'" + getElement(i,'orgId')[5:] + ","
        s+= getElement(i,'kind') + ");"

        query(c, s)

def setSQLpersonKinds (c, ele) :
    for i in ele :
        s = "Insert into PersonKinds values("
        s+= "'" + getElement(i,'personId')[5:] + ","
        s+= getElement(i,'kind') + ");"

        query(c, s)

def setSQLresources (c, ele) :
    for i in ele :
        s = "Insert into Resources values("
        s+= "'" + getElement(i,'resourceId')[5:] + ","
        s+= getElement(i,'resource') + ");"

        query(c, s)

def setSQLcrisisResources (c, ele) :
    for i in ele :
        s = "Insert into CrisisResources values("
        s+= "'" + getElement(i,'crisisId')[5:] + ","
        s+= "'" + getElement(i,'resourceId')[5:] + ");"

        query(c, s)

def setSQLwaysToHelp (ele):
    for i in ele :
        s = "Insert into WaysToHelp values("
        s+= "'" + getElement(i,'helpId')[5:] + ","
        s+= getElement(i,'wayToHelp') + ");"

        query(c, s)

def setSQLcrisisWaysToHelp (ele):
    for i in ele :
        s = "Insert into CrisisWaysToHelp values("
        s+= "'" + getElement(i,'crisisId')[5:] + ","
        s+= "'" + getElement(i,'helpId')[5:] + ");"

        query(c, s)

def setSQLcontactInfos (c, ele) :
    for i in ele :
        s = "Insert into ContactInfos values("
        s+= "'" + getElement(i,'contactInfoId')[5:] + ","
        s+= getElement(i,'phoneNumber') + ","
        s+= getElement(i,'emailAddress') + ","
        s+= "'" + getElement(i,'facebookUrlId')[5:] + ","
        s+= "'" + getElement(i,'twitterUrlId')[5:] + ","
        s+= "'" + getElement(i,'websiteUrlId')[5:] + ");"

        query(c, s)

def setSQLorgContactInfos (c, ele) :
    for i in ele :
        s = "Insert into OrgContactInfos values("
        s+= "'" + getElement(i,'orgId')[5:] + ","
        s+= "'" + getElement(i,'contactInfoId')[5:] + ");"

        query(c, s)

def setSQLcitations (c, ele) :
    for i in ele :
        s = "Insert into Citations values("
        s+= "'" + getElement(i,'citationId')[5:] + ","
        s+= getElement(i,'citation') + ");"

        query(c, s)

def setSQLcrisisCitations (c, ele) :
    for i in ele :
        s = "Insert into CrisisCitations values("
        s+= "'" + getElement(i,'citationId')[5:] + ","
        s+= "'" + getElement(i,'crisisId')[5:] + ");"

        query(c, s)

def setSQLorgCitations (c, ele) :
    for i in ele :
        s = "Insert into OrgCitations values("
        s+= "'" + getElement(i,'orgId')[5:] + ","
        s+= "'" + getElement(i,'citationId')[5:] + ");"

        query(c, s)

def setSQLpersonCitations (c, ele) :
    for i in ele :
        s = "Insert into PersonCitations values("
        s+= "'" + getElement(i,'personId')[5:] + ","
        s+= "'" + getElement(i,'citationId')[5:] + ");"

        query(c, s)

def setSQLurls (c, ele) :
    for i in ele :
        s = "Insert into Urls values("
        s+= "'" + getElement(i,'urlId')[5:] + ","
        s+= getElement(i,'type') + ","
        s+= getElement(i,'urlAddress') + ");"

        query(c, s)

def setSQLcrisisUrls (c, ele) :
    for i in ele :
        s = "Insert into CrisisUrls values("
        s+= "'" + getElement(i,'crisisId')[5:] + ","
        s+= "'" + getElement(i,'urlId')[5:] + ");"

        query(c, s)

def setSQLorgUrls (c, ele) :
    for i in ele :
        s = "Insert into OrgUrls values("
        s+= "'" + getElement(i,'orgId')[5:] + ","
        s+= "'" + getElement(i,'urlId')[5:] + ");"

        query(c, s)

def setSQLpersonUrls (c, ele) :
    for i in ele :
        s = "Insert into PersonUrls values("
        s+= "'" + getElement(i,'personId')[5:] + ","
        s+= "'" + getElement(i,'urlId')[5:] + ");"

        query(c, s)

def setSQLcrisisOrgs (c, ele) :
    for i in ele :
        s = "Insert into CrisisOrgs values("
        s+= "'" + getElement(i,'crisisId')[5:] + ","
        s+= "'" + getElement(i,'orgId')[5:] + ");"

        query(c, s)

def setSQLcrisisPeople (c, ele) :
    for i in ele :
        s = "Insert into CrisisPeoplr values("
        s+= "'" + getElement(i,'crisisId')[5:] + ","
        s+= "'" + getElement(i,'personId')[5:] + ");"

        query(c, s)

def setSQLorgPeople (c, ele) :
    for i in ele :
        s = "Insert into OrgPeople values("
        s+= "'" + getElement(i,'orgId')[5:] + ","
        s+= "'" + getElement(i,'personId')[5:] + ");"

        query(c, s)



# -------
# End Block
# -------



def WCDB_run (r):
    """
reads an Element tree input with a unique root separated by a blank line
return a string
"""
    string = r.readline()
    line = string
    while not line in ["", "\n"]:
        line = r.readline()
        string = string + "".join(line)


    if string in ["", "\n", None]:
        return string
    a = toElementTree(string)
    assert(type(a) is Element)

    #WCDB2 Begin
    c = login()
    for el in a:
        # Writes the Element Tree to the Tables
        setSQLClassification(c, el)

    #WCDB2 End
        
    l = toXML(a)
    assert(type(l) is str)
    return l

def WCDB_solve(r,w):
    """
reads an input file per block of Element tree until the end of the file
return string
"""
    while True:
        output = WCDB_run(r)
        if output in ["", "\n", None]:
            break
        else:
            w.write(output + "\n")
