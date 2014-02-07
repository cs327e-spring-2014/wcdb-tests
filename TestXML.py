Python 2.7.3 (default, Sep 26 2013, 20:03:06) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> #-------------------
>>> # TestXML.py
>>> #-------------------
>>> 
>>> from xml.etree.ElementTree import Element, fromstring
>>> 
>>> print("TestXML.py")
print()

s = "<xml>" + "".join(open("ElementTree.xml")) + "</xml>"
assert(type(s) is str)
print(s)
print()

x = fromstring(s)
assert(type(x) is Element)

print("First Level Elements")
print()
for u in x :
    print(u)
print()

print("Second Level Elements")
print()
for u in x :
    for v in u :
        print(v)
print()

print("Third Level Elements")
print()
for u in x :
    for v in u :
        for w in v :
            print(w)
print()

print("Done.")
