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
