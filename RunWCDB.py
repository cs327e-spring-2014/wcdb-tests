# -----------------------------------------------------------------------
# project 3/WCDB(phase2)/RunWCDB.py
# Author: Xiaoqin LI
# Description:
  #At least 10 acceptance tests (separated by one blank line)
  #with at least 500 lines total, in the files RunWCDB.in and RunWCDB.out
# Date: 04/03/2014
# -----------------------------------------------------------------------

"""
To run the program
    % python3/python RunWCDB.py < RunWCDB.in > RunWCDB.out

To document the program
    % pydoc -w WCDB
"""

# -------
# imports
# -------

import sys
import WCDB

#--------Main fuction--------------------
def main():
    #---------- a list to save the filenames----------

    xml_filename_list = ['UtNonObliviscar-WCDB.xml','SeekWolves-WCDB.xml','BashKetchum-WCDB.xml','TeamRocket-WCDB.xml','Databosses-WCDB.xml','EJADK-WCDB.xml','Brigadeiros-WCDB.xml','GottaGitThat-WCDB.xml']

	#['GottaGitThat-WCDB.xml','UtNonObliviscar-WCDB.xml','SeekWolves-WCDB.xml','BashKetchum-WCDB.xml','TeamRocket-WCDB.xml','Databosses-WCDB.xml','EJADK-WCDB.xml','Brigadeiros-WCDB.xml']#, \]           

    WCDB.wcdb_solve(sys.stdin, sys.stdout,xml_filename_list)
    #----------------------------------------

main()

