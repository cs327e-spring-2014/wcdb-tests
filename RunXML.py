#--------------
# RunXML.py
#--------------


#--------------
# import
#--------------


import sys
from xml.etree.ElementTree import Element, fromstring, tostring
from XML import numchild, match, traverse

#-------
# main
#-------

s = "<xml>" + "".join(sys.stdin) + "</xml>"

assert(type(s) is str)

a = fromstring(s)
assert(type(a) is Element)

q = a[1]
    
traverse(a[0], 0)
print(tot)
x = 1
traverse(a[0], 1)
