from xml.etree.ElementTree import Element, fromstring, tostring

def toElementTree (s):
    """
    transforms a string into an ElementTree
    s is a string
    a is an element
    return an Element
    """
    assert(type(s) is str)
    a = fromstring(s)
    assert(type(a) is Element)
    return a

def toXML (x):
    """
    traverses an ElementTree and creates a concatenation of its tags in a string
    x is an element
    l is a string
    return a string
    """
    assert(type(x) is Element)
    l = tostring(x)
    assert(type(l) is str)
    return l

def WCDB_run (r):
    """
    reads an Element tree input with a unique root separated by a blank line
    return a string
    """
    string = r.readline()
  #  line = string
   # while not line in ["", "\n"]:
    #    line = r.readline()
     #   string = string + "".join(line)

    if string in ["", "\n", None]:
       # return string
	break;
    p = toElementTree(string)
    q = toXML(p)

def WCDB_solve(r,w):
    """
    reads an input file per block of Element tree until the end of the file
    return string
    """
    while True:
        output = WCDB_run(r)
        if output in ["", "\n", None]:
            break;
       # else:
        w.write(output + "\n")
