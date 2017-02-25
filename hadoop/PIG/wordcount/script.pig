lines = LOAD '/user/admin/files/starwars/starwars-epIV.txt' USING PigStorage('\t') 
	AS (character: chararray, dialog: chararray);
words = FOREACH lines GENERATE FLATTEN(TOKENIZE(REPLACE(LOWER(TRIM(dialog)),'[\\p{Punct},\\p{Cntrl}]','')))
	as word;
grouped = GROUP words BY word;
wordcount = FOREACH grouped GENERATE group, COUNT(words);
wordcountsort = ORDER wordcount BY $1 DESC; 

STORE wordcountsort INTO '/user/admin/files/starwars/output_words' USING 
PigStorage(','); 
