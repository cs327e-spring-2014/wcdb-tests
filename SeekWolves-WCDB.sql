create table crises (
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	crisisId TEXT,
	name TEXT,
	kind TEXT,
	streetAddress TEXT,
	city TEXT,
	stateOrProvince TEXT,
	postalCode TEXT,
	country TEXT,
	dateAndTime TEXT,
	fatalities BIGINT,
	injuries BIGINT,
	populationIll BIGINT,
	populationDisplaced TEXT,
	environmentalImpact TEXT,
	politicalChanges TEXT,
	culturalChanges TEXT,
	jobsLost BIGINT,
	damageInUSD BIGINT,
	reparationCost BIGINT,
	regulatoryChanges TEXT,
	PRIMARY KEY (id) );

 create table orgs(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	orgId TEXT,
	name TEXT,
	kind TEXT,
	streetAddress TEXT,
	city TEXT,
	stateOrProvince TEXT,
	postalCode TEXT,
	country TEXT,
	foundingMission TEXT,
	dateFounded DATE,
	dateAbolished DATE,
	majorEvents TEXT,
	PRIMARY KEY (id) );

 create table people(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	personId TEXT,
	name TEXT,
	kind TEXT,
	streetAddress TEXT,
	city TEXT,
	stateOrProvince TEXT,
	postalCode TEXT,
	country TEXT,
	PRIMARY KEY (id) );

 create table resources(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	resourceId TEXT,
	resource TEXT,
	PRIMARY KEY (id));

 create table crisisResources(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	crisisId TEXT,
	resourceId TEXT,
	PRIMARY KEY (id));

create table waysToHelp(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	helpId TEXT,
	wayToHelp TEXT,
	PRIMARY KEY (id) );

create table crisisWaysToHelp(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	crisisId TEXT,
	helpId TEXT,
	PRIMARY KEY (id) );

create table contactInfos(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	contactInfoId TEXT,
	phoneNumber TEXT,
	emailAddress TEXT,
	facebookUrlId TEXT,
	twitterUrlId TEXT,
	websiteUrlId TEXT,
	PRIMARY KEY (id) );

create table orgContactInfos(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	orgId TEXT,
	contactInfoId TEXT,
	PRIMARY KEY (id) );

create table citations(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	citationId TEXT,
	citation TEXT,
	PRIMARY KEY (id) );

create table crisisCitations(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	citationId TEXT,
	crisisId TEXT,
	PRIMARY KEY (id) );

create table orgCitations(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	orgId TEXT,
	citationId TEXT,
	PRIMARY KEY (id) );

create table personCitations(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	personId TEXT,
	citationId TEXT,
	PRIMARY KEY (id) );

create table urls(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	urlId TEXT,
	type TEXT,
	urlAddress TEXT,
	PRIMARY KEY (id) );

create table crisisUrls(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	crisisId TEXT,
	urlId TEXT,
	PRIMARY KEY (id) );

create table orgUrls(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	orgId TEXT,
	urlId TEXT,
	PRIMARY KEY (id) );

create table personUrls(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	personId TEXT,
	urlId TEXT,
	PRIMARY KEY (id) );

create table crisisOrgs(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	crisisId TEXT,
	orgId TEXT,
	PRIMARY KEY (id) );

create table crisisPeople(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	crisisId TEXT,
	personId TEXT,
	PRIMARY KEY (id) );

create table orgPeople(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	orgId TEXT,
	personId TEXT,
	PRIMARY KEY (id) );
