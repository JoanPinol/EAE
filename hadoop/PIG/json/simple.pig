dishes = LOAD '/user/cloudera/pig/restaurant/restaurant.json'
         USING JsonLoader(
             'dish:chararray, cheff:chararray, amount:float'
         );
cheaper = FILTER dishes BY amount < 4;         
ordered = ORDER cheaper BY cheff ASC;
dump ordered;
