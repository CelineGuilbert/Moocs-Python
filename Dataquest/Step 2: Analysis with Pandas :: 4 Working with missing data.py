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
