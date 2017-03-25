#2: Enumerate

animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]
viciousness = [1, 5, 10, 10, 1]

for animal in animals:
    print("Animal")
    print(animal)
    print("Viciousness")
    
#In the example above, we have two lists. 
#We want to retrieve the position of the item in animals the loop is currently on, 
#so we can use it to look up the corresponding value in the viciousness list.
#Unfortunately, we can't just loop through animals, and then tap into the second list. 
#Python has an enumerate() function that can help us with this, though.

#The enumerate() function allows us to have two variables in the body of a for loop -- an index, and the value.
    
ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i,ship in enumerate(ships):
    print(ship)
    print(cars[i])
    
    ##retour :    
    #Andrea Doria
    #Ford Edsel
    #Titanic
    #Ford Pinto
    #Lusitania
    #Yugo



##3: Adding Columns
things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i,thing in enumerate(things):
    thing.append(trees[i])
    
    ## retour de thing:
    #[['apple', 'monkey', 'cedar'],
    #['orange', 'dog', 'maple'],
    # ['banana', 'cat', 'fig']]



##4: List Comprehensions
animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]

animal_lengths = []
for animal in animals:
    animal_lengths.append(len(animal))

#replace by the syntax
animal_lengths = [len(animal) for animal in animals]

#Use list comprehension to create a new list called apple_prices_doubled, where you multiply each item in apple_prices by 2.
apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [price*2 for price in apple_prices]
#Use list comprehension to create a new list called apple_prices_lowered, where you subtract 100 from each item in apple_prices
apple_prices_lowered = [price-100 for price in apple_prices]

##6: None
values = [-50, -80, -100]
max_value = 0
for i in values:
    if i > max_value:
        max_value = i
##In the above scenario, max_value is 0 when the loop finishes.
#This is wrong, because 0 isn't in values; it's just a placeholder we used to initialize max_value.
#We can resolve this kind of issue using the None object, which has a special data type called NoneType.
#The None object indicates that the variable has no value. Rather than using the normal double equals sign (==) to check whether a 
#value equals None,we use the variable is None syntax.
values = [-50, -80, -100]
max_value = None
for i in values:
    if max_value is None or i > max_value:
        max_value = i
        
#Loop through each value in values.
#Check whether the value is not None, and if it's greater than 30.
#Append the result of the check to checks.
#When finished, checks should be a list of Booleans indicating whether or not the corresponding items in values are not None and 
#greater than 30.
values = [None, 10, 20, 30, None, 50]
checks = []

checks = [x is not None and x > 30 for x in values]
    ## checkslist (<class 'list'>)
    ##[False, False, False, False, False, True]

#Set max_value to None.
#Loop through the keys in name_counts.
#Assign the value associated with the key to count.
#If max_value is None, or count is greater than max_value:
#Assign count to max_value.
#At the end of the loop, max_value will contain the largest value in name_counts
max_value = None
for key in name_counts: #name_counts is a dict
    count = name_counts[key]
    if max_value is None or count > max_value:
        max_value = count

## 9: The Items Method
#The code we used on the previous screen to access the keys and values in a dictionary was slightly awkward. 
#We can simplify this process with the items() method, which allows us to iterate through keys and values at the same time.

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for key,value in plant_types.items():
    print(key)
    print(value)
    
#orchid
#flower
#cedar
#tree
#maple



##10: Finding The Most Common Female Names
#As we learned on a previous screen, the most common female names occur two times in name_counts
top_female_names = []
for key in name_counts:#name_counts is a dict
    if name_counts[key] == 2:
        top_female_names.append(key)

 ##Most commom Name for male
top_male_names = []
male_name_counts = {}
for row in legislators:
    if row[3] == "M" and row[7] > 1940:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[name] = male_name_counts[name] + 1
        else:
            male_name_counts[name] = 1

highest_value = None
for name,count in male_name_counts.items():
    if highest_value is None or count > highest_value:
        highest_value = count

for name,count in male_name_counts.items():
    if count == highest_value:
        top_male_names.append(name)
