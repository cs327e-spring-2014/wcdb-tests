use cs327e_joshen;

drop table if exists CrisisOrgs;
drop table if exists CrisisPeople;
drop table if exists OrgPeople;
drop table if exists CrisisCitations;
drop table if exists OrgCitations;
drop table if exists PersonCitations;
drop table if exists CrisisResources;
drop table if exists CrisisWaysToHelp;
drop table if exists OrgContactInfos;
drop table if exists CrisisUrls;
drop table if exists OrgUrls;
drop table if exists PersonUrls;
drop table if exists Crises;
drop table if exists Orgs;
drop table if exists People;
drop table if exists Resources;  
drop table if exists WaysToHelp; 
drop table if exists ContactInfos;  
drop table if exists Citations;
drop table if exists Urls;

CREATE TABLE Crises (
            crisisId varchar(10) COLLATE utf8_unicode_ci NOT NULL,
            name varchar(100) COLLATE utf8_unicode_ci NOT NULL,
            kind enum('Natural Disaster','War / Conflict','Act of Terrorism','Human Error Disaster','Assassination / Shooting') COLLATE utf8_unicode_ci NOT NULL,
            streetAddress varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
            city varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
            stateOrProvince varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
            country varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
            dateAndTime datetime NOT NULL,
            fatalities bigint(12) unsigned NULL,
            injuries bigint(12) unsigned NULL,
            populationIll bigint(12) unsigned NULL,
            populationDisplaced bigint(12) unsigned NULL,
            environmentalImpact text COLLATE utf8_unicode_ci DEFAULT NULL,
            politicalChanges text COLLATE utf8_unicode_ci DEFAULT NULL,
            culturalChanges text COLLATE utf8_unicode_ci DEFAULT NULL,
            jobsLost bigint(12) unsigned NULL,
            damageInUSD bigint(12) unsigned NULL,
            reparationCost bigint(12) unsigned NULL,
            regulatoryChanges text COLLATE utf8_unicode_ci DEFAULT NULL,
            PRIMARY KEY (crisisId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE Orgs (
            orgId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            name varchar(100) COLLATE utf8_unicode_ci NOT NULL,
            kind enum('Corporation','Government Agency','Military Force','Intergovernmental Agency','Intergovernmental Public Health Agency', 'Nonprofit / Humanitarian Organization') COLLATE utf8_unicode_ci NOT NULL,
            streetAddress varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
            city varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
            stateOrProvince varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
            postalCode varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
            country varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
            foundingMission text COLLATE utf8_unicode_ci DEFAULT NULL,
            datefounded datetime DEFAULT NULL,
            majorEvents text COLLATE utf8_unicode_ci DEFAULT NULL,
            PRIMARY KEY (orgId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE People (
            personId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            name varchar(100) COLLATE utf8_unicode_ci NOT NULL,
            kind enum('President','Celebrity','Actor/Actress','Musician','Politician', 'CEO','Humanitarian','Perpetrator','Regular Worker') COLLATE utf8_unicode_ci NOT NULL,
            streetAddress varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
            city varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
            stateOrProvince varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
            postalCode varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
            country varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
            PRIMARY KEY (personId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE Resources (
            resourceId int(6) unsigned NOT NULL AUTO_INCREMENT,
            resource text COLLATE utf8_unicode_ci NOT NULL,
            PRIMARY KEY (resourceId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE CrisisResources (
            crisisId varchar(10) COLLATE utf8_unicode_ci NOT NULL,
            resourceId int(6) unsigned NOT NULL,
            FOREIGN KEY (crisisId) REFERENCES Crises(crisisId),
            FOREIGN KEY (resourceId) REFERENCES Resources(resourceId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE WaysToHelp (
            helpId int(6) unsigned NOT NULL AUTO_INCREMENT,
            wayToHelp text COLLATE utf8_unicode_ci NOT NULL,
            PRIMARY KEY (helpId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE CrisisWaysToHelp (
            crisisId varchar(10) COLLATE utf8_unicode_ci NOT NULL,
            helpId int(6) unsigned NOT NULL,
            FOREIGN KEY (crisisId) REFERENCES Crises(crisisId),
            FOREIGN KEY (helpId) REFERENCES WaysToHelp(helpId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE ContactInfos (
            contactInfoId int(6) unsigned NOT NULL AUTO_INCREMENT,
            phoneNumber varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
            emailAddress varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
            facebookUrlId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            twitterUrlId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            websiteUrlId  varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            PRIMARY KEY (contactInfoId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE OrgContactInfos (
            orgId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            contactInfoId int(6) unsigned NOT NULL,
            FOREIGN KEY (orgId) REFERENCES Orgs(orgId),
            FOREIGN KEY (contactInfoId) REFERENCES ContactInfos(contactInfoId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE Citations (
            citationId int(6) unsigned NOT NULL AUTO_INCREMENT,
            citation text COLLATE utf8_unicode_ci NOT NULL,
            PRIMARY KEY (citationId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE CrisisCitations (
            citationId int(6) unsigned NOT NULL,
            crisisId varchar(20) COLLATE utf8_unicode_ci NOT NULL,    
            FOREIGN KEY (citationId) REFERENCES Citations(citationId),
            FOREIGN KEY (crisisId) REFERENCES Crises(crisisId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE OrgCitations (
            orgId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            citationId int(6) unsigned NOT NULL,
            FOREIGN KEY (orgId) REFERENCES Orgs(orgId),
            FOREIGN KEY (citationId) REFERENCES Citations(citationId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE PersonCitations (
            personId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            citationId int(6) unsigned NOT NULL,
            FOREIGN KEY (personId) REFERENCES People(personId),
            FOREIGN KEY (citationId) REFERENCES Citations(citationId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE Urls (
            urlId int(6) unsigned NOT NULL AUTO_INCREMENT,
            type enum('Image','Video','Map','SocialNetwork','Website','ExternalLink') COLLATE utf8_unicode_ci NOT NULL,
            urlAddress text COLLATE utf8_unicode_ci NOT NULL,
            PRIMARY KEY (urlId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE CrisisUrls (
            crisisId varchar(10) COLLATE utf8_unicode_ci NOT NULL,
            urlId int(6) unsigned NOT NULL,
            FOREIGN KEY (crisisId) REFERENCES Crises(crisisId),
            FOREIGN KEY (urlId) REFERENCES Urls(urlId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE OrgUrls (
            orgId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            urlId int(6) unsigned NOT NULL,
            FOREIGN KEY (orgId) REFERENCES Orgs(orgId),
            FOREIGN KEY (urlId) REFERENCES Urls(urlId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE PersonUrls (
            personId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            urlId int(6) unsigned NOT NULL,
            FOREIGN KEY (personId) REFERENCES People(personId),
            FOREIGN KEY (urlId) REFERENCES Urls(urlId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE CrisisOrgs (
            crisisId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            orgId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            FOREIGN KEY (crisisId) REFERENCES Crises(crisisId),
            FOREIGN KEY (orgId) REFERENCES Orgs(orgId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE CrisisPeople (
            crisisId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            personId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            FOREIGN KEY (crisisId) REFERENCES Crises(crisisId),
            FOREIGN KEY (personId) REFERENCES People(personId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE OrgPeople (
            orgId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            personId varchar(20) COLLATE utf8_unicode_ci NOT NULL,
            FOREIGN KEY (orgId) REFERENCES Orgs(orgId),
            FOREIGN KEY (personId) REFERENCES People(personId) 
            )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;





































