
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


# Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index",outputCol="carrier_fact")

##The last step in the Pipeline is to combine all of the columns containing our features into a single column. 
##You can do this by storing each of the values from a column as an entry in a vector. 
##, the pyspark.ml.feature submodule contains a class called VectorAssembler. 
##This Transformer takes all of the columns you specify and combines them into a new vector column.

# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=['month',"air_time","carrier_fact","dest_fact","plane_age"], outputCol="features")


##Create the pipeline

#Pipeline is a class in the pyspark.ml module that combines all the Estimators and Transformers that you've already created. 
#This lets you reuse the same modeling process over and over again by wrapping it up in one simple object

# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer,dest_encoder,carr_indexer,carr_encoder,vec_assembler])




## TEST VS TRAIN

#In Spark it's important to make sure you split the data after all the transformations.
#This is because operations like StringIndexer don't always produce the same index even when given the same list of strings.



# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)

# Split the data into training and test sets
training, test = piped_data.randomSplit([.6,.4])
