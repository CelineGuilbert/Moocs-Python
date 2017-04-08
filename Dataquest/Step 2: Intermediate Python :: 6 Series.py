##http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html#pandas.Series

##1. Data structures
#The three key data structures in pandas are:

  #Series objects (collections of values)
  #DataFrames (collections of Series objects)
  #Panels (collections of DataFrame objects)


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






