#The three key data structures in pandas are:

  ##Series objects (collections of values)
  ##DataFrames (collections of Series objects)
  ##Panels (collections of DataFrame objects)
  
  
 #Series objects use NumPy arrays for fast computation, but add valuable features to them for analyzing data. 
 #While NumPy arrays use an integer index, for example, Series objects can use other index types, such as a string index.
 
 
 
 ##2: Integer Indexes
 
 fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango["FILM"]
print(series_film[0:5])
                       
series_rt = fandango['RottenTomatoes']
print(series_rt[0:5])


##3: Custom Indexes

