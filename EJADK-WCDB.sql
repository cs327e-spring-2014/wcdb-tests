SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
 
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

USE `cs327e_awo84`;
 
DROP TABLE IF EXISTS `crises`;
CREATE TABLE IF NOT EXISTS `crises` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `kind` enum('Natural Disaster','War / Conflict','Act of Terrorism','Human Error Disaster','Assassination / Shooting') COLLATE utf8_unicode_ci NOT NULL,
  `streetAddress` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `stateOrProvince` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `postalCode` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dateAndTime` datetime NOT NULL,
  `fatalities` int(11) unsigned DEFAULT NULL,
  `injuries` int(11) unsigned DEFAULT NULL,
  `populationIll` int(11) unsigned DEFAULT NULL,
  `populationDisplaced` int(11) unsigned DEFAULT NULL,
  `environmentalImpact` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `politicalChanges` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `culturalChanges` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `jobsLost` int(11) unsigned DEFAULT NULL,
  `damageInUsd` int(11) unsigned DEFAULT NULL,
  `reparationCost` int(11) unsigned DEFAULT NULL,
  `regulatoryChanges` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`crisisId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
 
DROP TABLE IF EXISTS `orgs`;
CREATE TABLE IF NOT EXISTS `orgs` (
  `orgId` bigint(20) unsigned NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `kind` enum('Government Agency','Military Force','Intergovernmental Agency','Intergovernmental Public Health Agency','Nonprofit / Humanitarian Organization') COLLATE utf8_unicode_ci NOT NULL,
  `streetAddress` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `stateOrProvince` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `postalCode` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `foundingMission` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dateFounded` date DEFAULT NULL,
  `dateAbolished` date DEFAULT NULL,
  `majorEvents` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`orgId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
 
DROP TABLE IF EXISTS `people`;
CREATE TABLE IF NOT EXISTS `people` (
  `personId` bigint(20) unsigned DEFAULT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `kind` enum('Celebrity','Actor / Actress','Musician','Politician','President','CEO','Humanitarian','Perpetrator') COLLATE utf8_unicode_ci NOT NULL,
  `streetAddress` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `stateOrProvince` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `postalCode` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
 
DROP TABLE IF EXISTS `resources`;
CREATE TABLE IF NOT EXISTS `resources` (
  `resourceId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `resource` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`resourceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;
 
 
DROP TABLE IF EXISTS `crisisResources`;
CREATE TABLE IF NOT EXISTS `crisisResources` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `resourceId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`crisisId`) REFERENCES crises(`crisisId`),
  FOREIGN KEY (`resourceId`) REFERENCES resources(`resourceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
 
DROP TABLE IF EXISTS `waysToHelp`;
CREATE TABLE IF NOT EXISTS `waysToHelp` (
  `helpId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `wayToHelp` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`helpId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;
 

DROP TABLE IF EXISTS `crisisWaysToHelp`;
CREATE TABLE IF NOT EXISTS `crisisWaysToHelp` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `helpId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`crisisId`) REFERENCES crises(`crisisId`),
  FOREIGN KEY (`helpId`) REFERENCES waysToHelp(`helpId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
  
DROP TABLE IF EXISTS `contactInfos`;
CREATE TABLE IF NOT EXISTS `contactInfos` (
  `contactInfoId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `phoneNumber` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `emailAddress` varchar(75) COLLATE utf8_unicode_ci DEFAULT NULL,
  `facebookUrlId` bigint(20) unsigned DEFAULT NULL,
  `twitterUrlId` bigint(20) unsigned DEFAULT NULL,
  `websiteUrlId` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`contactInfoId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1;
 
 
DROP TABLE IF EXISTS `orgContactInfos`;
CREATE TABLE IF NOT EXISTS `orgContactInfos` (
  `orgId` bigint(20) unsigned NOT NULL,
  `contactInfoId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`orgId`) REFERENCES orgs(`orgId`),
  FOREIGN KEY (`contactInfoId`) REFERENCES contactInfos(`contactInfoId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
 
DROP TABLE IF EXISTS `citations`;
CREATE TABLE IF NOT EXISTS `citations` (
  `citationId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `citation` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1;
 
DROP TABLE IF EXISTS `crisisCitations`;
CREATE TABLE IF NOT EXISTS `crisisCitations` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `citationId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`crisisId`) REFERENCES crises(`crisisId`),
  FOREIGN KEY (`citationId`) REFERENCES citations(`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
DROP TABLE IF EXISTS `orgCitations`;
CREATE TABLE IF NOT EXISTS `orgCitations` (
  `orgId` bigint(20) unsigned NOT NULL,
  `citationId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`orgId`) REFERENCES orgs(`orgId`),
  FOREIGN KEY (`citationId`) REFERENCES citations(`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
 
DROP TABLE IF EXISTS `personCitations`;
CREATE TABLE IF NOT EXISTS `personCitations` (
  `personId` bigint(20) unsigned NOT NULL,
  `citationId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`personId`) REFERENCES people(`personId`),
  FOREIGN KEY (`citationId`) REFERENCES citations(`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
  
DROP TABLE IF EXISTS `urls`;
CREATE TABLE IF NOT EXISTS `urls` (
  `urlId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `type` enum('Image','Video','Map','SocialNetwork','Website','ExternalLink') COLLATE utf8_unicode_ci NOT NULL,
  `urlAddress` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1;
 
DROP TABLE IF EXISTS `crisisUrls`;
CREATE TABLE IF NOT EXISTS `crisisUrls` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `urlId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`crisisId`) REFERENCES crises(`crisisId`),
  FOREIGN KEY (`urlId`) REFERENCES urls(`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
DROP TABLE IF EXISTS `orgUrls`;
CREATE TABLE IF NOT EXISTS `orgUrls` (
  `orgId` bigint(20) unsigned NOT NULL,
  `urlId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`orgId`) REFERENCES orgs(`orgId`),
  FOREIGN KEY (`urlId`) REFERENCES urls(`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
 
DROP TABLE IF EXISTS `personUrls`;
CREATE TABLE IF NOT EXISTS `personUrls` (
  `personId` bigint(20) unsigned NOT NULL,
  `urlId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`personId`) REFERENCES people(`personId`),
  FOREIGN KEY (`urlId`) REFERENCES urls(`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
 
DROP TABLE IF EXISTS `crisisOrgs`;
CREATE TABLE IF NOT EXISTS `crisisOrgs` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `orgId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`crisisId`) REFERENCES crises(`crisisId`),
  FOREIGN KEY (`orgId`) REFERENCES orgs(`orgId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
 
DROP TABLE IF EXISTS `crisisPeople`;
CREATE TABLE IF NOT EXISTS `crisisPeople` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `personId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`crisisId`) REFERENCES crises(`crisisId`),
  FOREIGN KEY (`personId`) REFERENCES people(`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 

DROP TABLE IF EXISTS `orgPeople`;
CREATE TABLE IF NOT EXISTS `orgPeople` (
  `orgId` bigint(20) unsigned NOT NULL,
  `personId` bigint(20) unsigned NOT NULL,
  FOREIGN KEY (`orgId`) REFERENCES orgs(`orgId`),
  FOREIGN KEY (`personId`) REFERENCES people(`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;