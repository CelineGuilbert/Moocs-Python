#A class is a template for new objects. So, if we have a Car class with color, make, and model properties, we can create many different
#instances of the Car class, and they will all have their own values for those properties. An instance is an object created from a 
#template, or class. black_honda_accord is an instance of the Car class. If we wanted to create a red_toyota_camry instance,
#we could do so, and it would have its own color, make, and model value


##3. Class Syntax
#For a class called Car(), we'd use class Car(): to start a class definition. 
#Inside the class, we define a special function called __init__. This is where we define our properties.

#The definition of our Car class looks like this:
class Car():
    def __init__(self):
        self.color = "black"
        self.make = "honda"
        self.model = "accord"
        
#By assigning values to color, make, and model within __init__, we indicate that we want our Car instances to have color, make, and model 
#properties with the default values we specified. These values are appropriate for our black_honda_accord instance, but we'll have to
#customize them for our red_toyota_camry instance.

## Exercice
#Create a class called Team.
#Inside the class, create a name property. Assign the value "Tampa Bay Buccaneers" to this property.
#Create an instance of the Team class, and assign it to the variable bucs.
#Print the name property of the bucs instance.

class Team():
    def __init__(self):
        self.name="Tampa Bay Buccaneers"

bucs = Team()
print(bucs.name)



## 4. Instance Methods And __init__
#In addition to properties, instances can also have behavior. We define this behavior using methods. 
#We actually just did this on the last screen. __init__ is a special method that the Python interpreter automatically calls whenever
#we create an instance of a class.

#Recall that __init__ takes in a self parameter. This parameter refers to the current instance, and allows us to access
#and add to its properties. self is passed in automatically when we call Team() (which calls __init__).

#We can add more parameters to __init__, and pass them in explicitly when we call Team(). 
#Suppose we want to add a name property to our Team class:

class Team():
    def __init__(self, name):
        self.name = name
        
# Add a name parameter to the __init__ method, and set the value of the self.name property to the name argument.
# Make an instance of the class, passing in the value "New York Giants" to the __init__ function (when you write Team()).
# Assign the result to the variable giants.    

class Team():
    def __init__(self,name):
        self.name = name
        
giants = Team("New York Giants")        



## 5: The Self Keyword
#Recall that we use the self keyword to add properties to a class.



##6: More Instance Methods
#Methods are very similar to functions, and we define them with the same syntax. 
#The only difference is that methods are "attached" to instances, while functions aren't. 
## original code
class Team():                    
    def __init__(self, name):
        self.name = name

## new method
    def print_name(self):       
        print(self.name)

        
#Add an instance method called count_total_wins to the definition for the Team class.
    #The method should take no arguments (except self), and should return the number of games the team won during 
    #the period this data set describes.
#Use the instance method to assign the number of wins by the "Denver Broncos" to broncos_wins.
#Use the instance method to assign the number of wins by the "Kansas City Chiefs" to chiefs_wins.        
import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

class Team():
    def __init__(self, name): #propriete de la classe
        self.name = name
    
    def print_name(self):
        print(self.name)

    def count_total_wins(self):
        count = 0
        for row in nfl:
            if row[2] == self.name:
                count = count + 1
        return count

broncos = Team("Denver Broncos")
broncos_wins = broncos.count_total_wins()

chiefs = Team("Kansas City Chiefs")
chiefs_wins = chiefs.count_total_wins()


## 7: Adding To The Init Function
#On the previous screen, we loaded the nfl variable for you outside of the Team class. 
#However, this approach isn't ideal. The purpose of classes is to organize our code, and a big part of organizing code is abstraction.

import csv
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)
      
    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
 
Jaguar = Team('Jacksonville Jaguars')
jaguars_wins = Jaguar.count_total_wins()



##8: Wins In A Year

import csv
class Team():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
    
    def count_total_wins_by_year(self):
        count_y = 0
        for row in self.nfl:
            if row[2] == self.name and row[0] == self.year:
                count_y=count_y+1
        return count_y
sf = Team("San Francisco 49ers","2013")
niners_wins_2013=sf.count_total_wins_by_year()
