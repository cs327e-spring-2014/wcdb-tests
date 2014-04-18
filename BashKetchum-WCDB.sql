-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 26, 2014 at 03:08 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cs327e-wcdb`
--

USE `cs327e_wigu`;

-- --------------------------------------------------------

--
-- Table structure for table `crises`
--

DROP TABLE IF EXISTS `OrgPeople`;
DROP TABLE IF EXISTS `CrisisPeople`;
DROP TABLE IF EXISTS `CrisisOrgs`;
DROP TABLE IF EXISTS `PersonUrls`;
DROP TABLE IF EXISTS `OrgUrls`;
DROP TABLE IF EXISTS `CrisisUrls`;
DROP TABLE IF EXISTS `Urls`;
DROP TABLE IF EXISTS `PersonCitations`;
DROP TABLE IF EXISTS `OrgCitations`;
DROP TABLE IF EXISTS `CrisisCitations`;
DROP TABLE IF EXISTS `Citations`;
DROP TABLE IF EXISTS `OrgContactInfos`;
DROP TABLE IF EXISTS `ContactInfos`;
DROP TABLE IF EXISTS `CrisisWaysToHelp`;
DROP TABLE IF EXISTS `WaysToHelp`;
DROP TABLE IF EXISTS `CrisisResources`;
DROP TABLE IF EXISTS `Resources`;
DROP TABLE IF EXISTS `People`;
DROP TABLE IF EXISTS `Orgs`;
DROP TABLE IF EXISTS `Crises`;

CREATE TABLE IF NOT EXISTS `Crises` (
  `crisisId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(70) COLLATE utf8_unicode_ci NOT NULL,
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
  `damageInUSD` bigint(11) unsigned DEFAULT NULL,
  `reparationCost` int(11) unsigned DEFAULT NULL,
  `regulatoryChanges` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`crisisId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `orgs`
--

CREATE TABLE IF NOT EXISTS `Orgs` (
  `orgId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `people`
--

CREATE TABLE IF NOT EXISTS `People` (
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

-- --------------------------------------------------------

--
-- Table structure for table `resources`
--

CREATE TABLE IF NOT EXISTS `Resources` (
  `resourceId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `resource` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`resourceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `crisisresources`
--

CREATE TABLE IF NOT EXISTS `CrisisResources` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `resourceId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`, `resourceId`),
  FOREIGN KEY (`crisisId`) REFERENCES Crises(`crisisId`),
  FOREIGN KEY (`resourceId`) REFERENCES Resources(`resourceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `waystohelp`
--

CREATE TABLE IF NOT EXISTS `WaysToHelp` (
  `helpId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `wayToHelp` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`helpId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `crisiswaystohelp`
--

CREATE TABLE IF NOT EXISTS `CrisisWaysToHelp` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `helpId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`, `helpId`),
  FOREIGN KEY (`crisisId`) REFERENCES Crises(`crisisId`),
  FOREIGN KEY (`helpId`) REFERENCES WaysToHelp(`helpId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `contactinfos`
--

CREATE TABLE IF NOT EXISTS `ContactInfos` (
  `contactInfoId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `phoneNumber` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `emailAddress` varchar(75) COLLATE utf8_unicode_ci DEFAULT NULL,
  `facebookUrlId` bigint(20) unsigned DEFAULT NULL,
  `twitterUrlId` bigint(20) unsigned DEFAULT NULL,
  `websiteUrlId` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`contactInfoId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orgcontactinfos`
--

CREATE TABLE IF NOT EXISTS `OrgContactInfos` (
  `orgId` bigint(20) unsigned NOT NULL,
  `contactInfoId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`orgId`, `contactInfoId`),
  FOREIGN KEY (`orgId`) REFERENCES Orgs(`orgId`),
  FOREIGN KEY (`contactInfoId`) REFERENCES ContactInfos(`contactInfoId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `citation`
--

CREATE TABLE IF NOT EXISTS `Citations` (
  `citationId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `citation` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `crisiscitations`
--

CREATE TABLE IF NOT EXISTS `CrisisCitations` (
  `citationId` bigint(20) unsigned NOT NULL,
  `crisisId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`citationId`, `crisisId`),
  FOREIGN KEY (`citationId`) REFERENCES Citations(`citationId`),
  FOREIGN KEY (`crisisId`) REFERENCES Crises(`crisisId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orgcitations`
--

CREATE TABLE IF NOT EXISTS `OrgCitations` (
  `orgId` bigint(20) unsigned NOT NULL,
  `citationId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`orgId`, `citationId`),
  FOREIGN KEY (`orgId`) REFERENCES Orgs(`orgId`),
  FOREIGN KEY (`citationId`) REFERENCES Citations(`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `personcitations`
--

CREATE TABLE IF NOT EXISTS `PersonCitations` (
  `personId` bigint(20) unsigned NOT NULL,
  `citationId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`personId`, `citationId`),
  FOREIGN KEY (`personId`) REFERENCES People(`personId`),
  FOREIGN KEY (`citationId`) REFERENCES Citations(`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `urls`
--

CREATE TABLE IF NOT EXISTS `Urls` (
  `urlId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `type` enum('Image','Video','Map','SocialNetwork','Website','ExternalLink') COLLATE utf8_unicode_ci NOT NULL,
  `urlAddress` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `crisisurls`
--

CREATE TABLE IF NOT EXISTS `CrisisUrls` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `urlId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`, `urlId`),
  FOREIGN KEY (`crisisId`) REFERENCES Crises(`crisisId`),
  FOREIGN KEY (`urlId`) REFERENCES Urls(`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orgurls`
--

CREATE TABLE IF NOT EXISTS `OrgUrls` (
  `orgId` bigint(20) unsigned NOT NULL,
  `urlId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`orgId`, `urlId`),
  FOREIGN KEY (`orgId`) REFERENCES Orgs(`orgId`),
  FOREIGN KEY (`urlId`) REFERENCES Urls(`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `personurls`
--

CREATE TABLE IF NOT EXISTS `PersonUrls` (
  `personId` bigint(20) unsigned NOT NULL,
  `urlId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`personId`, `urlId`),
  FOREIGN KEY (`personId`) REFERENCES People(`personId`),
  FOREIGN KEY (`urlId`) REFERENCES Urls(`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `crisisorgs`
--

CREATE TABLE IF NOT EXISTS `CrisisOrgs` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `orgId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`, `orgId`),
  FOREIGN KEY (`crisisId`) REFERENCES Crises(`crisisId`),
  FOREIGN KEY (`orgId`) REFERENCES Orgs(`orgId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `crisispeople`
--

CREATE TABLE IF NOT EXISTS `CrisisPeople` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `personId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`, `personId`),
  FOREIGN KEY (`crisisId`) REFERENCES Crises(`crisisId`),
  FOREIGN KEY (`personId`) REFERENCES People(`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orgpeople`
--

CREATE TABLE IF NOT EXISTS `OrgPeople` (
  `orgId` bigint(20) unsigned NOT NULL,
  `personId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`orgId`, `personId`),
  FOREIGN KEY (`orgId`) REFERENCES Orgs(`orgId`),
  FOREIGN KEY (`personId`) REFERENCES People(`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
