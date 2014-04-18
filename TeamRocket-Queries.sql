--# Which crises occur within the United States?--
select *
from Crises
where country = "United States";

--# What is the total cost in damages of United States crises?--
select damageInUSD
from Crises
where country = "United States";

--# Are there more organizations based outside of the United States (within this database) than American organizations?--
select R.col1 - S.col2
from
(select count(*) as col1
from Orgs
where country != "United States")
as R,
(select count(*) as col2
from Orgs
where country = "United States")
as S
;

--# What is the least common kind of person?--
select R, S
from
(select kind as R, count(*) as S
 from People
 group by kind)
as S
order by S asc
limit 0, 1
;

--# What is the least common kind of crisis?--
select R, S
from
(select kind as R, count(*) as S
 from Crises
 group by kind)
as S
order by S asc
limit 0, 1
;
