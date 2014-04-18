
drop table if exists Crises;
drop table if exists Orgs;
drop table if exists People;

/* -------------------------------------------------
       Create Tables
-----------------------------------------------------*/

create table Crises (
	crisisID            TEXT      not null,
	name                TEXT      not null,
	kind		    TEXT      not null,
	streetAddress       TEXT,
	city                TEXT,
        stateOrProvince     TEXT,
        postalCode          BIGINT,
	country             TEXT,
        dateAndTime         YEAR(4),
        fatalities          BIGINT,
        injuries            BIGINT,
        populationIll       BIGINT,
        populationdisplaced BIGINT,
        environmentalImpact TEXT,
        politicalChanges    TEXT,
        culturalChanges     TEXT,
        jobsLost            BIGINT,
	damageInUSD         BIGINT,
	reparationCost      BIGINT,
	regulatoryChanges   TEXT, 
	Primary Key (crisisID) );

create table Orgs (
	orgID               TEXT     not null,
        name                TEXT     not null,
	kind	            TEXT     not null,
        streetAddress       TEXT,
        city                TEXT,
        stateOrProvince     TEXT,
        postalCode          BIGINT,
        country             TEXT,
        foundingMission     TEXT,
	dateFounded         DATE,
	dateAbolished       DATE,
	majorEvents         TEXT,
	Primary Key (orgID)    );

create table People (
	personID            TEXT     not null,
	name	            TEXT     not null,
	kind                TEXT     not null,
	streetAddress       TEXT,
	postalCode          BIGINT,
	country	            TEXT,
	Primary Key (personID) );

create table resources (
	resourceID	    TEXT     not null,
	resource	    TEXT,
	Primary Key (resourceID) );

create table crisisResources (
	crisisID	    TEXT,
	resourceID          TEXT );

create table waystoHelp (
	helpID 	            TEXT,
	waytohelp	    TEXT,
	Primary Key (helpID)  );

create table crisisWaysToHelp (
	crisisID            TEXT,
	helpID              TEXT );

create table contactInfos (
	contactInfoID       TEXT,
	phoneNumber         VARCHAR,
	emailAddress        TEXT,
	facebookURLID       TEXT,
	twitterURLID        TEXT,
	websiteURLID        TEXT,
	Primary Key (contactInfoID) );

create table orgContactInfos (
	orgID	            TEXT,
	contactInfoID       TEXT );

create table citations (
	citationID          TEXT,
	citation	    TEXT,
	Primary Key (citationID) );

create table crisisCitations (
	citationID          TEXT,
	crisisID	    TEXT );

create table orgCitations (
	orgID	            TEXT,
	citationID          TEXT );

create table personCitations (
	personID	    TEXT,
	citationID	    TEXT );

create table urls (
	urlID	            TEXT,
	type                TEXT,
	urlAddress          TEXT );

create table crisisUrls (
	crisisID	    TEXT,
	urlID	            TEXT );

create table orgUrls (
	orgID	            TEXT,
	urlID 	            TEXT );

create table personUrls (
	personID 	    TEXT,
	urlID	            TEXT );

create table crisisOrgs (
	crisisID	    TEXT,
	orgID               TEXT );

create table crisisPeople (
	crisisID	    TEXT,
	personID	    TEXT );

create table orgPeople (
	orgID	            TEXT,
	personID	    TEXT );


