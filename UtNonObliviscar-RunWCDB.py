"""
To run the program
% python WCDB.py < RunWCDB.in > RunWCDB.out
"""

# -------
# imports
# -------

import sys

from WCDB import WCDB_solve

# ----
# main
# ----

WCDB_solve(sys.stdin, sys.stdout)
