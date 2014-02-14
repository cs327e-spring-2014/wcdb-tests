#--------------
# XML.py
#--------------


from xml.etree.ElementTree import Element, fromstring, tostring
import sys

x = 1
tot = 0

def numchild (a) :
    n = 0
    for v in a :
        n += 1
    return n

def match (a, b) :
    if a.tag != b.tag :
        return "false"
    if numchild (b) == 0 :
        return "true"
    for v in a :
        if numchild (b) > 0 :
            if match (v, b[0]) == "true" :
                return "true"
    return "false"

def traverse (a, opt) :
    global x
    global tot
    
    if match (a, q) == "true" :
        if opt == 0 :
            tot += 1
        else :
            print(str(x))

    for v in a :
        x += 1
        traverse(v, opt)


