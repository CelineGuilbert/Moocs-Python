##http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html#pandas.Series

##1. Data structures
#The three key data structures in pandas are:

  #Series objects (collections of values)
  #DataFrames (collections of Series objects)
  #Panels (collections of DataFrame objects)

#https://github.com/fivethirtyeight/data/tree/master/fandango
fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango["FILM"]
print(series_film[0:5])


# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values
series_custom=Series(rt_scores,index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]


##4: Integer Index Preservation
series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]

fiveten = series_custom[5:10]
print(fiveten)
    ##retourne :
    ##The Water Diviner (2015)        63
    ##Irrational Man (2015)           42
    ##Top Five (2014)                 86
    ##Shaun the Sheep Movie (2015)    99
    ##Love & Mercy (2015)             89
    ##dtype: int64
    
##5: Reindexing
#We can use the reindex() method to sort series_custom alphabetically by film. To accomplish this, we need to:

#Return a list representation of the current index using tolist().
#Sort the index with sorted().
#Use reindex() to set the newly-ordered index.

original_index = series_custom.index // df.index()
sorted_index = sorted(original_index) ## by alphanumeric // sorted(list)
sorted_by_index = series_custom.reindex(sorted_index)  // df.reindex(list)



##6: Sorting

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
print(sc2[0:10])
print(sc3[0:10])



##7: Transforming Columns With Vectorized Operations

#exemple de normalisation:
series_normalized = (series_custom/20)
# Add each value with each other
np.add(series_custom, series_custom)
# Apply sine function to each value
np.sin(series_custom)
# Return the highest value (will return a single value, not a Series)
np.max(series_custom)


##8: Comparing And Filtering

criteria_one = series_custom > 50
criteria_two = series_custom < 75
#return Boolean Series objects.

#Return a filtered Series object named both_criteria that only contains the values where both criteria are true.
#Use bracket notation and the & operator to obtain this Series object.
criteria_one = series_custom > 50
criteria_two = series_custom < 75

both_criteria = series_custom[criteria_one & criteria_two]


##9: Alignment
#Both Series objects use the same custom string index, which they base on the film names. Use the Python arithmetic operators to return
#a new Series object, rt_mean, that contains the mean ratings from both critics and users for each film.
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean=(rt_critics + rt_users)/2





########################## DATAFRAMES ##########################

##2: Using Integer Indexes To Select Rows
# First five rows
fandango[0:5]
# From row at 140 and higher
fandango[140:]
# Just row at index 50
fandango.iloc[50]
# Just row at index 45 and 90
fandango.iloc[[45,90]]
#Return a dataframe containing just the first and last rows, and assign it to first_last.
first_last = fandango.iloc[[0,-1]]

##3: Using Custom Indexes
fandango = pd.read_csv('fandango_score_comparison.csv')
fandango_films=fandango.set_index("FILM", drop=False, inplace=False)
print(fandango.index)


##4: Using A Custom Index For Selection
# Slice using either bracket notation or loc[]
fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]

# Specific movie
fandango_films.loc['Kumiko, The Treasure Hunter (2015)']

# Selecting list of movies
movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
fandango_films.loc[movies]


##5: Apply() Logic Over The Columns In A Dataframe
  
import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(deviations)


double_df = float_df.apply(lambda x: x*2)
print(double_df.head(1))
halved_df=float_df.apply(lambda x: x/2)
print(halved_df.head(1))


##7: Apply() Over Dataframe Rows

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
print(rt_mt_means[0:5])



##Delete NAN values to specific columns

new_titanic_survival = titanic_survival.dropna(subset=["age",'sex'])









