## 2. SETS __ the set() function

#When exploring data, it's often useful to extract the unique elements in a list.
#The result of this conversion is a set - a data type where each element is unique. A set behaves very similarly to a list.

unique_animals = set(["Dog", "Cat", "Hippo", "Dog", "Cat", "Dog", "Dog", "Cat"])
print(unique_animals)
#We'll get {'Hippo', 'Cat', 'Dog'} as a result, Note that the interpreter encloses Sets in curly braces when it prints them.
#Because Sets don't have indexes, the items in a set may display in a different order each time you print it.

#You can add items to a set using the add() method:
unique_animals.add("Tiger")
unique_animals.remove("Dog") #or remove
list(unique_animals) #convert to a list


gender = []
for item in legislators:
    gender.append(item[3])

gender = set(gender)
print(gender)
##genderset (<class 'set'>)
##{'', 'F', 'M'}

## 4: Missing Values

#Create an empty list named birth_years.
#Loop through each item in legislators.
  #Split the value in the birthday column on the - character.
  #Assign the result to parts.
  #Extract the first item in parts and append it to birth_years.
#At the end, birth_years will be a list containing the birth years of all the legislators in legislators.

birth_years=[]
for item in legislators:
    parts= item[2].split("-") #parts est une liste /// item[2] est un str
    birth_years.append(parts[0])
    
    
##6: Try/Except Blocks
#int('') : The code above will cause a ValueError, because an empty string can't be converted to an integer.
try:
    int('')
except Exception:  #Exception is a Type
    print("There was an error")
#In the example above, the Python interpreter will try to run int(''), and generate a ValueError.
#Instead of stopping the code from executing, it will be handled by the except statement, which will print the message 
#There was an error.
#The Python interpreter will continue to run any lines of code that come after the except statement.
    
    
    
##7: Exception Instances
#When the Python interpreter generates an exception, it actually creates an instance of the Exception class.
#This class has certain properties that help us debug the error. 
#We can access the instance of the Exception class in the except statement body:
try:
    int('')
except Exception as exc:
    print(type(exc)) ##<class 'ValueError'>
    print(str(exc)) ##invalid literal for int() with base 10: ''
#In the example above, we use the as statement to assign the instance of the Exception class to the variable exc
