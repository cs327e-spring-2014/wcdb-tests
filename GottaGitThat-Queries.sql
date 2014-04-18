/*
use cs327e_joshen;
*/

/* -----------------------------------------------------------------------
How to execute this file: mysql -v -H < Queries.sql > Queries.html

GottaGitThat Questions

1) Which crisis had the most combined fatalities and injuries?
2) How many crises have occurred in the 21st century?
3) Which country has the most crises?
4) How many organizations had crises that had 0 damage in USD
5) How many people are involved in 2 or more crises
*/

select "Which crisis had the most combined fatalities and injuries?";
select name, (fatalities + injuries) as Total from Crises order by Total desc limit 1;
# ------------------------------------------------------------------------

select "How many crises have occurred in the 21st century?";
select count(Name) AS Crises_Count from Crises where dateAndTime >= '2000-01-01 00:00:00';
# ------------------------------------------------------------------------

select "Which country has the most crises?";
select count(country) as Count, country from Crises group by country order by count desc limit 1;
# ------------------------------------------------------------------------

select "How many organizations had crises that had 0 damage in USD?";
select count(distinct O.name) as Org_Name from CrisisOrgs as CO inner join Crises as C on CO.crisisId=C.crisisId inner join Orgs as O on CO.orgId=O.orgId where C.damageinUSD = 0;
# ------------------------------------------------------------------------

select "How many people are involved in 2 or more crises?";
select P.name, count(P.name) as Count  from CrisisPeople as CP inner join People as P on CP.personId=P.personId inner join Crises as C on CP.crisisId=C.crisisId group by P.name having Count >= 2;  


/* -----------------------------------------------------------------------
Brigadeiros

1) What organizations don't exist anymore?
2) What are the 5 most recent crises?
3) What are the crises with the most amount of resources?
4) What crises expend more money on reconstruction than in the damage done?
5) What's the most common kind of person?
*/

select "What are the 5 most recent crises?";
Select name, dateAndTime from Crises order by dateAndTime desc limit 5;
# ------------------------------------------------------------------------

select "What are the crises with the most amount of resources?";
select count(distinct R.resource) as Resource_Count, C.name from CrisisResources as CR inner join Crises as C on CR.crisisId = C.crisisId inner join Resources as R on CR.resourceId=R.resourceId group by C.name order by Resource_Count desc limit 1;
# ------------------------------------------------------------------------

select "What crises expend more money on reconstruction than in the damage done?";
select name, damageInUSD, reparationCost from Crises where reparationCost > damageInUSD;
# ------------------------------------------------------------------------

select "What is the most common kind of person?";
select count(name) as Count, kind from People group by kind order by Count desc limit 1;

/* -----------------------------------------------------------------------
Ut Non Obliviscar's Queries:

1. Which crisis had the highest reparation cost and what was the crisis?
2. Which organizations were founded before 1950?
3. How many organizations are intergovernmental agencies?
4. How many people have a Social Network URL?
5. In what year did the most crises occur?
*/

select "Which crisis had the highest reparation cost and what was the crisis?";
select name, reparationCost from Crises order by reparationCost desc limit 1;
# ------------------------------------------------------------------------

select "Which organizations were founded before 1950?";
select name, datefounded from Orgs where datefounded <= '1950-01-01 00:00:00';
# ------------------------------------------------------------------------

select "How many organizations are intergovernmental agencies?";
select count(name) as Count, kind from Orgs where kind = 4;
# ------------------------------------------------------------------------

select "How many people have a Social Network URL?";
select count(distinct P.name) as Count, U.type from PersonUrls as PU inner join People as P on PU.personId = P.personId inner join Urls as U on PU.urlId = U.urlId where type=4;
# ------------------------------------------------------------------------

select "In what year did the most crises occur?";
select count(name) as Crisis_Count, Extract(Year from dateAndTime) as Year from Crises group by Year order by Crisis_Count desc limit 1;

/* -----------------------------------------------------------------------
Team Rocket's Queries:

1. Which crises occur within the United States?
2. What is the total cost in damages of United States crises?
3. Are there more organizations based outside of the United States (within this database) than American organizations?
4. What is the least common kind of person?
5. What is the least common kind of crisis?
*/

select "Which crises occur within the United States?";
select name, country from Crises where country = 'United States' or country = 'USA' or country= 'US';
# ------------------------------------------------------------------------

select "What is the total cost in damages of United States crises?";
select  country, sum(damageinUSD) as Total_Cost from Crises where country = 'United States' or country = 'USA' or country = 'US';
# ------------------------------------------------------------------------

select "Are there more organizations based outside of the United States (within this database) than American organizations?";
select sum(Count) as OrganizationCount, country as Country from (select count(name) as Count, country from Orgs group by country having country <> 'United States' and country <> 'US' and country <> 'USA' order by substring_index(country,'NULL',1)) as O2 union select sum(Count) as OrganizationCount, country as Country from (select count(name) as Count, country from Orgs group by country having country = 'United States' or country = 'US' or country = 'USA') as O3;
# ------------------------------------------------------------------------

select "What is the least common kind of person?";
select count(name) as Count, kind from People where kind <> "" group by kind order by Count limit 1;
# ------------------------------------------------------------------------

select "What is the least common kind of crisis?";
select count(name) as Count, kind from Crises group by kind order by Count limit 1;

/* -----------------------------------------------------------------------
Databosses' Queries:

1. How many crises is President Obama involved in?
2. Which "Way to Help" is most common?
3. What country are most of the People in?
4. What organizations are involved with the Haiti Earthquake?
5. How many crises have caused over 1 billion USD in damages?
*/

Select "How many crises is President Obama involved in?";
Select count(distinct C.name), P.name from CrisisPeople as CP inner join Crises as C on CP.crisisId=C.crisisId inner join People as P on CP.personId=P.personId where P.name = 'Barack Obama';
# ------------------------------------------------------------------------


select "Which Way To Help Is most common?";
Select distinct W.wayToHelp, count(C.name) as Crisis_Count from CrisisWaysToHelp as CW inner join Crises as C on CW.crisisId = C.crisisId inner join WaysToHelp as W on CW.helpId = W.helpId group by W.wayToHelp order by Crisis_Count desc limit 1;

# ------------------------------------------------------------------------

select "What country are most of the People in?";
select count(name) as Count, country from People group by country order by Count desc limit 1;
# ------------------------------------------------------------------------

select "What organizations are involved with the Haiti Earthquake?";
Select O.name as Org_Name, C.name as Crisis_Name from CrisisOrgs as CO inner join Crises as C on CO.crisisId = C.crisisId inner join Orgs as O on CO.orgId = O.orgId where C.name = 'Haiti Earthquake';
# ------------------------------------------------------------------------

select "How many crises have caused over 1 billion USD in damages?";
select name, damageInUSD from Crises where damageInUSD > 1000000000;

/* -----------------------------------------------------------------------
SeekWolves Queries:

1. What is the location of each of the crisis (city and country)
2. Which crises occurred outside US?
3. Which crises relief effort was American Red Cross part of?
4. Which presidents were related to the crises?
5. Which crises had fatalities less than 100?
*/

select "What is the location of each of the crisis (city and country)";
select name, city, country from Crises;
# ------------------------------------------------------------------------

select "Which crises occurred outside US?";
select name, country from Crises where country <> 'United States' and country <> 'USA' and country <> 'US';
# ------------------------------------------------------------------------

select "Which crises relief effort was American Red Cross part of?";
Select distinct C.name, O.name from CrisisOrgs as CO inner join Crises as C on CO.crisisId = C.crisisId inner join Orgs as O on CO.orgId= O.orgId where O.name = 'American Red Cross';
# ------------------------------------------------------------------------

select "Which presidents were related to the crises?";
Select distinct C.name, P.kind, P.name from CrisisPeople as CP inner join Crises as C on CP.crisisId = C.crisisId inner join People as P on CP.personId = P.personId where P.kind =1;
# ------------------------------------------------------------------------

select "Which crises had fatalities less than 100?";
select name, fatalities from Crises where fatalities < 100;

/* -----------------------------------------------------------------------
BashKetchum:

1. Of the people classified as presidents, how many natural disasters were each of them connected to?
2. Which organizations were involved in crises that occurred outside of the country its HQs are based in?
3. What was the average cost damage in USD done by crises that caused over 1000 fatalities?
4. How many natural disasters had over 500 fatalities and costed over 10 billion dollars?
5. Ignoring nulls, what is the total damage cost of disasters in our century?
*/

select "Of the people classified as presidents, how many natural disasters were each of them connected to?";
Select distinct P.name, P.kind as Person_Kind,C.kind as Crisis_Kind, C.name as Crisis_Name from CrisisPeople as CP inner join Crises as C on CP.crisisId = C.crisisId inner join People as P on CP.personId = P.personId where P.kind =1 and C.kind =1;
# ------------------------------------------------------------------------

select "Which organizations were involved in crises that occurred outside of the country its HQs are based in?";
Select distinct O.name, O.country, C.name, C.country from CrisisOrgs as CO inner join Crises as C on CO.crisisId = C.crisisId inner join Orgs as O on CO.orgId = O.orgId where O.country <> C.country;
# ------------------------------------------------------------------------

select "What was the average cost damage in USD done by crises that caused over 1000 fatalities?";
Select avg(damageinUSD) as Average_Cost from Crises where fatalities > 1000;
# ------------------------------------------------------------------------

select "How many natural disasters had over 500 fatalities and costed over 10 billion dollars?";
select count(name) as Natural_Disaster_Count from Crises where fatalities > 500 and damageinUSD > 10000000000 and kind =1;
# ------------------------------------------------------------------------

select "Ignoring nulls, what is the total damage cost of disasters in our century?";
select sum(damageInUSD) as Total_Damage_Cost from Crises where dateAndTime > '2000-00-00 00:00:00';

/* -----------------------------------------------------------------------
EJADK:

1. What is the first (earliest) crisis in the database?
2. What is the total number of deaths caused by natural disasters?
3. Count the number of politicians grouped by country.
4. Count the number of crisis that each organization helped.
5.What is the most common resource needed?
*/

select "What is the first (earliest) crisis in the database?";
select name, min(dateAndTime) as Date from Crises;
# ------------------------------------------------------------------------

select "What is the total number of deaths caused by natural disasters?";
select sum(fatalities) as Total_Fatalities from Crises where kind =1;
# ------------------------------------------------------------------------

select "Count the number of politicians grouped by country.";
select count(kind) as Number_of_Politicians, country from People where kind = 5 group by country;
# ------------------------------------------------------------------------

select "Count the number of crisis that each organization helped.";
select distinct O.name as Org_Name, count(C.name) as Crisis_Count from CrisisOrgs as CO inner join Crises as C on CO.crisisId = C.crisisId inner join Orgs as O on CO.orgId = O.orgId group by O.name;
# ------------------------------------------------------------------------

select "What is the most common resource needed?";
select count(C.name) as Resource_Count, R.resource from CrisisResources as CR inner join Crises as C on CR.crisisId=C.crisisId inner join Resources as R on CR.resourceId=R.resourceId group by resource order by Resource_Count desc limit 1;

