use cs327e_wigu;

SELECT "============BashKetchum Queries===========";

SELECT "Of the people classified as presidents, how many natural disasters were each of them connected to?";
SELECT P.name AS PeopleName, COUNT(*)
    FROM People AS P
    INNER JOIN CrisisPeople USING (personId)
    INNER JOIN Crises AS C USING (crisisId)
    WHERE P.kind = 'President' AND C.kind = 'Natural Disaster'
    GROUP BY P.name;
SELECT "";

SELECT "Which organizations were involved in crises that occurred outside of the country its HQs are based in?";
SELECT DISTINCT O.name AS OrgName
    FROM Orgs AS O
    INNER JOIN CrisisOrgs USING (orgId)
    INNER JOIN Crises AS C USING (crisisId)
    WHERE O.country != C.country;
SELECT "";

SELECT "What was the average cost damage in USD done by crises that caused over 1000 fatalities?";
SELECT AVG(damageInUSD)
    FROM Crises
    WHERE fatalities > 1000;
SELECT "";

SELECT "How many natural disasters had over 500 fatalities and costed over 10 billion dollars?";
SELECT COUNT(*)
    FROM Crises
    WHERE kind = 'Natural Disaster' AND fatalities > 500 AND damageInUSD > 10000000000;
SELECT "";

SELECT "Ignoring nulls, what is the total damage cost of disasters in our century?";
SELECT SUM(damageInUSD)
    FROM Crises
    WHERE damageInUSD IS NOT NULL AND dateAndTime >= '2000-01-01 00:00:00';
SELECT "";

SELECT "========Ut Non Obliviscar's Queries=======";

SELECT "Which crisis had the highest reparation cost and what was the crisis?"; 
SELECT name, reparationCost
    FROM Crises
    WHERE reparationCost >= ALL
        (SELECT reparationCost
         FROM Crises);
SELECT "";

SELECT "Which organizations were founded before 1950?";
SELECT name, dateFounded
    FROM Orgs
    WHERE dateFounded <= '1950-01-01 00:00:00';
SELECT "";

SELECT "How many organizations are intergovernmental agencies?";
SELECT COUNT(*) numIntergovernmentalAgencies
    FROM Orgs
    WHERE kind = 'Intergovernmental Agency';
SELECT "";

SELECT "How many people have a Social Network URL?";
SELECT COUNT(DISTINCT personId) AS PersonCount
FROM PersonUrls
WHERE urlId IN
    (SELECT urlId
     FROM Urls
     WHERE Urls.type = 'SocialNetwork');
SELECT "";

SELECT "In what year did the most crises occur?";
SELECT crisisYear, R.yearCount
FROM (SELECT COUNT(*) AS yearCount, YEAR(dateAndTime) AS crisisYear
      FROM Crises
      GROUP BY crisisYear) AS R
WHERE R.yearCount >= ALL(SELECT COUNT(*)
                         FROM Crises
                         GROUP BY YEAR(dateAndTime));
SELECT "";

SELECT "==========GottaGitThat's Queries==========";
SELECT "";

SELECT "Which crisis had the most combined fatalities and injuries?";
SELECT name
    FROM Crises
    WHERE (injuries + fatalities) >= ALL
    (SELECT (injuries + fatalities) FROM Crises);
SELECT "";

SELECT "How many crises have occurred in the 21st century?";
SELECT COUNT(*)
    FROM Crises
    WHERE dateAndTime >= '2000-01-01 00:00:00' AND dateAndTime <= '2099-12-31 11:59:59';
SELECT "";

SELECT "Which country has the most crises?";
SELECT country, COUNT(*) AS crisisCount
FROM Crises
GROUP BY country
HAVING COUNT(*) >= ALL(SELECT COUNT(*)
                          FROM Crises
                          GROUP BY country);
SELECT "";

SELECT "How many organizations are related to crises that had 0 damage in USD?";
SELECT COUNT(*) AS org_count
FROM CrisisOrgs
INNER JOIN Crises USING (crisisId)
WHERE damageInUSD = 0;
SELECT "";

SELECT "Which people are involved in 2 or more crises?";
SELECT R.name AS peopleName, COUNT(*) AS pCount
FROM People AS R
INNER JOIN CrisisPeople USING (personId)
GROUP BY personId
HAVING COUNT(*) >= 2;
SELECT "";

SELECT "===========Brigadeiros===========";
SELECT ""; 

SELECT "What organizations don't exist anymore?";
SELECT name
    FROM Orgs
    WHERE dateAbolished IS NOT NULL;
SELECT "";

SELECT "What are the 5 most recent crises?";
SELECT name, dateAndTime
   FROM Crises
   ORDER BY dateAndTime desc
   LIMIT 5;
SELECT "";

SELECT "What are the crises with the most amount of resources?";
SELECT name, resourceCount
FROM Crises
INNER JOIN
(SELECT crisisId, COUNT(*) AS resourceCount
 FROM CrisisResources
 GROUP BY crisisId
 HAVING COUNT(*) >= ALL(SELECT COUNT(*)
                        FROM CrisisResources
                        GROUP BY crisisId)
) AS T
USING (crisisId);
SELECT "";

SELECT "What crises expend more money on reconstruction than in the damage done?";
SELECT name 
    FROM Crises
    WHERE reparationCost IS NOT NULL AND reparationCost > damageInUSD;
SELECT "";

SELECT "What's the most common kind of person?";
SELECT kind, COUNT(*) AS kind_count
    FROM People
    GROUP BY kind
    HAVING COUNT(*) >= ALL
        (SELECT COUNT(*)
        FROM People
        GROUP BY kind);
SELECT "";

SELECT "==========Team Rocket's Queries==========";
SELECT "";

SELECT "Which crises occur within the United States?";
SELECT name
    FROM Crises
    WHERE country = "USA" OR country = "U.S.A." OR country = "United States"
    OR country = "U.S." OR country = "United States of America";
SELECT "";

SELECT "What is the total cost in damages of United States crises?";
SELECT sum(damageInUSD) 
    FROM Crises
    WHERE country = "USA" OR country = "U.S.A." OR country = "United States"
    OR country = "U.S." OR country = "United States of America";
SELECT "";

SELECT "Are there more organizations based outside of the United States (within this database) than American organizations?";
SELECT
IF(
(SELECT COUNT(*) AS outsideCount
 FROM Orgs
 WHERE country not in ('United States', 'USA', 'U.S.')) >

(SELECT COUNT(*) AS insideCount
 FROM Orgs
 WHERE country in ('United States', 'USA', 'U.S.')), 'True', 'False');
SELECT "";

SELECT "What is the least common kind of person?";
SELECT kind, COUNT(*) AS kind_count 
    FROM People
    GROUP BY kind
    HAVING COUNT(*) <= ALL
        (SELECT COUNT(*)
        FROM People
        GROUP BY kind);
SELECT "";

SELECT "What is the least common kind of crisis?";
SELECT kind, COUNT(*) AS kind_count 
    FROM Crises
    GROUP BY kind
    HAVING COUNT(*) <= ALL
        (SELECT COUNT(*)
        FROM Crises
        GROUP BY kind);
SELECT "";


SELECT "==========SeekWolves Queries==========";
SELECT "";


SELECT "What is the location of each of the crisis (city and country)";
SELECT city, country FROM Crises;
SELECT "";

SELECT "Which crises occurred outside US?";
SELECT name FROM Crises
  WHERE country not in ('United States', 'U.S.', 'United States of America', 'USA');
SELECT "";

SELECT "Which crises relief effort was American Red Cross part of?";
SELECT Crises.name
FROM CrisisOrgs
INNER JOIN Crises USING (crisisId)
INNER JOIN Orgs USING (orgId)
WHERE Orgs.name = 'American Red Cross';
SELECT "";

SELECT "Which presidents were related to the crises?";
SELECT name
FROM People
WHERE kind = 'President';
SELECT "";

SELECT "Which crises had fatalities less than 100?";
SELECT name
FROM Crises
WHERE fatalities < 100;
SELECT "";

SELECT "==========Databosses' Queries==========";
SELECT "";

SELECT "How many crises is President Obama involved in?";
SELECT R.name, count(*) as NumberOfCrisesInvolved
    FROM People as R
    INNER JOIN CrisisPeople USING (personId)
    GROUP BY personId
    HAVING R.name = "President Obama" or R.Name = "Barack Obama" or R.name = "President Barack Obama";
SELECT "";

SELECT "Which Way to Help is most common?";
SELECT WayToHelp, COUNT(*)
    FROM WaysToHelp 
    INNER JOIN CrisisWaysToHelp USING (helpId)
    GROUP BY WayToHelp
    HAVING COUNT(*) >= ALL
        (SELECT COUNT(*)
         FROM WaysToHelp
         INNER JOIN CrisisWaysToHelp USING (helpId)
         GROUP BY wayToHelp);
SELECT "";

SELECT "What country are most of the People in?";
SELECT country, count(*)
    FROM People
    GROUP BY country
    HAVING COUNT(*) >= ALL
        (SELECT COUNT(*) 
         FROM People
         GROUP BY country);
SELECT "";

SELECT "What organizations are involved with the Haiti Earthquake?";
SELECT Orgs.name
    FROM Crises as R
    INNER JOIN CrisisOrgs using (crisisId)
    INNER JOIN Orgs using (orgId) 
    WHERE R.name = "Haiti Earthquake" or R.name = "Haitian Earthquake" or R.name = "Haiti Earthquake (2010)";
SELECT "";

SELECT "How many crises have caused over 1 billion USD in damages?";
SELECT COUNT(*)
    FROM Crises
    WHERE damageInUSD > 1000000000;
SELECT "";

SELECT "=============EDJAKS' Queries==============";
SELECT "";

SELECT"What is the first (earliest) crisis in the database?";
SELECT * 
    FROM Crises
    WHERE dateAndTime <= all
        (SELECT dateAndTime
            FROM Crises);
SELECT "";

SELECT "What is the total number of deaths caused by natural disasters?";
SELECT SUM(fatalities)
    FROM Crises
    WHERE kind = 'Natural Disaster';
SELECT "";

SELECT "Count the number of politicians grouped by country.";
SELECT country, COUNT(*) 
    FROM People
    WHERE kind = 'Politician'
    GROUP BY country;
SELECT "";

SELECT "Count the number of crisis that each organization helped.";
SELECT name, COUNT(*) AS numCrisesHelped
    FROM CrisisOrgs
    INNER JOIN Orgs using (orgId)
    GROUP BY orgId;
SELECT "";

SELECT "What is the most common resource needed?";
SELECT resource
FROM Resources
WHERE resourceId =
    (SELECT resourceId
     FROM (SELECT resourceId, COUNT(*) As resourceCount
           FROM CrisisResources
           GROUP BY resourceId) AS R
     WHERE resourceCount >= (SELECT max(resourceCount)
                             FROM (SELECT resourceId, COUNT(*) As resourceCount
                                   FROM CrisisResources
                                   GROUP BY resourceId) AS S));

