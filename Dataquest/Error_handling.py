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
    parts= item[2].split("-")
    birth_years.append(parts[0])
