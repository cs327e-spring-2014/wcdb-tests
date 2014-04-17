--# What is the first (earliest) crisis in the database?--
Select name, dateAndTime
	From crises
	Where dateAndTime <= all
    	(Select dateAndTime
            From crises);
	
--# What is the total number of deaths caused by natural disasters?--
Select sum(fatalities)
	From crises
	Where kind = 'Natural Disaster';
	
--# Count the number of politicians grouped by country?--
Select country, count(*)
	From people 
	Where kind = 'politician' 
	Group by country;

--# Count the number of crises that each organization helped?--
Select name, count(distinct crisisId)
	From crisisOrgs
	inner join orgs using (orgId)
	Group by name;
    
--# What is the most common resource needed?--
Select resource, count(resourceId)
	From resources 
	inner join crisisResources using (resourceId)
	group by resourceId
	order by count(resourceId) desc
	limit 1 ;
	
	
	
		
