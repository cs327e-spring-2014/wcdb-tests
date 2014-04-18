--#What is the first (earliest) crisis in the database?--
Select name, dateAndTime
	From crises
	Where dateAndTime <= all
    (Select dateAndTime From crises where year(dateandtime) <> 0000)
    and
    year(dateandtime) <> 0000;
	
--#What is the total number of deaths caused by natural disasters?--
Select sum(fatalities)
	From crises
	Where kind = 'Natural Disaster';
	
--#Count the number of politicians grouped by country?--
Select country, count(*)
	From people 
	Where kind = 'politician' 
	Group by country;

--#Count the number of crises that each organization helped?--
Select name, count(distinct crisisId)
	From crisisOrgs
	inner join orgs using (orgId)
	Group by name;
    
--#What is the most common resource needed?--
Select resource, count(resourceId)
	From resources 
	inner join crisisResources using (resourceId)
	group by resourceId
	order by count(resourceId) desc
	limit 1 ;

--#Which crises had the most combined fatalities and injuries?--
Select name, fatalities + injuries
	From crises
	order by (fatalities + injuries) desc
	limit 1;

--#How many crises have occurred in the 21st century?--
Select count(*)
	From crises
	where dateandTime >= 2000;

--#Which country has the most crises?--
Select country, count(*)
	From crises
	group by country
	order by count(*) desc
	limit 1;

--#How many organizations are related to crises that had 0 damage in USD?--
Select count(distinct O.orgId)
	From orgs as O
	inner join crisisOrgs as CO using(orgId)
	inner join crises as C using (crisisId)
	Where C.damageInUSD = 0;

--#Which people are involved in 2 or more crises?--
Select name
	from people inner join crisisPeople using(personId)
	group by name
	having count(*) > 2;

--#What organizations don't exist anymore?--
Select name
	from orgs
	where year(dateAbolished) <= 2014 and year(dateAbolished) <> 0000;

--#What are the 5 most recent crises?--
Select name
	from crises
	order by dateAndTime desc
	limit 5;

--#What are the crises with the most amount of resources?--
Select crises.name
	from crisisResources
	inner join resources on (crisisResources.resourceId = resources.resourceId)
	inner join crises using (crisisId)
	group by crisisId
	order by count(distinct resources.resource) desc limit 1;

--#What crises expend more money on reconstruction than damage done?--
Select name
	from crises
	where reparationCost > damageInUSD;

--#What's the most common kind of person?--
Select kind
	from people
	group by kind
	order by count(*) desc
	limit 1;

--#Which crises had the highest reparation cost?--
Select name
	from crises
	where reparationCost >= all
	(select reparationCost from crises);

--#Which organizations were founded before 1950?--
Select name
	from orgs
	where year(dateFounded) <= 1950;

--#How many organizations are intergovernmental agencies?--
Select count(*)
	from orgs
	where kind = 'Intergovernmental Agency';

--#How many people have a social network url?--
Select count(distinct p.personId)
	from urls as u
	inner join personUrls as pU on (u.urlId = pU.urlId)
	inner join people as p using (personId)
	where u.type = 'SocialNetwork';

--#In what year did the most crises occur?--
Select year(dateAndTime)
	from crises
	group by year(dateAndTime)
	order by count(year(dateAndTime)) desc limit 1;

--#Which crises occur within the United States?--
Select name
	from crises
	where country = 'USA' or country = 'United States' or country = 'United States of America';

--#What is the total cost in damages of United States crises?--
Select sum(damageInUSD)
	from crises
	where country = 'USA' or country = 'United States' or country = 'United States of America';

--#Are there more organizations based outside of the United States than American organizations?--
Select x.num - y.num
	from
	(select count(*) as num
	from orgs
	where country <> 'USA' and country <> 'United States' and country <> 'United States of America') as x,
	(select count(*) as num
	from orgs
	where country = 'USA' or country = 'United States' or country = 'United States of America') as y;

--#What is the least common kind of person?--
Select count(*), kind
	from people
	group by kind
	order by count(*) asc limit 1;

--#How many crises is President Obama involved in?--
Select count(distinct crisisId) from
	(select * from crisisPeople where personId = '1') as T;

--#Which way to help is the most common?--
Select wayToHelp
	from waysToHelp
	group by wayToHelp
	order by count(*) desc limit 1;

--#Which country are most of the people in?--
Select country
	from people
	group by country
	order by count(*) desc limit 1;

--#How many crises have caused over 1 billion USD in damage?--
Select count(*)
	from crises
	where damageInUSD > 1000000000;

--#What is the location of each of the crises?--
Select name, city, country from crises;

--#Which crises occurred outside the USA?--
Select name from crises where country <> 'USA' and country <> 'United States';

--#Which crises relief efforts were American Red Cross a part of?--
Select distinct(c.name)
	from orgs as o
	inner join crisisOrgs using (orgId)
	inner join crises as c using (crisisId)
	where o.name = "American Red Cross";

--#Which presidents were related to the crises?--
Select distinct(p.personId), p.name, c.name
	from people as p
	inner join crisisPeople using (personId)
	inner join crises as c using (crisisId)
	where p.kind = 'President';

--#Which crises had fatalities less than 100?--
Select name from crises where fatalities <= 100;

--#Of the people classified as president, how many natural disasters were each of them--
--#connected to?--
Select p.name, count(distinct c.crisisId)
	from people as p
	inner join crisisPeople using (personId)
	inner join crises as c using (crisisId)
	where p.kind = 'President' and c.kind = 'Natural Disaster'
	group by p.name;

--#Which organizations were involved in crises that occurred outside of the country--
--#its HQs are based in?--
Select distinct(o.name)
	from orgs as o
	inner join crisisOrgs using (orgId)
	inner join crises as c using (crisisId)
	where o.country <> c.country;

--#What was the average cost damage in USD done by crises that caused over 1000 fatalities?--
Select avg(damageInUSD)
	from crises
	where fatalities > 1000;

--#How many natural disasters had over 500 fatalities and cost over 10 billion dollars?--
Select count(*) from crises where kind = 'Natural Disaster' and damageInUSD > 10000000000 and fatalities > 500;

--#Ignoring nulls, what is the total damage cost of disasters in our century?--
Select sum(damageInUSD)
	from crises
	where damageInUSD is NOT NULL and year(dateAndTime) >= 2000;