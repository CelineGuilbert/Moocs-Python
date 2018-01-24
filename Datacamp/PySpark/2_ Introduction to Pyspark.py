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
