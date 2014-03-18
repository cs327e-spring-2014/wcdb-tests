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
    assert(type(x) is Element)
    temp = x.tag
    l= l + "<" + temp+ ">"
    for v in x:
        l = toString(v, l )
    l = l + "<" + "/" + temp + ">"
    assert(l != "")
    assert(type(l) is str)
    return l

i = toElementTree("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")
print i

s= toString(i)
print s