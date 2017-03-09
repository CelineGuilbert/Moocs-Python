#count item

#Count the number of items in weather. You can accomplish this by:
#Looping over each element in weather.
#Adding 1 to count for each element.
#When finished, count should equal the number of items in weather.


count = 0

for item in weather:
    count = count + 1
    
#The IN STATEMENT

animals = ["cat", "dog", "rabbit"]
for animal in animals:
    if animal == "cat":
        print("Cat found")
        
        
animals = ["cat", "dog", "rabbit"]
if "cat" in animals:
    print("Cat found")

animals = ["cat", "dog", "rabbit"]
cat_found = "cat" in animals

#Use the in statement to check whether the value cat is in the list animals, and assign the result to cat_found.
#Use the in statement to check whether the value space_monster is in the list animals, and assign the result to space_monster_found.
#animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

for animal in animals:
    cat_found = "cat" in animals
    space_monster_found =  "space_monster" in animals


#Loop through each item in the weather_types list.
#Check whether the item occurs in the new_weather list.
#Append the result of the check to weather_type_found.
#At the end, weather_type_found should be a list of Boolean values.

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for item in weather_types:
    found = item in new_weather
    weather_type_found.append(found)
    
    
    
    
    
weather_counts = {}
for item in weather:
       if item in weather_counts:
             weather_counts[item] =  weather_counts[item] + 1
       else:
              weather_counts[item] = 1



