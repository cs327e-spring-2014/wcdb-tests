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

def WCBD_run (r):
    string = r.readline()
    line = string
    while not line in ["", "\n"]:
        line = r.readline()
        string = string + "".join(line)


    if string in ["", "\n", None]:
        return string
    a = toElementTree(string)
    assert(type(a) is Element)
    l = toXML(a)
    assert(type(l) is str)
    return l

def WCBD_solve(r,w):
    while True:
        output = WCBD_run(r)
        if output in ["", "\n", None]:
            break;
        else:
            w.write(output + "\n")

