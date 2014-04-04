#!/usr/bin/env python3

# ------------------------------
# Copyright (C) 2014
# Eric Poulter, Anthony Oliveri, Derek Perez,
#   Jesse Vo, Jasmine Mann, and Ksenia Kolesnikova
# -------------------------------


# -------
# imports
# -------

import sys
from WCDB import wcdb_importToMySQL, wcdb_exportToXML


# ----
# main
# ----

allTableNames = ["crises", "orgs", "people", "resources", "crisisResources", "waysToHelp",
                     "crisisWaysToHelp", "contactInfos", "orgContactInfos", "citations", "crisisCitations",
                     "orgCitations", "personCitations", "urls", "crisisUrls", "orgUrls", "personUrls",
                     "crisisOrgs", "crisisPeople", "orgPeople"]

allRowNames = ["crisis", "org", "person", "resource", "crisisResourcePair", "wayToHelpPair",
                   "crisisWayToHelpPair", "contactInfo", "orgContactInfoPair", "citationPair",
                   "crisisCitationPair", "orgCitationPair", "personCitationPair", "url", "crisisUrlPair",
                   "orgUrlPair", "personUrlPair", "crisisOrgPair", "crisisPeoplePair", "orgPeoplePair"]

#wcdb_importToMySQL(sys.stdin)
wcdb_exportToXML(allTableNames, allRowNames)
