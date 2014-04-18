
use cs327e_ksombra;
drop table if exists Citations;
drop table if exists ContactInfos;
drop table if exists Crises;
drop table if exists CrisisCitations;
drop table if exists CrisisOrgs;
drop table if exists CrisisPeople;
drop table if exists CrisisResources;
drop table if exists CrisisWaysToHelp;
drop table if exists CrisisUrls;
drop table if exists Orgs;
drop table if exists OrgCitations;
drop table if exists OrgContactInfos;
drop table if exists OrgPeople;
drop table if exists OrgUrls;
drop table if exists PersonCitations;
drop table if exists PersonUrls;
drop table if exists Resources;
drop table if exists Urls;
drop table if exists WaysToHelp;
drop table if exists People;

/* -------------------------------------------------
       Create Tables
-----------------------------------------------------*/

create table Crises (
	crisisID            INT      not null,
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
	orgID               INT     not null,
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
	personID            INT     not null,
	name	            TEXT     not null,
	kind                TEXT     not null,
	streetAddress       TEXT,
	postalCode          BIGINT,
	country	            TEXT,
	Primary Key (personID) );

create table Resources (
	resourceID	    INT     not null,
	resource	    TEXT,
	Primary Key (resourceID) );

create table CrisisResources (
	crisisID	    INT,
	resourceID          TEXT );

create table WaysToHelp (
	helpID 	            INT,
	waytohelp	    TEXT,
	Primary Key (helpID)  );

create table CrisisWaysToHelp (
	crisisID            INT,
	helpID              TEXT );

create table ContactInfos (
	contactInfoID       INT,
	phoneNumber         VARCHAR(15),
	emailAddress        TEXT,
	facebookURLID       TEXT,
	twitterURLID        TEXT,
	websiteURLID        TEXT,
	Primary Key (contactInfoID) );

create table OrgContactInfos (
	orgID	            INT,
	contactInfoID       TEXT );

create table Citations (
	citationID          INT,
	citation	    TEXT,
	Primary Key (citationID) );

create table CrisisCitations (
	citationID          INT,
	crisisID	    INT );

create table OrgCitations (
	orgID	            INT,
	citationID          INT );

create table PersonCitations (
	personID	    INT,
	citationID	    INT );

create table Urls (
	urlID	            INT,
	type                TEXT,
	urlAddress          TEXT );

create table CrisisUrls (
	crisisID	    INT,
	urlID	            INT );

create table OrgUrls (
	orgID	            INT,
	urlID 	            INT );

create table PersonUrls (
	personID 	    INT,
	urlID	            INT );

create table CrisisOrgs (
	crisisID	    INT,
	orgID               INT );

create table CrisisPeople (
	crisisID	    INT,
	personID	    INT );

create table OrgPeople (
	orgID	            INT,
	personID	    INT );


