
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



