# Print the tables in the catalog
print(spark.catalog.listTables())

## [Table(name='flights', database=None, description=None, tableType='TEMPORARY', isTemporary=True)]



# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()
