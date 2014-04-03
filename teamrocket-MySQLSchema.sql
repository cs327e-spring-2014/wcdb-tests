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
-- Database: `cs327e_ksombra`
--
CREATE DATABASE IF NOT EXISTS `cs327e_ksombra` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `cs327e_ksombra`;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `citation`
--
 
DROP TABLE IF EXISTS `Citations`;
CREATE TABLE IF NOT EXISTS `Citations` (
  `citationId` bigint(20) unsigned NOT NULL,
  `citation` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `contactinfos`
--
 
DROP TABLE IF EXISTS `ContactInfos`;
CREATE TABLE IF NOT EXISTS `ContactInfos` (
  `contactInfoId` bigint(20) unsigned NOT NULL,
  `phoneNumber` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `emailAddress` varchar(75) COLLATE utf8_unicode_ci DEFAULT NULL,
  `facebookUrlId` bigint(20) unsigned DEFAULT NULL,
  `twitterUrlId` bigint(20) unsigned DEFAULT NULL,
  `websiteUrlId` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`contactInfoId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `crises`
--
 
DROP TABLE IF EXISTS `Crises`;
CREATE TABLE IF NOT EXISTS `Crises` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;
 

-- --------------------------------------------------------

-- Table Structure for CrisisKinds

DROP TABLE IF EXISTS `CrisisKinds`;
CREATE TABLE IF NOT EXISTS `CrisisKinds` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `kind` enum('Natural Disaster','War / Conflict','Act of Terrorism','Human Error Distaster','Assassination / Shooting') COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY(`crisisId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ;

-- --------------------------------------------------------

-- Table Structure for OrgKinds

DROP TABLE IF EXISTS `OrgKinds`;
CREATE TABLE IF NOT EXISTS `CrisisKinds` (
  `orgId` bigint(20) unsigned NOT NULL,
  `kind` enum('Government Agency','Military Force','Intergovernmental Agency','Intergovernmental Public Health Agency','Nonprofit / Humanitarian Organization') COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY(`orgId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ;

-- --------------------------------------------------------

-- Table Structure for PersonKinds

DROP TABLE IF EXISTS `PersonKinds`;
CREATE TABLE IF NOT EXISTS `PersonKinds` (
  `personId` bigint(20) unsigned NOT NULL,
  `kind` enum('Celebrity','Actor / Actress','Musician','Politician','President','CEO','Humanitarian','Perpetrator') COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY(`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ;


-- --------------------------------------------------------
 
--
-- Table structure for table `crisiscitations`
--
 
DROP TABLE IF EXISTS `CrisisCitations`;
CREATE TABLE IF NOT EXISTS `CrisisCitations` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `citationId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`,`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `crisisorgs`
--
 
DROP TABLE IF EXISTS `CrisisOrgs`;
CREATE TABLE IF NOT EXISTS `CrisisOrgs` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `orgId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`,`orgId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `crisispeople`
--
 
DROP TABLE IF EXISTS `CrisisPeople`;
CREATE TABLE IF NOT EXISTS `CrisisPeople` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `personId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`,`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `crisisresources`
--
 
DROP TABLE IF EXISTS `CrisisResources`;
CREATE TABLE IF NOT EXISTS `CrisisResources` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `resourceId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`,`resourceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `crisisurls`
--
 
DROP TABLE IF EXISTS `CrisisUrls`;
CREATE TABLE IF NOT EXISTS `CrisisUrls` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `urlId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`,`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `crisiswaystohelp`
--
 
DROP TABLE IF EXISTS `CrisisWaysToHelp`;
CREATE TABLE IF NOT EXISTS `CrisisWaysToHelp` (
  `crisisId` bigint(20) unsigned NOT NULL,
  `helpId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`crisisId`,`helpId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `orgcitations`
--
 
DROP TABLE IF EXISTS `OrgCitations`;
CREATE TABLE IF NOT EXISTS `OrgCitations` (
  `orgId` bigint(20) unsigned NOT NULL,
  `citationId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`orgId`,`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `orgcontactinfos`
--
 
DROP TABLE IF EXISTS `OrgContactInfos`;
CREATE TABLE IF NOT EXISTS `OrgContactInfos` (
  `orgId` bigint(20) unsigned NOT NULL,
  `contactId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`orgId`,`contactId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `orgpeople`
--
 
DROP TABLE IF EXISTS `OrgPeople`;
CREATE TABLE IF NOT EXISTS `OrgPeople` (
  `orgId` bigint(20) unsigned NOT NULL,
  `personId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`orgId`,`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `orgs`
--
 
DROP TABLE IF EXISTS `Orgs`;
CREATE TABLE IF NOT EXISTS `Orgs` (
  `orgId` bigint(20) unsigned NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `orgurls`
--
 
DROP TABLE IF EXISTS `OrgUrls`;
CREATE TABLE IF NOT EXISTS `OrgUrls` (
  `orgId` bigint(20) unsigned NOT NULL,
  `urlId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`orgId`,`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `people`
--
 
DROP TABLE IF EXISTS `People`;
CREATE TABLE IF NOT EXISTS `People` (
  `personId` bigint(20) unsigned DEFAULT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `streetAddress` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `stateOrProvince` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `postalCode` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `personcitations`
--
 
DROP TABLE IF EXISTS `PersonCitations`;
CREATE TABLE IF NOT EXISTS `PersonCitations` (
  `personId` bigint(20) unsigned NOT NULL,
  `citationId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`personId`,`citationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `personurls`
--
 
DROP TABLE IF EXISTS `PersonUrls`;
CREATE TABLE IF NOT EXISTS `PersonUrls` (
  `personId` bigint(20) unsigned NOT NULL,
  `urlId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`personId`,`urlId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `resources`
--
 
DROP TABLE IF EXISTS `Resources`;
CREATE TABLE IF NOT EXISTS `Resources` (
  `resourceId` bigint(20) unsigned NOT NULL,
  `resource` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`resourceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `urls`
--
 
DROP TABLE IF EXISTS `Urls`;
CREATE TABLE IF NOT EXISTS `Urls` (
  `urlId` int(11) NOT NULL,
  `type` enum('Image','Video','Map','SocialNetwork','Website','ExternalLink') COLLATE utf8_unicode_ci NOT NULL,
  `urlAddress` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
-- --------------------------------------------------------
 
--
-- Table structure for table `waystohelp`
--
 
DROP TABLE IF EXISTS `WaysToHelp`;
CREATE TABLE IF NOT EXISTS `WaysToHelp` (
  `helpId` bigint(20) unsigned NOT NULL,
  `wayToHelp` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`helpId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
 
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
