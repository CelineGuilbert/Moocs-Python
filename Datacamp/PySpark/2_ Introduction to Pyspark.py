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
