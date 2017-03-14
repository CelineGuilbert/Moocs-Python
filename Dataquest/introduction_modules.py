#A module is a collection of functions and variables that have been bundled together in one file

#MATH MODULE

  #The sqrt() function inside the module takes a number as an argument, and returns the square root of that number. 
    #math.sqrt(4.0) would evaluate to 2.0, for example. 
  #The ceil() function returns the smallest integer that's greater than or equal to the input. In other words, it rounds the input up. 
  #The floor() function returns the largest integer that's less than or equal to the input. In other words, it rounds down.
  
import math
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)
print(c)


#CSV MODULE

  #We can work with CSV files more easily through the csv module. This module has a reader() function that takes a file object as
  #its argument, and returns an object that represents our data. We'll cover objects in more depth in the next mission, 
  #but for now, we'll simply convert this object to a list and use that result.
  #To read data from a file called "my_data.csv", we first import the csv module:
  
import csv

f = open("nfl.csv","r")
csvreader = csv.reader(f)
nfl = list(csvreader)

#
# [['2009', '1', 'Pittsburgh Steelers', 'Tennessee Titans'],
# ['2009', '1', 'Minnesota Vikings', 'Cleveland Browns'],
# ['2009', '1', 'New York Giants', 'Washington Redskins'],
# ['2009', '1', 'San Francisco 49ers', 'Arizona Cardinals']]
#




## Counting How Many Times A Team Won

#Imports and uses the csv module to load data from our "nfl.csv" file
#Counts how many games the "New England Patriots" won from 2009-2013
#To do this, set a counter to 0 and increment by 1 for each row that has "New England Patriots" in the winner column
#Assigns the count to patriots_wins



import csv

f = open('nfl.csv','r')
csvreader=csv.reader(f)
nfl = list(csvreader)

patriots_wins=0

for item in nfl:
    if item[2] == "New England Patriots":
            patriots_wins = patriots_wins + 1
            #patriots_wins += 1
