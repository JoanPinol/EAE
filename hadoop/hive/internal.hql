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
