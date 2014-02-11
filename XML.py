

#--------------
# XML.py
#--------------

from xml.etree.ElementTree import Element, fromstring, tostring

print("XML.py")
<<<<<<< HEAD
print("")
=======
print()
>>>>>>> ec8b78355662f129f98cb83b09808649ae7a3623

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
<<<<<<< HEAD
print("")
=======
print()
>>>>>>> ec8b78355662f129f98cb83b09808649ae7a3623

print("Done.")

