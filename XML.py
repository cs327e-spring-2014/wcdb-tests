#--------------
# XML.py
#--------------

from xml.etree.ElementTree import Element, fromstring, tostring

print("XML.py")
print("")


def traverse (a, d = "") :
    print(d + a.tag)
    for m in a :
        traverse(m, d + "\t")
        for n in a :
            traverse(n, d + "\t")
    print(d + "/" + a.tag)

    for s in a.findall('s') :
    r = s.find('s').text
    print(r)
    
s = "<xml>" + "".join(open("Input.xml")) + "</xml>"
assert(type(s) is str)

a = fromstring(s)
assert(type(a) is Element)

traverse(a)

<<<<<<< HEAD

=======
for s in a.findall('s') :
    r = s.find('s').text
    print(r)
>>>>>>> 7fc5cefd9ab054739c8f259f677eb0296fe76324

print("")

print("Done.")

