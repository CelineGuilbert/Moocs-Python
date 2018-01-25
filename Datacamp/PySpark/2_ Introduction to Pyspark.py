# Create the DataFrame flights
flights = spark.table("flights")

# Show the head
print(flights.show())

# Add duration_hrs  - Create a column
# In Spark you can do this using the .withColumn() method, which takes two arguments. 
#First, a string with the name of your new column, and second the new column itself.

flights = flights.withColumn("duration_hrs",flights.air_time / 60 )

#Updating a Spark DataFrame is somewhat different than working in pandas because the Spark DataFrame is immutable.
#This means that it can't be changed, and so columns can't be updated in place.



### Filtering Data
# Filter flights with a SQL string
long_flights1 = flights.filter("distance > 1000")

# Filter flights with a boolean column
long_flights2 = flights.filter(flights.distance > 1000)

# Examine the data to check they're equal
print(long_flights1.show())print(long_flights2.show())

#The Spark variant of SQL's SELECT is the .select() method
#This method takes multiple arguments - one for each column you want to select. 
#These arguments can either be the column name as a string (one for each column) or a column object (using the df.colName syntax). 
#When you pass a column object, you can perform operations like addition or subtraction on the column to change the data contained in it,


### Selecting
# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")
# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)
# Define first filter
filterA = flights.origin == "SEA"
# Define second filter
filterB = flights.dest == "PDX"
# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)


# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")
# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)
# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")


### Aggregating
# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin=="PDX").groupBy().min("distance").show()
# Find the longest flight from SEA in terms of duration
flights.filter(flights.origin=="SEA").groupBy().max("air_time").show()

# Average duration of Delta flights
flights.filter(flights.carrier=="DL").filter(flights.origin=='SEA').groupBy().avg("air_time").show()
# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()



###Grouping and Aggregating 
# Group by tailnum
by_plane = flights.groupBy("tailnum")
# Number of flights each plane made
by_plane.count().show()
# Group by origin
by_origin = flights.groupBy("origin")
# Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()


# Import pyspark.sql.functions as F
import pyspark.sql.functions as F
# Group by month and dest
by_month_dest = flights.groupBy("month","dest")
# Average departure delay by month and destination
by_month_dest.avg('dep_delay').show()
# Standard deviation
by_month_dest.agg(F.stddev('dep_delay')).show()
