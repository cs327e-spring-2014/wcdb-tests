
from xml.etree.ElementTree import Element, fromstring, tostring

def WCDB_run(r):
    """
transforms a string into an ElementTree
s is a string
a is an element
return an Element
"""
    s = r.readline()
    if s in ["", "\n", None]:
	return s
    a = fromstring(s)
    assert(type(a) is Element)
    return a

    l = tostring(a)
    assert(type(l) is str)
    return l

    if l in ["", "\n", None]:
        return l
        

def WCDB_solve(r,w):
    """
reads an input file per block of Element tree until the end of the file
return string
"""
    while True:
        output = WCDB_run(r)
        if output in ["", "\n", None]:
            return output
        w.write(output + "\n")
