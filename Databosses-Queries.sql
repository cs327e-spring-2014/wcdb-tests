select "";
select "GottaGitThat's Queries";
select "";



select "1";
select "Which crisis had the most combined fatalities and injuries?";

select name, MAX(coalesce(fatalities, injuries)) 
	from crises;


	select "2";
select "How many crises have occurred in the 21st century?";

select COUNT(*)
	from crises
	where year(dateAndTime) > 1999;



select "3";
select "Which country has the most crises?";

select country 
	from crises 
	group by country 
	order by count(country) desc 
	limit 1;
	
						

select "4";
select "How many organizations are related to crises that had 0 damage in USD?";

select count(distinct(orgId)) 
	from crisisOrgs 
	where crisisId in (select crisisId 
		from crises 
		where damageInUSD = 0);



select "5";
select "Which people are involved in 2 or more crises?";

select name 
	from people 
	where personId in (select personId 
		from crisisPeople 
		group by personId 
		having count(personId) >= 2);




select "";
select "Brigadeiros' Queries";
select "";



select "6"; 
select "What organizations don't exist anymore?";

select name, dateAbolished 
	from orgs 
	where year(dateAbolished) < 2015;



select "7";
select "What are the 5 most recent crises?";

select name 
	from crises 
	ORDER BY dateAndTime desc 
	limit 5;	


select "8";
select "What are the crises with the most amount of resources?";

select name, crisisId 
	from crises 
		where crisisId in (select crisisId 
			from crisisResources 
			group by crisisId 
			order by count(resourceId) desc) 
			limit 1;



select "9";
select "What crises expend more money on reconstruction than in the damage done?";

select name, damageInUSD, reparationCost 
	from crises 
	where reparationCost > damageInUSD;


select "10";
select "Whats the most common kind of person?";

select kind, (count(kind)) 
	from people 
	group by kind 
	order by count(kind) desc limit 1;

select ""; 
select "Ut Non Obliviscar's Queries";
select "";

select "11"; 
select "Which crisis had the highest reparation cost?";

select name, Max(reparationCost) 
	from crises;

select "12";
select "Which organizations were founded before 1950?";

select name 
	from orgs 
	where year(dateFounded) < 1950;

select "13";
select "How many organizations are intergovernmental agencies?";

select count(kind) 
	from orgs 
	where (kind = 'Intergovernmental Agency');

select "14";
select "How many people have a Social Network URL?";

select distinct(personId), urlId 
	from personUrls 
	where urlId in (select urlId 
		from urls where type = "Social Network");

select "15";
select "In what year did the most crises occur?";

select count(year(dateAndTime)), year(dateAndTime) 
	from crises where year(dateAndTime) NOT LIKE "0" 
	group by year(dateAndTime)
	order by count(year(dateAndTime)) desc 
	limit 1;

select "";
select "Team Rocket's Queries";
select "";

select "16";
select "Which crises occur within the United States?";

select name 
	from crises 
	where country = 'USA' or 'United States';


select "17";
select "What is the total cost in damages of United States crises?";

select COALESCE(sum(damageInUSD)) 
	from crises 
	where country = "USA" or country = "US" or country = "United States";

select "18";
select "Are there more organizations based outside of the United States than American organizations?";

(SELECT country, count(orgId)
	from orgs
	where country = 'US' 
	or country = 'USA' 
	or country = 'United States' 
	or country = 'United States of America')
union
(SELECT 'Other', count(orgId)
	from orgs
	where country not in ('USA','US','United States', 'United States of America'));

select "19";
select "What is the least common kind of person?";

select kind, (count(kind))  
	from people  
	group by kind  
	order by count(kind) asc 
	limit 1;

select "20";
select "What is the least common kind of crisis?";

SELECT kind
	FROM crises
	GROUP BY kind
	ORDER BY count(kind) ASC
	limit 1;

select "";
select "Databosses' Queries";
select ""; 

select "21";
select "How many crises is President Obama involved in?";

select count(*) from people natural join crisisPeople where name in (select name from people where name = 'Barack Obama');



		
select "22";	
select "Which 'Way to Help' is most common?";

SELECT wayToHelp
	FROM waysToHelp
	WHERE helpId = (SELECT helpId
			FROM crisisWaysToHelp
			GROUP BY helpId
			ORDER BY count(helpId) DESC
			limit 1);

select "23";
select "What country are most of the People in?";

SELECT country
	FROM people
	group by country
	order by count(name) desc
	limit 1;

select "24";
select "What organizations are involved with the Haiti Earthquake?";

SELECT distinct name
	from orgs
	where orgId in (SELECT orgId
				from crisisOrgs
				where crisisId in (SELECT crisisId
							from crises 
							where name = 'Haiti Earthquake'));

select "25";
select "How many crises have caused over 1 billion USD in damages?";

SELECT name, damageInUSD
	from crises
	where (damageInUSD > 1000000000);

select "";
select "SeekWolves' Queries";
select "";
 
select "26"; 
select "What is the location of each of the crisis (city and country)?";

SELECT name, city, country
	from crises;

select "27";
select "Which crises occurred outside USA?";

SELECT name
	from crises
	where (country != "USA" AND country != "United States of America" AND country != "United States");

select "28";
select "Which crises relief effort was American Red Cross part of?";

SELECT crises.name
	from crises
	inner join crisisOrgs using (crisisId)
	inner join orgs using (orgId)
	where orgs.name = 'American Red Cross';

select "29";	
select "Which presidents were related to the crises?";

SELECT DISTINCT people.name, crises.name
	from people
	inner join crisisPeople using (personId)
	inner join crises using (crisisId)
	where people.kind = 'President;;

select "30";
select "Which crises had fatalities less than 100?";

SELECT name, fatalities
	from crises
	where (fatalities < 100);

select "";	
select "BashKetchum"'"s Queries";
select "";

select "31";
select "Of the people classified as presidents,how many natural disasters were each of them connected to?";

SELECT distinct people.name
	from people
	inner join crisisPeople using (personId)
	inner join crises using (crisisId)
	where crises.kind ='Natural Disaster' AND 
	people.kind = 'President';

				
select "32";
select "Which organizations were involved in crises that occurred outside of the country its HQs are based in?";

SELECT distinct orgs.name
	from orgs
	inner join crisisOrgs using (orgId)
	inner join crises using (crisisId)
	where orgs.country != crises.country;
	
select "33";
select "What was the average cost damage in USD done by crises that caused over 1000 fatalities?";

SELECT avg(damageInUSD)
	from crises
	where (fatalities > 1000);

select "34";
select "How many natural disasters had over 500 fatalities and costed over 10 billion dollars?";

SELECT name 
	FROM crises 
	WHERE (kind = 'Natural Disaster') 
		AND (fatalities > 500) 
		AND (damageInUSD > 10000000000);

select "35";
select "Ignoring nulls, what is the total damage cost of disasters in our century?";

select SUM(damageInUSD)
	from crises
	where year(dateAndTime) > 2000
		AND damageInUSD is NOT NULL;

select "";
select "EJADK's Queries";
select "";

select "36";
select "What is the first (earliest) crisis in the database?";

select dateAndTime 
	from crises 
	where year(dateAndTime) > 0000 
	order by dateAndTime asc 
	limit 1;

select "37";
select "What is the total number of deaths caused by natural disasters?";

select SUM(fatalities)
	from crises
	where kind = "Natural Disaster"
		AND fatalities is NOT NULL;

select "38";
select "Count the number of politicians grouped by country?";

select country, COUNT(kind)
	from people
	where (kind = "Politician")
	GROUP BY country;	

select "39";
select "Count the number of crisis that each organization helped?";

select orgs.name, count(crises.name)
	from orgs 
	inner join crisisOrgs using (orgId)
	inner join crises using (crisisId)
	group by orgs.name
	order by orgs.name asc;

select "40";
select "What is the most common resource needed?";

select resourceId, resource, count(crisisId) 
	from resources natural join crisisResources 
		group by crisisId 
		order by count(crisisId) desc 
		limit 1;

		
