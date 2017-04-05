#Missing data can take a few different forms:

#In Python, the None keyword and type indicates no value.
#The Pandas library uses NaN, which stands for "not a number", to indicate a missing value.
#In general terms, both NaN and None can be called null values

#If we want to see which values are NaN, we can use the pandas.isnull() function which takes a pandas series and returns a series of
#True and False values, the same way that NumPy did when we compared arrays.

sex = titanic_survival["sex"]
sex_is_null = pandas.isnull(sex)
sex_null_true = sex[sex_is_null] #We can use this resultant series to select only the rows that have null values.

age_is_null = pandas.isnull(age) #renvoie True or False
age_null_true = age[age_is_null]
age_null_count = len(age_null_true) #permer de compter
print(age_null_count)


age_is_null = pd.isnull(titanic_survival["age"])
good_ages = titanic_survival["age"][age_is_null == False]
correct_mean_age = sum(good_ages) / len(good_ages)


##4: Easier Ways To Do Math
#Luckily, missing data is so common that many pandas methods automatically filter for it. 
#For example, if we use use the Series.mean() method to calculate the mean of a column, missing values will not be included in the
#calculation.
correct_mean_fare= titanic_survival["fare"].mean()


##5: Calculating Summary Statistics
#Use a for loop to iterate over passenger_classes. Within the for loop:
  #Select just the rows in titanic_survival where the pclass value is equivalent to the current iterator value (class).
  #Select just the fare column for the current subset of rows.
  #Use the Series.mean method to calculate the mean of this subset.
  #Add the mean of the class to the fares_by_class dictionary with class as the key.
#Once the loop completes, the dictionary fares_by_class should have 1, 2, and 3 as keys, with the average fares as the corresponding 
#values.

passenger_classes = [1, 2, 3]
fares_by_class = {}

for classe in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival['pclass']== classe]
    pclass_fares= pclass_rows['fare']
    fare_for_class = pclass_fares.mean()
    fares_by_class[classe]=fare_for_class
            
      
##6: Making Pivot Tables
#Luckily, the Dataframe.pivot_table() method instead, which simplifies the kind of work we did on the last screen. 
#To produce the same data, we could use one line.

passenger_survival = titanic_survival.pivot_table(index="pclass", values="fare", aggfunc=np.mean)
#calcule la valeur moyenne de "fare" par "pclass"
#The default for the aggfunc parameter is actually the mean, so if we're calculating this we can omit this parameter.


## 7: More Complex Pivot Tables
#pass a list of column names to the values parameter instead of a single value
import numpy as np
port_stats = titanic_survival.pivot_table(index="embarked", values=["fare","survived"], aggfunc=np.sum)
print(port_stats)

##                fare  survived
##embarked                      
##C         16830.7922     150.0
##Q          1526.3085      44.0
##S         25033.3862     304.0

##8: Drop Missing Values
#The dropna() method takes an axis parameter, which indicates whether you would like to drop rows or columns. 
#Specifying axis=0 or axis='index' will drop any rows that have null values, 
##while specifying axis=1 or axis='columns' will drop #any columns that have null values.
#We will use 0 and 1 since they're more commonly used, but you can use either.

drop_na_rows = titanic_survival.dropna(axis=0)
#Drop all rows in titanic_survival where the columns "age" or "sex" have missing and values assign the result to new_titanic_survival.
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["age", "sex"])


##9: Using Iloc To Access Rows By Position
#Assign the first ten rows from new_titanic_survival to first_ten_rows.
first_ten_rows = new_titanic_survival.iloc[0:10]
#Assign the fifth row from new_titanic_survival to row_position_fifth.
row_position_fifth = new_titanic_survival.iloc[4]
#Assign the row with index label 25 from new_titanic_survivalto row_index_25.
row_index_25 = new_titanic_survival.loc[25]

#Assign the value at row index label 1100, column index label "age" from new_titanic_survival to row_index_1100_age.
row_index_1100_age=new_titanic_survival.loc[1100,"age"]
#Assign the value at row index label 25, column index label "survived" from new_titanic_survival to row_index_25_survived.
row_index_25_survived=new_titanic_survival.loc[25,"survived"]
#Assign the first 5 rows and first three columns from new_titanic_survival to five_rows_three_cols.
five_rows_three_cols=new_titanic_survival.iloc[0:5,0:3]  


##11: Reindexing Rows
#Sometimes it's useful to reindex, starting from 0. We can use the DataFrame.reset_index() method to do this.
#By default, the method retains the old index by adding an extra column to the dataframe with the old index values.

#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reset_index.html

#Reindex the new_titanic_survival dataframe so the row indexes start from 0, and the old index is dropped.
titanic_reindexed=new_titanic_survival.reset_index(drop=True)
print(titanic_reindexed.iloc[0:5,0:3])


##12: Apply Functions Over A DataFrame
#To perform a complex calculation across pandas objects, we'll need to learn about the DataFrame.apply() method. 
#By default, DataFrame.apply() will iterate through each column in a DataFrame, and perform on each function

# This function returns the hundredth item from a series
def hundredth_row(column):
    # Extract the hundredth item
    hundredth_item = column.iloc[99]
    return hundredth_item

# Return the hundredth item from each column
hundredth_row = titanic_survival.apply(hundredth_row)

#Write a function that counts the number of null elements in a Series.
import pandas as pd 
def isnull(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)

column_null_count = titanic_survival.apply(isnull)


##13: Applying A Function To A Row
def which_class(row):
    pclass = row['pclass']
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    else pclass == 3:
        return "Third Class"

classes = titanic_survivors.apply(which_class, axis=1)



import pandas as pd

def generate_age_label(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"

age_labels = titanic_survival.apply(generate_age_label, axis=1)
