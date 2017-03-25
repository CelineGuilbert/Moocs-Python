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

for i, animal in enumerate(animals):
    print("Animal Index")  ## label
    print(i)
    print("Animal") ## label
    print(animal)
    
    
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
