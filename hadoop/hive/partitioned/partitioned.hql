#Create partitioned table
##Creating temporary table (will be deleted atomatically at the end of the session)
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;
set hive.exec.max.dynamic.partitions.pernode=1000;
 
DROP TABLE IF EXISTS temp_user;
 
CREATE TEMPORARY TABLE temp_user(
	firstname VARCHAR(64),
	lastname  VARCHAR(64),
	address   STRING,
	country   VARCHAR(64),
	city      VARCHAR(64),
	state     VARCHAR(64),
	post      STRING,
	phone1    VARCHAR(64),
	phone2    STRING,
	email     STRING,
	web       STRING
	)
	ROW FORMAT DELIMITED 
		FIELDS TERMINATED BY ','
		LINES TERMINATED BY '\n'
        STORED AS TEXTFILE;
 
LOAD DATA INPATH '/user/admin/files/UserRecords/UserRecords.txt' INTO TABLE temp_user;

##Creating partitioned table
CREATE TABLE partitioned_user(
	firstname VARCHAR(64),
	lastname  VARCHAR(64),
	address   STRING,
	city 	  VARCHAR(64),
	post      STRING,
	phone1    VARCHAR(64),
	phone2    STRING,
	email     STRING,
	web       STRING
	)
	PARTITIONED BY (country VARCHAR(64), state VARCHAR(64))
	STORED AS SEQUENCEFILE;
 
INSERT INTO TABLE partitioned_user
	PARTITION (country, state)
        SELECT  firstname ,
		lastname  ,
		address   ,
	city      ,
		post      ,
		phone1    ,
		phone2    ,
		email     ,
		web       ,
		country   ,
	state     
	FROM temp_user;

## testing performance
SELECT firstname, phone1, city 
	FROM partitioned_user 
	WHERE country='US' AND state='CA' 
	ORDER BY city 
	LIMIT 5;
  
SELECT firstname, phone1, city 
	FROM temp_user 
	WHERE country='US' AND state='CA' 
	ORDER BY city 
	LIMIT 5;
  
##analizing partitions
show partitions partitioned_user;
SHOW PARTITIONS partitioned_user PARTITION(country='US');
 
