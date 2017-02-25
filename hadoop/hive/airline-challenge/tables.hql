#
#Original data from http://stat-computing.org/dataexpo/2009/
#

#create external table loading data
create temporary external table onTimePerfExt
(Year INT ,
Month INT ,
DayofMonth INT ,
DayOfWeek INT ,
DepTime INT ,
CRSDepTime INT ,
ArrTime INT ,
CRSArrTime INT ,
UniqueCarrier STRING ,
FlightNum INT ,
TailNum STRING ,
ActualElapsedTime INT ,
CRSElapsedTime INT ,
AirTime STRING ,
ArrDelay INT ,
DepDelay INT ,
Origin STRING ,
Dest STRING ,
Distance INT ,
TaxiIn STRING ,
TaxiOut STRING ,
Cancelled INT ,
CancellationCode STRING ,
Diverted INT ,
CarrierDelay STRING ,
WeatherDelay STRING ,
NASDelay STRING ,
SecurityDelay STRING ,
LateAircraftDelay STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE
LOCATION 's3a://xxxx/uploads/test/airline/';

#create partitioned table on hdfs
create table onTimePerfPart
(DayofMonth INT ,
DayOfWeek INT ,
DepTime INT ,
CRSDepTime INT ,
ArrTime INT ,
CRSArrTime INT ,
UniqueCarrier STRING ,
FlightNum INT ,
TailNum STRING ,
ActualElapsedTime INT ,
CRSElapsedTime INT ,
AirTime STRING ,
ArrDelay INT ,
DepDelay INT ,
Origin STRING ,
Dest STRING ,
Distance INT ,
TaxiIn STRING ,
TaxiOut STRING ,
Cancelled INT ,
CancellationCode STRING ,
Diverted INT ,
CarrierDelay STRING ,
WeatherDelay STRING ,
NASDelay STRING ,
SecurityDelay STRING ,
LateAircraftDelay STRING)
PARTITIONED BY (Year INT, Month INT )
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE;

#load data into partitioned table
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
INSERT OVERWRITE TABLE onTimePerfPart PARTITION(Year, Month) SELECT DayofMonth, DayOfWeek, DepTime, CRSDepTime, ArrTime, CRSArrTime, UniqueCarrier, FlightNum, TailNum, ActualElapsedTime, CRSElapsedTime, AirTime, ArrDelay, DepDelay, Origin, Dest, Distance, TaxiIn, TaxiOut, Cancelled, CancellationCode, Diverted, CarrierDelay, WeatherDelay, NASDelay, SecurityDelay, LateAircraftDelay, Year, Month FROM onTimePerfExt;

#test performance
SELECT * FROM ontimeperfhdfs where year = 2008 and tailnum = 'N763SW' and dest = 'TPA';
