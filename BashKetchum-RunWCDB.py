#!/usr/bin/env python

from WCDB import importXML, exportXML
import sys


element = importXML(sys.stdin)
exportXML(element, sys.stdout)