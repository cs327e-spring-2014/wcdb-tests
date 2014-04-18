select "GottaGitThat's Queries";

select "";
select "Which crisis had the most combined fatalities and injuries?";

select name
    from Crises
    order by (fatalities + injuries) desc limit 1;


select "";
select "How many crises have occurred in the 21st century?";

select count(distinct(crisisId))
    from Crises
    where dateAndTime > "19991231";

select "";
select "Which country has the most crises?";

select country
    from Crises
    group by country
    order by count(crisisId) desc limit 1;

select "";
select "How many organizations are related to crises that had 0 damage in USD?";

select count(distinct(orgId))
    from Crises natural join CrisisOrgs      
    where damageInUSD = 0;


select "";
select "Which people are involved in 2 or more crises?";


Select name from People inner join CrisisPeople on People.personID=CrisisPeople.personID group by name having count(*)>1;

# ------------------------------------------------------------------------
select "Brigadeiros's Queries";

select "";
select "What organizations don't exist anymore?";

select name
    from Orgs 
    where dateAbolished > 0;

select "";
select "What are the 5 most recent crises";

select name
    from Crises
    order by dateAndTime desc limit 5;

select "";
select "What are the crises with the most amount of resources?";

select name, max(num) from (
    select name, count(crisisId) as num 
    from Crises inner join CrisisResources using(crisisId)
    group by crisisId) as t;

    
select "";
select "What crises expend more money on reconstruction than in the damage done?";

select name
    from Crises
    where damageInUSD < reparationCost;


select "";
select "What's the most common kind of person?";


Select kind from People group by kind order by count(*) desc limit 1;

# ------------------------------------------------------------------------
select "Ut Non Obliviscar's Queries";

select "";
select "Which crisis had the highest reparation cost and what was the cost?";

select name, max(reparationCost) from Crises;

select "";
select "Which organizations were founded before 1950?";

select name
    from Orgs
    where dateFounded < "19500101";

select "";
select "How many organizations are intergovernmental agencies?";

select count(distinct(orgID))
    from Orgs
    where country like '%,%';
    
select "";
select "How many people have a Social Network URL?";

select count(distinct(personId))
    from PersonUrls natural join Urls
    where type = "SocialNetwork";

select "";
select "In what year did the most crises occur?";

select max(num) as 'number of crises', year from 
    ((select count(*) as num, YEAR(dateAndTime) as year from Crises 
    group by YEAR(dateAndTime)) 
    order by num desc) as t;

# ------------------------------------------------------------------------

select "Team Rocket's Queries";

select "";
select "Which crises occur within the United States?";

select name
    from Crises
    where country = "United States";

select "";
select "What is the total cost in damages of United States crises?";

select sum(damageInUSD)
    from Crises
    where country = "United States";

select "";
select "Are there more organizations based outside of the United States (within this database) than American organizations?";

select x.num - y.num
    from
    (select count(name) as num
    from orgs
    where name !="USA") as x,
    (select count(name) as num
    from orgs
    where name ="USA") as y;

select "";
select "What is the least common kind of person?";

select kind
    from People
    group by kind
    order by count(personId) asc limit 1;

select "";
select "What is the least common kind of crisis?";

select kind
    from Crises
    group by kind
    order by count(crisisId) asc limit 1;

# ------------------------------------------------------------------------
select "Databosses' Queries";

select "";
select "How many crises is President Obama involved in?";

select count(distinct(crisisId))
    from CrisisPeople natural join People
    where name = "Barack Obama";

select "";
select "Which 'Way to Help' is most common?";

select wayToHelp
    from WaysToHelp natural join CrisisWaysToHelp
    group by wayToHelp
    order by count(crisisId) desc limit 1;

select "";
select "What country are most of the People in?";

select country
    from People
    group by country
    order by count(personId) desc limit 1;

select "";
select "What organizations are involved with the Haiti Earthquake?";

select o.name
    from Orgs as o inner join CrisisOrgs using (orgId)
              inner join Crises as c using (crisisId)
    where c.name = "Haiti Earthquake";

select "";
select "How many crises have caused over 1 billion USD in damages?";

select count(*)
    from Crises
    where damageInUSD > 1000000000;

# ------------------------------------------------------------------------
select "SeekWolves's Queries";

select "";
select "What is the location of each of the crisis (city and country)?";

select name, city, country
    from Crises;

select "";
select "Which crises occurred outside US?";

select name
    from Crises
    where country != "United States";

select "";
select "Which crises relief effort was American Red Cross part of?";

select distinct(c.name)
    from Crises as c inner join CrisisOrgs using (crisisId)
                inner join Orgs as o using (orgId)
    where o.name = "American Red Cross";

select "";
select "Which presidents were related to the crises?";

select distinct(name)
    from People natural join CrisisPeople
    where kind = "President";

select "";
select "Which crises had fatalities less than 100?";

select name
    from Crises
    where fatalities < 100;

# ------------------------------------------------------------------------
select "BashKetchum's Queries";

select "";
select "Of the people classified as presidents, how many natural disasters were each of them connected to?";

select p.name, count(distinct(c.crisisId))
    from People as p inner join CrisisPeople using (personId) inner join Crises as c using (crisisId)
    where p.kind = "President" and c.kind = "Natural Disaster";
    group by p.name;

select "";
select "Which organizations were involved in crises that occurred outside of the country its HQs are based in?";

select distinct (o.name)
    from Orgs as o inner join CrisisOrgs using (orgId) inner join Crises as c using (crisisId)
    where o.country != c.country;

select "";
select "What was the average cost damage in USD done by crises that caused over 1000 fatalities?";

select avg(damageInUSD)
    from Crises
    where fatalities > 1000;

select "";
select "How many natural disasters had over 500 fatalities and costed over 10 billion dollars";

select count(*)
    from Crises
    where kind = "Natural Disaster" and and fatalities > 500 and reparationCost > 10000000000;

select "";
select "Ignoring nulls, what is the total damage cost of disasters in our century";

select sum(damageInUSD)
    from Crises
    where damageInUSD != NULL and year(dateAndTime) >= 2000;

# ------------------------------------------------------------------------
select "EJADK's Queries";

select "";
select "What is the first (earliest) crisis in the database?";

select name
    from Crises
    order by dateAndTime asc limit 1;

select "";
select "What is the total number of deaths caused by natural disasters?";

select sum(fatalities)
    from Crises
    where kind = "Natural Disaster";

select "";
select "Count the number of politicians grouped by country.";

select country, count(personId)
    from People 
    where kind = "Politician"
    group by country;

select "";
select "Count the number of crisis that each organization helped.";

select name, count(crisisId)
    from Orgs natural join CrisisOrgs
    group by orgId;

select "";
select "What is the most common resource needed?";

select resource
    from CrisisResources natural join Resources
    group by resourceId
    order by count(crisisId) desc limit 1;

exit
