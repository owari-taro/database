# case分

```

postgres=# select * from sample_prefpopulation;
 id |  name   | sex | population 
----+---------+-----+------------
  1 | tokyo   |   1 |        120
  2 | tokyo   |   2 |         40
  3 | saitama |   1 |         30
  4 | saitama |   2 |         30
(4 rows)

postgres=# select name, sum(case when sex=1 then population else 0 end) as men,sum(case when sex=2 then population else 0 end) as women from sample_prefpopulation group by name;
  name   | men | women 
---------+-----+-------
 tokyo   | 120 |    40
```