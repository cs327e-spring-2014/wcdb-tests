#!/usr/bin/env python

# --------
# Login.py
# --------

import _mysql

def login () :
    c = _mysql.connect(
            host = "z",
            user = "ksombra",
            passwd = "QAUG7bpXD2",
            db = "cs327e_ksombra")
    assert str(type(c)) == "<type '_mysql.connection'>"
    return c

# --------
# Query.py
# --------

def query (c, s) :
    assert(str(type(c)) == "<type '_mysql.connection'>")
    assert(type(s) is str)
    c.query(s)
    r = c.use_result()
    if r is None :
        return None
    assert(str(type(r)) == "<type '_mysql.result'>")
    t = r.fetch_row(maxrows = 0)
    assert(type(t) is tuple)
    return t

def testPython() :
    conn = login()
    qry = query(c = conn, s = "Insert into TestTable values (27)")
    print(qry)

    qry = query(c = conn, s = "Select * from TestTable")
    print(qry)

    print("Test")

testPython()
