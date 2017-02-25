##Create table 
CREATE TABLE `twitterdata`(
  `tweetid` bigint, 
  `username` string, 
  `txt` string, 
  `createdat` string, 
  `profilelocation` string, 
  `favc` bigint, 
  `retweet` string, 
  `retcount` bigint, 
  `followerscount` int)
COMMENT 'ejemplo twitter'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'  
STORED AS TEXTFILE;

##Load data into the table
LOAD  DATA  INPATH  '/user/admin/files/twitter/Twitterdata.txt' OVERWRITE INTO TABLE twitterdata;


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

#Create partitioned table
