#NumPy is much easier to work with than lists of lists, because:

#It's easy to perform computations on data.
#Data indexing and slicing is faster and easier.
#We can convert data types quickly.


#Overall, NumPy makes working with data in Python much more efficient. It's widely used for this reason, especially for machine learning.

#You may have noticed some limitations with NumPy as you worked through the past two missions, though. For example:
    #All of the items in an array must have the same data type. For many datasets, this can make arrays cumbersome to work with.
    #Columns and rows must be referred to by number, which gets confusing when you go back and forth from column name to column number.


import csv
f = open("world_alcohol.csv")
reader = csv.reader(f)
world_alcohol = list(reader)

years = []
for row in world_alcohol:
    years.append(row[0])

years = years[1:]

total = 0
for year in years:
    total = total + float(year)

avg_year = total / len(years)


#NumPy is a Python module that is used to create and manipulate multidimensional arrays.

#An array is a collection of values. Arrays have one or more dimensions. An array dimension is the number of indices it takes to extract
#a value. 
#Each value in a NumPy array has to have the same data type
#In a list, we specify a single index, so it is one-dimensional:
#A list is similar to a NumPy one-dimensional array, or vector, because we only need a single index to get a value.
first_row =  [1986, "Western Pacific", "Viet Nam", "Wine", 0]
print(first_row[0])


#The code would read in the nfl.csv file into a NumPy array. 
#NumPy arrays are represented using the numpy.ndarray class. We'll refer to ndarray objects as NumPy arrays in our material.
import numpy
nfl = numpy.genfromtxt("nfl.csv", delimiter=",")

#Create Array
vector = numpy.array([10, 20, 30])
matrix= numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
#visualiser le shape
matrix_shape = matrix.shape
#visualiser le type d'un array
world_alcohol_dtype = world_alcohol.dtype


#Reading In The Data Properly
    #u75 =  This specifies that we want to read in each value as a 75 byte unicode data type
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=1)
print(world_alcohol)



#Assign the whole third column from world_alcohol to the variable countries.
#Assign the whole fifth column from world_alcohol to the variable alcohol_consumption.

countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]



#Assign all the rows and the first 2 columns of world_alcohol to first_two_columns.
# attention, non inclusive
first_two_columns= world_alcohol[:,0:2]


#Selecting Elements
#Compare the third column of world_alcohol to the string Algeria.
#Assign the result to country_is_algeria.
#Select only the rows in world_alcohol where country_is_algeria is True.
#Assign the result to country_algeria.

country_is_algeria = world_alcohol[:,2] == "Algeria" #renvoie true ou false pour chaque élément
country_algeria=world_alcohol[country_is_algeria]


#replacing

world_alcohol[:,0][world_alcohol[:,0] == '1986'] = '2014'
world_alcohol[:,3][world_alcohol[:,3] == 'Wine'] = 'Grog'

#converting data type 
#We can convert the data type of an array with the astype() method.
vector = numpy.array(["1", "2", "3"])
vector = vector.astype(float)


#Calculate Mean et Sum, Warning : only with float array

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()


#Create a matrix called canada_1986 that only contains the rows in world_alcohol where the first column is the string 1986 
#and the third column is the string Canada.
#Extract the fifth column of canada_1986, replace any empty strings ('') with the string 0, 
#and convert the column to the float data type. Assign the result to canada_alcohol.
#Compute the sum of canada_alcohol. Assign the result to total_canadian_drinking

is_canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == '1986')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,4]
empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = "0"
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()


##Calculating Consumption For Each Country
#Now that we know how to calculate the average consumption of all types of alcohol for a single country and year, we can scale up the process and make the same calculation for all countries in a given year. Here's a rough process:

#Create an empty dictionary called totals.
#Select only the rows in world_alcohol that match a given year. Assign the result to year.
#Loop through a list of countries. For each country:
#Select only the rows from year that match the given country.
#Assign the result to country_consumption.
#Extract the fifth column from country_consumption.
#Replace any empty string values in the column with the string 0.
#Convert the column to the float data type.
#Find the sum of the column.
#Add the sum to the totals dictionary, with the country name as the key.
#After the code executes, you'll have a dictionary containing all of the country names as keys, with the associated alcohol consumption totals as the values.


totals = {}
is_year = world_alcohol[:,0] == "1989"
year = world_alcohol[is_year,:]

for country in countries:
    is_country = year[:,2] == country
    country_consumption = year[is_country,:]
    alcohol_column = country_consumption[:,4]
    is_empty = alcohol_column == ''
    alcohol_column[is_empty] = "0"
    alcohol_column = alcohol_column.astype(float)
    totals[country] = alcohol_column.sum()
    
    
##Finding The Country That Drinks The Most
#Now that we've computed total alcohol consumption for each country in 1989, we can loop through the totals dictionary to find the country with the highest value.

#The process we've outlined below will help you find the key with the highest value in a dictionary:

#Create a variable called highest_value that will keep track of the highest value. Set its value to 0.
#Create a variable called highest_key that will keep track of the key associated with the highest value. Set its value to None.
#Loop through each key in the dictionary.
#If the value associated with the key is greater than highest_value, assign the value to highest_value, and assign the key to highest_key.
#After the code runs, highest_key will be the key associated with the highest value in the dictionary.


highest_value = 0
highest_key = None
for country in totals:
    consumption = totals[country]
    if highest_value < consumption:
        highest_value = consumption
        highest_key = country
        
    


