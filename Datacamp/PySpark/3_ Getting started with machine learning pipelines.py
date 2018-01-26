
#The columns in your DataFrame must be either integers or decimals (called 'doubles' in Spark).

#When we imported our data, we let Spark guess what kind of information each column held. 
#Unfortunately, Spark doesn't always guess right and you can see that some of the columns in our DataFrame are strings 
#containing numbers as opposed to actual numeric values.

#To remedy this, you can use the .cast() method in combination with the .withColumn() method. 
#It's important to note that .cast() works on columns, while .withColumn() works on DataFrames.



# Cast the columns to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast('integer'))
model_data = model_data.withColumn("air_time",model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month", model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year", model_data.plane_year.cast('integer'))


## Create the column plane_age
#plane_year = each plane was manufactured
"nous voulons avoir l'âge de l'avion 
model_data = model_data.withColumn("plane_age", model_data.year-model_data.plane_year)

# Create is_late
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0 )
# Convert to an integer
model_data = model_data.withColumn("label", model_data.is_late.cast('integer'))
# Remove missing values
model_data = model_data.filter("arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")
