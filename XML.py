#--------------
# XML.py
#--------------

from xml.etree.ElementTree import Element, fromstring, tostring, tostringlist

print("XML.py")
print("")
x = 1

def traverse (a, d = "") :
    global x
    #print(d + a.tag + str(x))
    for v in a :
        x += 1
        traverse(v, d + "\t")
    #print(d + "/" + a.tag)

        p = iter(v)
        e = next (p)
        print(e.tag)

    
s = "<xml>" + "".join(open("Input.xml")) + "</xml>"
assert(type(s) is str)

a = fromstring(s)
assert(type(a) is Element)


#for n in a.findall("."):
 #   traverse(n[1])

traverse(a[0], "")


x = 1

print ("Done.")



#def compare() :
 #   while (traverse(a[0], "")
           

           




    

