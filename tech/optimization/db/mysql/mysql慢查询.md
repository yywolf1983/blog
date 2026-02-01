mysqldumpslow命令
/path/mysqldumpslow -s c -t 10 /database/mysql/slow-log
这会输出记录次数最多的10条SQL语句，其中：


-s, 是表示按照何种方式排序，c、t、l、r分别是按照记录次数、时间、查询时间、返回的记录数来排序，ac、at、al、ar，表示相应的倒叙；
-t, 是top n的意思，即为返回前面多少条的数据；
-g, 后边可以写一个正则匹配模式，大小写不敏感的；
比如
/path/mysqldumpslow -s r -t 10 /database/mysql/slow-log
得到返回记录集最多的10个查询。
/path/mysqldumpslow -s t -t 10 -g “left join” /database/mysql/slow-log
得到按照时间排序的前10条里面含有左连接的查询语句。
