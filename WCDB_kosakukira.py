from xml.etree.ElementTree import Element, ElementTree, fromstring, tostring

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

def toTheString (x, l=""):
    """
    traverses an ElementTree and creates a concatenation of its tags in a string
    x is an element
    l is a string
    return a string
    """
    if x in ["", "\n"]:
        return x

    assert(type(x) is Element)

    #l = tostring(x)
    """
    Before, I was trying to toss the below code in favor of additional imports ElementTree
    and tostring.

    However, a simple tostring(element), despite its name,
    returned a "bytes" type that looked like this:
    b\\<apple>< orange /></apple>b\\

    I don't know how or why it happened, so I went ahead and revrted the changes I tried to make.
    """
    temp = x.tag
    l= l + "<" + temp+ ">"
    for v in x:
        print(v.text)
        l = toTheString(v, l )
    l = l + "<" + "/" + temp + ">"
    print(l)
    assert(l != "")
    assert(type(l) is str)
    return l

def WCBD_run (r):
    string = r.readline()
    line = string
    while not line in ["", "\n"]:
        line = r.readline()
        string = string + "".join(line)

    print()
    if string in ["", "\n", None]:
        return string
    a = toElementTree(string)
    assert(type(a) is Element)
    l = toString(a)
    assert(type(l) is str)
    return l

def WCBD_solve(r,w):
    while True:
        output = WCBD_run(r)
        if output in ["", "\n", None]:
            break
        else:
            w.write(output + "\n")

