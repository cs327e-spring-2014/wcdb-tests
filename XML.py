#--------------
# XML.py
#--------------

from xml.etree.ElementTree import Element, fromstring, tostring, tostringlist

print("XML.py")
print("")


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
print("")



for x in a.findall("./"):
    print (x[0])


for n in a.findall("./"):
    m = tostringlist(n[0])
    print(m)



print("Done.")

