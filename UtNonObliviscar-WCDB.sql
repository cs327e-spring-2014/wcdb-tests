create table Crises (
    crisisID varchar(7),
    name text,
    kind enum('Natural Disaster','War / Conflict','Act of Terrorism','Human Error Disaster','Assassination / Shooting'),
    streetAddress text,
    city text,
    stateOrProvince text,
    postalCode text,
    country text,
    dateAndTime text,
    fatalities bigint,
    injuries bigint,
    populationIll bigint,
    populationDisplaced bigint,
    environmentalImpact text,
    politicalChanges text,
    culturalChanges text,
    jobsLost bigint,
    damageInUSD bigint,
    reparationCost bigint,
    regulatoryChanges text,
    primary key (crisisID));

create table Orgs (
    orgID varchar(7),
    name text,
    kind enum('Government Agency','Military Force','Intergovernmental Agency','Intergovernmental Public Healthy Agency','Nonprofit / Humanitarian Organization'),
    streetAddress text,
    city text,
    stateOrProvince text,
    postalCode text,
    country text,
    foundingMission text,
    dateFounded text,
    dateAbolished text,
    majorEvents text,
    primary key (orgID));

create table People (
    personID varchar(7),
    name text,
    kind enum('Celebrity','Actor / Actress','Musician','Politician','President','CEO','Humanitarian','Perpetrator'),
    streetAddress text,
    city text,
    stateOrProvince text,
    postalCode text,
    country text,
    primary key (personID));

create table Resources (
    resourceID varchar(7),
    resource text,
    primary key (resourceID));

create table WaysToHelp (
    helpID varchar(7),
    wayToHelp text,
    primary key (helpID));

create table ContactInfos (
    contactInfoID varchar(7),
    phoneNumber text,
    emailAddress text,
    facebookUrlID text,
    twitterUrlID text,
    websiteUrlID text,
    primary key (contactInfoID));

create table Citations (
    citationID varchar(7),
    citation text,
    primary key (citationID));

create table Urls (
    urlID varchar(7),
    type enum('Image','Video','Map','SocialNetwork','Website','ExternalLink'),
    urlAddress text,
    primary key(urlID));

create table CrisisResources(
    crisisID varchar(7),
    resourceID varchar(7));

create table CrisisWaysToHelp(
    crisisID varchar(7),
    helpID varchar(7));

create table OrgContactInfos(
    orgID varchar(7),
    contactInfoID varchar(7));

create table CrisisCitations(
    citationID varchar(7),
    crisisID varchar(7));

create table OrgCitations(
    orgID varchar(7),
    citationID varchar(7));

create table PersonCitations(
    personID varchar(7),
    citationID varchar(7));

create table CrisisUrls(
    crisisID varchar(7),
    urlID varchar(7));

create table OrgUrls(
    orgID varchar(7),
    urlID varchar(7));

create table PersonUrls(
    personID varchar(7),
    urlID varchar(7));

create table CrisisOrgs(
    crisisID varchar(7),
    orgID varchar(7));

create table CrisisPeople(
    crisisID varchar(7),
    personID varchar(7));

create table OrgPeople(
    orgID varchar(7),
    personID varchar(7));






