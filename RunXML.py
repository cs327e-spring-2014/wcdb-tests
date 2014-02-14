#--------------
# RunXML.py
#--------------


#--------------
# import
#--------------


import sys
from XML import numchild, match, traverse

#-------
# main
#-------

string = sys.stdin.readlines()
s = "<xml>" + "".join(string) + "</xml>"
assert(type(s) is str)

a = fromstring(s)
assert(type(a) is Element)

q = a[len(a)]
    
traverse(a[0], 0)
print(tot)
x = 1
traverse(a[0], 1)


