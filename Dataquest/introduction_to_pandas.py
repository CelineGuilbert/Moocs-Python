import pandas
food_info = pandas.read_csv("food_info.csv")
print(type(food_info))


#exploring dataframe

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)
first_twenty = food_info.head(20)

#selecting a row

hundredth_row = food_info.loc[99]
print(hundredth_row)


#type
print(food_info.dtypes)



#selecting multiple rows

print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])

nums_rows = food_info.shape[0]
last_rows = food_info.loc[nums_rows-5:nums_rows]

# selecting individual columns

# Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

# Display the type of the column to confirm it's a Series object.
print(type(ndb_col))

saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]


# Selecting Multiple Columns By Name

zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]

selenium_thiamin = food_info[['Selenium_(mcg)', 'Thiamin_(mg)']]



#Select and display only the columns that use grams for measurement (that end with "(g)"). To accomplish this:
#Use the columns attribute to return the column names in food_info and convert to a list by calling the method tolist()
#Create a new list, gram_columns, containing only the column names that end in "(g)". The string method endswith() returns True
#if the string object calling the method ends with the string passed into the parentheses.
#Pass gram_columns into bracket notation to select just those columns and assign the resulting dataframe to gram_df
#Then use the dataframe method head() to display the first 3 rows of gram_df.

print(food_info.columns)
print(food_info.head(2))
column_list = food_info.columns.tolist()
grams_columns = [col for col in column_list if col.endswith("(g)")]
gram_df = food_info[grams_columns]
gram_df.head(3)

