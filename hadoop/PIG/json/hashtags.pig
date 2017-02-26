-- Registering elephant-bird udf. Get the jars from its github: https://github.com/twitter/elephant-bird


REGISTER hdfs://quickstart.cloudera:8020/user/cloudera/udf/elephant-bird-hadoop-compat-4.1.jar;
REGISTER hdfs://quickstart.cloudera:8020/user/cloudera/udf/elephant-bird-pig-4.1.jar;
REGISTER hdfs://quickstart.cloudera:8020/user/cloudera/udf/json-simple-1.1.1.jar;

load_tweets = LOAD '/user/cloudera/pig/twitter/limited/' USING com.twitter.elephantbird.pig.load.JsonLoader('-nestedLoad') AS myMap;
extract_details = FOREACH load_tweets GENERATE FLATTEN(myMap#'entities') as (m:map[]),FLATTEN(myMap#'id') as id;
hash = foreach extract_details generate FLATTEN(m#'hashtags') as(tags:map[]),id as id;


txt = foreach hash generate FLATTEN(tags#'text') as text ,id;
grp = group txt by text;

cnt = foreach grp generate group as hashtag_text, COUNT(txt.text) as hashtag_cnt:long;
ordered = ORDER cnt BY hashtag_cnt DESC;
dump ordered;
