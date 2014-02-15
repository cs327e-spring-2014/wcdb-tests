#!/usr/bin/env python

"""
To run the program
% python RunXML.py < RunXML.in > RunXML.out
% chmod ugo+x RunXML.py
% RunXML.py < RunXML.in > RunXML.out

To document the program
% pydoc -w XML
"""

# -------
# imports
# -------

import sys
from XML import main

# ----
# main
# ----
"""
calls main from XML.py
"""
try :
	main()
except :
	pass
