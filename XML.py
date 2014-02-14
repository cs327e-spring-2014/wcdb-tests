#--------------
# XML.py
#--------------

<<<<<<< HEAD
from xml.etree.ElementTree import Element, fromstring, tostring, tostringlist
=======

from xml.etree.ElementTree import Element, fromstring, tostring
import sys
>>>>>>> b07f09d2af8d6add3d3cdf9e98d428c6d6367848

print("")
x = 1
<<<<<<< HEAD

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
=======
tot = 0

def numchild (a) :
    n = 0
    for v in a :
        n += 1
    return n

def match (a, b) :
    if a.tag != b.tag :
        return "false"
    if numchild (b) == 0 :
        return "true"
    for v in a :
        if numchild (b) > 0 :
            if match (v, b[0]) == "true" :
                return "true"
    return "false"

def traverse (a, opt) :
    global x
    global tot
    
    if match (a, q) == "true" :
        if opt == 0 :
            tot += 1
        else :
            print(str(x))

    for v in a :
        x += 1
        traverse(v, opt)
>>>>>>> b07f09d2af8d6add3d3cdf9e98d428c6d6367848

    
s = "<xml>" + "".join() + "</xml>"
assert(type(s) is str)

a = fromstring(s)
assert(type(a) is Element)

<<<<<<< HEAD

#for n in a.findall("."):
 #   traverse(n[1])

traverse(a[0], "")


x = 1

print ("Done.")



#def compare() :
 #   while (traverse(a[0], "")
           

           




    

=======
q = a[1]
    
traverse(a[0], 0)
print(tot)
x = 1
traverse(a[0], 1)
>>>>>>> b07f09d2af8d6add3d3cdf9e98d428c6d6367848
