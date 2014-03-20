from xml.etree.ElementTree import Element, fromstring

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

def toString (x, l=""):
    """
    traverses an ElementTree and creates a concatenation of its tags in a string
    x is an element
    l is a string
    return a string
    """
    if x in ["", "\n"]:
        return x

    assert(type(x) is Element)
    temp = x.tag
    l= l + "<" + temp+ ">"
    for v in x:
        l = toString(v, l )
    l = l + "<" + "/" + temp + ">"
    assert(l != "")
    assert(type(l) is str)
    return l


"""
Is WCBD_run necessary? Also, it should be WCDB.
"""
def WCBD_run (r):
    string = r.readline()
    line = string
    while not line in ["", "\n"]:
        line = r.readline()
        string = string + "".join(line)

    print line
    if string in ["", "\n", None]:
        return string
    a = toElementTree(string)
    assert(type(a) is Element)
    l = toString(a)
    assert(type(l) is str)
    return l

"""
Is WCBD_solve necessary either? I thought we were just doing import/export.
"""
def WCBD_solve(r,w):
    while True:
        output = WCBD_run(r)
        if output in ["", "\n", None]:
            break;
        else:
            w.write(output + "\n")

