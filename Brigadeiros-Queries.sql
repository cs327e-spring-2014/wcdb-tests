use cs327e_abatista; 

#----------------------------NUMBER 1S----------------------------
select "Which crisis had the most combined fatalities and injuries?";
select name, max(fatalities + injuries) from crises;

select "What organizations don't exist anymore?";
select name, dateAbolished from orgs where dateAbolished < (DATE(NOW()));

select "Which crisis had the highest reparation cost and what was the crisis?";
select name, max(reparationCost) from crises;

select "Which crises occur within the United States?";
select name, country from crises where country = 'USA' or country = 'United States' or country = 'ALL';

select "How many crisis is president Obama involved in?";
select count(*) from orgPeople where personId in (select personId from people where name = 'Barack Obama');

select "What is the location of each of the crisis (city and country)?";
select name, city, country from crises;

select "Of the people classified as presidents, how many natural disasters were each of them connected to?";
select R.name, count(*) as Connected_To from people as R inner join crisisPeople using (personId) inner join crises as P using (crisisId) where (R.kind = 'President') and (P.kind = 'Natural Disaster') group by R.name;

select "What is the first (earliest) crisis in the database?";
select name, dateAndTime from crises order by dateAndTime asc limit 1;

#----------------------------NUMBER 2S----------------------------
select 'How many crises have occurred in the 21st century?';
select count(name) as Total_Crises from crises where dateAndTime between '2000-01-01 00:00:00' and '2999-12-31 23:59:59' order by dateAndTime;

select 'What are the 5 most recent crises?';
select crisisID, name, dateAndTime from crises order by dateAndTime desc limit 5;

select 'Which organizations were founded before 1950?';
select orgId, name, dateFounded from orgs where dateFounded <= '1950-01-01' order by dateFounded desc;

select ' What is the total cost in damages of United States crises?';
select sum(damageInUSD) from crises where country='USA' or country='US' or country='United States' or country='United States of America';

select 'Which Way to Help is most common?';
select Y as Appearances, wayToHelp from (select count(wayToHelp) as Y, wayToHelp from waysToHelp inner join crisisWaysToHelp using(helpId) group by wayToHelp) as A where Y >= all (select count(wayToHelp) as Z from waysToHelp inner join crisisWaysToHelp using(helpId) group by wayToHelp);

select 'Which crises occurred outside US?';
select crisisId, name, country from crises where country<>'USA' and country<>'US' and country<>'United States' and country<>'United States of America';

select 'Which organizations were involved in crises that occurred outside of the country its HQs are based in?';
select A.name, B.name from crises as A inner join crisisOrgs as C using (crisisId) inner join orgs as B using (orgId) where A.country <> B.country;

select 'What is the total number of deaths caused by natural disasters?';
select sum(fatalities) from crises where kind='Natural Disaster';

#----------------------------NUMBER 3S----------------------------
select "How many organizations are intergovernmental agencies?";
select count(*) from orgs where kind="Intergovernmental Agency";

select "Which crises relief effort was American Red Cross part of?";
select distinct crises.name from crises 
	inner join crisisOrgs on crises.crisisId 
	inner join orgs on orgs.orgId 
	where orgs.name="International Federation of Red Cross and Red Crescent Societies";

select "What was the average cost damage in USD done by crises that caused over 1000 fatalities?";
select avg(damageInUSD) as "Average Cost Damage" from crises where fatalities > 1000;

select "Which country has the most crises?";
select distinct crises.country, count(*) from crises group by country order by count(*) DESC limit 1;

select "What country are most people in?";
select distinct country, count(*) as "# People from" from people group by country order by count(*) DESC limit 1;

select "Count the number of politicians grouped by country.";
select country, count(kind) as "Number of Politicians" from people where kind="Politician" group by country order by "Number of Politicians" asc;

select " What are the crises with the most amount of resources?";
select name, count(resourceId) as "number resources" from crises inner join crisisResources using(crisisId) group by name order by count(resourceId) desc limit 5;

select "Are there more organizations based outside of the United States (within this database) than American organizations?";
select if ((select count(distinct name) from orgs where country="USA" or country="United States" or country="US") < (select count(distinct name) from orgs where country<>"USA" and country<>"United States" and country<>"US"),'YES','NO');

#----------------------------NUMBER 4S----------------------------
select 'How many organizations are related to crises that had 0 damage in USD? -  Tested, runs, I dont know if the result is correct';
select count(distinct(A.orgID)) from orgs as A inner join crisisOrgs as B using (orgID) inner join crises as C using (crisisID) where C.damageInUSD = 0;

select 'What crises expend more money on reconstruction than in the damage done? - Tested, runs, I dont know if the result is correct';
select name from crises where (damageInUSD) < (reparationCost) order by name;

select 'How many people have a Social Network URL? - Tested, runs, I think it works';
select count(distinct(name)) from people natural join personUrls where urlId is not NULL;

select 'What is the least common kind of person? - Not working, need to solve it';
select A, kind from (select kind, count(kind) as  A from people group by kind) as B where A <= all (select X from (select count(kind) as X from people group by kind) as Y);

select 'What organizations are involved with the Haiti Earthquake? - Tested, it ru,s it works';
select A.name from orgs as A inner join crisisOrgs as B using (orgID) inner join crises as C using (crisisID) where C.name = 'Haiti Earthquake' order by A.name;
	
select 'Which presidents were related to the crises? - Tested, runs, works';
select distinct(A.name) from people as A inner join crisisPeople as B using (personID) inner join crises as C using (crisisID) where A.kind = 'President' order by A.name;
		
select 'How many natural disasters had over 500 fatalities and costed over 10 billion dollars? - Tested, runs, works';
select count(name) from crises where kind = 'Natural Disaster' and fatalities > 500 and damageInUSD > 10000000000;

select 'Count the number of crisis that each organization helped. Tested, runs, I dont know if the result is correct';
select distinct(A.name), count(distinct(C.crisisID)) from orgs as A inner join crisisOrgs as B using (orgID) inner join crises as C using (crisisID) group by C.name order by name;

#----------------------------NUMBER 5S----------------------------
select"Which people are involved in 2 or more crises";
select max(A) as Appearances, C from (select count(personId) as A, X.name as C from people as X inner join orgPeople as Y using (personId) inner join orgs as Z using (orgId) group by personId) as B;

select"What is the most common kind of person?";
select A, kind from (select kind, count(kind) as A from people group by kind) as B where A >= all (select X from (select count(kind) as X from people group by kind) as Y);

select"In what year did the most crises occur?";
select S as Appearances, year from (select count(year) as S, year from (select Extract(year from dateAndTime) as year from crises) as B group by year) as C where S >= all (select count(W) as X from (select Extract(year from dateAndTime) as W from crises) as Y group by W);

select"What is the least common kind of crisis?";
select A, kind from (select kind, count(kind) as A from crises group by kind) as B where A <= all (select X from (select count(kind) as X from crises group by kind) as Y);

select"How many crises have caused over 1 billion USD in damages?";
select count(*) from crises where damageInUSD > 1000000000;

select"Which crises had fatalities less than 100?";
select name from crises where fatalities < 100;

select"Ignoring nulls, what is the total damage cost of disasters in our century?";
select sum(damageInUSD)	from crises where dateAndTime< '2000-01-01T:00:00:00' and dateAndTime>='1900-01-01T00:00:00';

select"What is the most common resource needed?";
select resource from crisisResources inner join resources using (resourceId) group by resourceId order by count(*) desc limit 1;

exit
