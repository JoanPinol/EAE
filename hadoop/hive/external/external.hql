##Create external table
CREATE EXTERNAL TABLE `movies`(
  `tittle` string, 
  `score` float, 
  `rating` string, 
  `genre` string, 
  `boxoffice` float, 
  `runningtime` int)
COMMENT 'movies example table'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'  
STORED AS TEXTFILE
LOCATION
  's3a://xxxx/uploads/test/movies'
TBLPROPERTIES (
  'skip.header.line.count'='1', 
)
