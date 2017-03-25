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
