SELECT "GottaGitThat";

SELECT "#1 Which crises had the most combined fatalities and injuries?";
SELECT name, fatalities + injuries
	FROM crises
	ORDER BY (fatalities + injuries) DESC limit 1;
	
SELECT "#2 How many crises have occurred in the 21st century?";
select count(*)
	from crises
	where dateAndTime >= 2000;

select "#3 Which country has the most crises?";
select country, count(*)
    from crises
    group by country
	order by count(*) desc
	limit 1;
	
select "#4 How many organizations are related to crises that had 0 damage in USD?";
SELECT count(distinct O.orgId)
	FROM orgs as O
	INNER JOIN crisisOrgs as CO using (orgId)
	INNER JOIN crises as C using (crisisId)
	WHERE C.damageInUSD = 0;

select "#5 Which people are involved in 2 or more crises?";
select name
	from people inner join crisisPeople using(personId)
	group by name
	having count(*) > 2;

SELECT "Brigaderios";

select "#6 What organizations dont exist anymore?";
select name
	from orgs
	where year(dateAbolished) <= 2014 and dateAbolished != 0000-00-0;
	
select "#7  What are the 5 most recent crises?";
select name
	from crises
	order by dateAndTime desc
	limit 5;
	
select "#8 What are the crises with the most amount of resources?";
SELECT crises.name
	FROM crisisResources
	INNER JOIN resources on (crisisResources.resourceId = resources.Id)
	INNER JOIN crises using (crisisId)
	GROUP BY crisisId 
	ORDER BY count(distinct resources.resource) DESC limit 1;
	
select "#9 What crises expend more money on reconstruction than in the damage done?";
select name
	from crises
	where reparationCost > damageInUSD;

select "#10  Whats the most common kind of person?";
select kind
	from people
	group by kind
	order by count(*) desc
	limit 1;

SELECT "UT Non Obliviscar";

select "#11 Which crises had the highest reparation cost?";
select name
	from crises
	where reparationCost >= all
	(select reparationCost from crises);

select "#12 Which organizations were founded before 1950?";
select name
	from orgs
	where year(dateFounded) <= 1950;
	
select "#13 How many organizations are intergovernmental agencies?";
select count(*)
	from orgs
	where kind = 'Intergovernmental Agency'; 

select "4. How many people have a social network url?";
SELECT count(distinct p.Id)
	FROM urls as u 
	INNER JOIN personUrls as pu on (u.Id = pu.urlId)
	INNER JOIN people as p using (personId)
	WHERE u.type = "SocialNetwork";

SELECT "5. In what year did the most crises occur?";
SELECT year(dateAndTime)
	FROM crises
	GROUP BY year(dateAndTime)
	ORDER BY count(year(dateAndTime)) DESC limit 1;

select "TEAM ROCKET QUERIES";
 
SELECT "1. Which crises occur within the United States?";
select name 
	from crises 
	where country = "USA";

SELECT "2. What is the total cost in damages of United States crises?";
select sum(damageinUSD) 
	from crises 
	where country = "USA";

SELECT "3. Are there more organizations based outside of 
		the United States (within this database) than American organizations?";

select x.num - y.num
from
	(select count(name) as num
	from orgs
	where name !="USA") as x,
	(select count(name) as num
	from orgs
	where name ="USA") as y;
	

SELECT "4. What is the least common kind of person?";
SELECT count(*) as Rows, kind 
	from people 
	group by kind 
	order by Rows asc limit 1; 

SELECT "5. What is the least common kind of crisis?";
select count(*) as Rows, kind 
	from crises 
	group by kind 
	order by Rows asc limit 1; 

SELECT "Databosses' Queries:";
 
SELECT "1. How many crises is President Obama involved in?";
select people.name, count(distinct crisisId) 
	from people 
	inner join crisisPeople on people.personId = crisisPeople.personId 
	where crisisPeople.personId = "PER_001";
 
SELECT "2. Which Way to Help is most common?";
select count(*) as Rows, wayToHelp 
 	from waysToHelp 
 	group by wayToHelp 
 	order by Rows desc limit 1;

SELECT "3. What country are most of the People in?";
SELECT count(*) as Rows, country 
	from people 
	group by country 
	order by Rows desc limit 1; 
 
SELECT "4. What organizations are involved with the Haiti Earthquake?";
select distinct(name) 
	from crisisOrgs 
	inner join orgs on crisisOrgs.orgId = orgs.orgId 
	where crisisOrgs.crisisId = "CRI_001";
 
SELECT "5. How many crises have caused over 1 billion USD in damages?";
select count(*) 
	from crises 
	where damageInUSD > 1000000000;

SELECT "SeekWolves";

SELECT " 1. What is the location of each of the crisis (city and country)? ";
SELECT name, city, country 
	FROM crises;

SELECT "2. Which crises occurred outside USA?";
SELECT name 
	FROM crises 
	WHERE country != "USA";

SELECT "3. Which crises relief effort was American Red Cross part of?";
SELECT distinct(c.name)
	FROM orgs as o
	INNER JOIN crisisOrgs using (orgId)
	INNER JOIN crises as c using (crisisId)
	WHERE o.name = "American Red Cross";

SELECT "4. Which presidents were related to the crises?";
SELECT distinct(p.personId), p.name, c.name 
	FROM people as p
	INNER JOIN crisisPeople using (personId)
	INNER JOIN crises as c using (crisisId)
	WHERE p.kind = "President";

SELECT "5. Which crises had fatalities less than 100?";
SELECT name 
	FROM crises 
	WHERE fatalities <= 100;

SELECT "BashKetchum";

SELECT "1. Of the people classified as presidents, how many natural 
		disasters were each of them connected to?";
SELECT p.name, count(distinct c.crisisId)	
	FROM people as p
	INNER JOIN crisisPeople using (personId)
	INNER JOIN crises as c using (crisisId)
	WHERE p.kind = "President" and c.kind = "Natural Disaster"
	GROUP BY p.name;

SELECT "2. Which organizations were involved in crises that occurred outside of 
    the country its HQs are based in?";
SELECT distinct (o.name)
	FROM orgs as o
	INNER JOIN crisisOrgs using (orgId)
	INNER JOIN crises as c using (crisisId)
	WHERE o.country != c.country;

SELECT "3. What was the average cost damage in USD done by crises that caused over 1000 
    fatalities?";
SELECT avg(damageInUSD) 
	FROM crises 
	WHERE fatalities > 1000;

SELECT "4. How many natural disasters had over 500 fatalities and costed over 
		10 billion dollars?";
SELECT count(*)
	FROM crises
	WHERE kind = "Natural Disaster" AND fatalities > 500 AND damageinUSD > 1000;

SELECT "5. Ignoring nulls, what is the total damage cost of disasters in 
		our century?";
SELECT sum(damageinUSD)
	FROM crises
	WHERE damageinUSD IS NOT NULL AND year(dateAndTime) >= 2000;

SELECT "EDAJK QUERIES";
SELECT "1. What is the first (earliest) crisis in the database?";
SELECT name
	FROM crises
	ORDER BY dateAndTime ASC limit 1;

SELECT "2.What is the total number of deaths caused by natural disasters?";
SELECT sum(fatalities)
	FROM crises
	WHERE kind = "Natural Disaster";

SELECT "3. Count the number of politicians grouped by country.";
SELECT country, count(distinct personId)
	FROM people
	WHERE kind = "Politician"
	GROUP BY country;

SELECT "4. Count the number of crisis that each organization helped.";
SELECT name, count(distinct crisisId)
	FROM orgs 
	INNER JOIN crisisOrgs using (orgId)
	GROUP BY orgId;

SELECT "5. What is the most common resource needed?";
SELECT resources.resource
	FROM crisisResources 
	INNER JOIN resources on (resources.Id = crisisResources.resourceId)
	GROUP BY resources.resource
	ORDER BY count(crisisResources.resourceId) DESC limit 1;



