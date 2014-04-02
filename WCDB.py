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
        s+= getElement(i,'stateOrProvince') + ","
        s+= getElement(i,'postalCode') + ","
        s+= getElement(i,'country') + ","
        s+= getElement(i,'dateAndTime') + ","
        s+= getElement(i,'fatalities') + ","
        s+= getElement(i,'injuries') + ","
        s+= getElement(i,'populationIll') + ","
        s+= getElement(i,'populationDisplaced') + ","
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
"""
def setSQLcrisisKinds (c, ele) :

def setSQLorgKinds (c, ele) :

def setSQLpersonKinds (c, ele) :

def setSQLresources (c, ele) :

def setSQLcrisisResources (c, ele) :

def setSQLwaysToHelp (ele):

def setSQLcrisisWaysToHelp (ele):

def setSQLcontactInfos (c, ele) :

def setSQLorgContactInfos (c, ele) :

def setSQLcitations (c, ele) :

def setSQLcrisisCitations (c, ele) :

def setSQLorgCitations (c, ele) :

def setSQLpersonCitations (c, ele) :

def setSQLurls (c, ele) :

def setSQLcrisisUrls (c, ele) :

def setSQLorgUrls (c, ele) :

def setSQLpersonUrls (c, ele) :

def setSQLcrisisOrgs (c, ele) :

def setSQLcrisisPeople (c, ele) :

def setSQLorgPeople (c, ele) :

"""

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
    c = login();
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
            break;
        else:
            w.write(output + "\n")
