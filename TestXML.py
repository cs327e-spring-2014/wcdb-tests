<<<<<<< HEAD
#-------------------
# TestXML.py
#-------------------

<<<<<<< HEAD
from xml.etree.ElementTree import Element, fromstring

print("TestXML.py")
print()
=======
>>>>>>> 4a3c794bc81c8bc230a4a46524ce9a0eb5c8a3c9

=======
>>>>>>> ec8b78355662f129f98cb83b09808649ae7a3623
import io
import unittest


from xml.etree.ElementTree import Element, fromstring, tostring

#-------------------
# TestXML.py
#-------------------


print("TestXML.py")
print()


def traverse (a, d = "") :
    assert (len.(a) != 0)
    print(d + a.tag)
    for v in a :
        traverse(v, d + "\t")
    print(d + "/" + a.tag)

s = "<xml>" + "".join(open("Input.xml")) + "</xml>"
assert(type(s) is str)
assert(len.type(s) != 0)

a = fromstring(s)
assert(type(a) is Element)

traverse(a)
print()

print("Done.")



