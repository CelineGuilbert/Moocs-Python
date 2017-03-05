#first and last element --  d'une série
weather[0]
weather[-1]

#A dictionary is like a list in that it has indexes, but the indexes aren't necessarily sequential numbers. 
We can create our own indexes with values of any data type, including strings.

#While we initiate a new list with square brackets ([),
#we create a new dictionary with curly braces ({).
#We can make an empty dictionary like this: scores = {}


# Assign the value 1 to the key Aquaman in a new dictionary named superhero_ranks.
superhero_ranks = {}
superhero_ranks["Aquaman"] = 1
superhero_ranks["Superman"] = 2

# Look for values in dictionnary : using square brackets
president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3

fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]



# Create a didctionnary more faster :
students = {
    "Tom": 60,
    "Jim": 70
}

animals = {7 : "raven", 8 : "goose", 9 : "duck" }
times= {"morning" : 9, "afternoon" : 14, "evening" : 19, "night" : 23}


# Modifying dictionnary values

1. Add the key Ann and value 85 to the dictionary students.
2. Replace the value for the key Tom with 80.
3. Add 5 to the value for the key Jim.

students = {
    "Tom": 60,
    "Jim": 70
}

students['Ann'] = 85
students["Tom"] = 80
students["Jim"] = students['Jim'] + 5



#The In Statement And Dictionaries
#we used the in statement to check whether an element occurred in a list:

students = {
    "Tom": 60,
    "Jim": 70
}

"Tom" in students would return True, and "Sue" in students would return in False.



#Append any names in planet_names that are longer than 5 characters to long_names.
#Otherwise, append the names to short_names. To accomplish this:


planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for planet_name in planet_names:
    if len(planet_name) > 5:
        long_names.append(planet_name)
    else:
        short_names.append(planet_name)
