<<<<<<< HEAD
#-------------------
# TestXML.py
#-------------------

from xml.etree.ElementTree import Element, fromstring

print("TestXML.py")
print()
=======
>>>>>>> 4a3c794bc81c8bc230a4a46524ce9a0eb5c8a3c9



from xml.etree.ElementTree import Element, fromstring, tostring

#-------------------
# TestXML.py
#-------------------


print("TestXML.py")
print()

def traverse (a, d = "") :
    print(d + a.tag)
    for v in a :
        traverse(v, d + "\t")
    print(d + "/" + a.tag)

s = "<xml>" + "".join(open("Input.xml")) + "</xml>"
assert(type(s) is str)

a = fromstring(s)
assert(type(a) is Element)

traverse(a)
print()

print("Done.")
