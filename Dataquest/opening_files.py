open("story.txt", "r")
text = open("story.txt", "r")

#<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
#"r" = the mode for reading in files.

#Note that the File object, text, won't contain the actual contents of the file. 
#It's instead an object that acts as an interface to the file
#and contains methods for reading in and modifying the file's contents 

#File objects have a read() method that returns a string representation of the text in a file

f = open("test.txt", "r")
g = f.read()


#fonction split piur convertir en liste

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows)

# List of Lists
#1. splits each element in three_rows (which contains the first three elements from rows) on the comma delimiter (,)
#2. appends the resulting list (split_list) to a new list we create (final_list)
#3. displays the final list using the print() function

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []

for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)


####
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

final_data = []
for row in rows:
    text  = row.split(',')
    final_data.append(text)
print(final_data)
        
        
        
#Accessing elements in a list after retreating

print(five_elements)
cities_list = []
cities_list.append(five_elements[0][0])
cities_list.append(five_elements[1][0])
cities_list.append(five_elements[2][0])
cities_list.append(five_elements[3][0])
cities_list.append(five_elements[4][0])


#With a loop

crime_rates = []
cities_list = []
for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
    
for row in final_data:
    citie_list = row[0]
    cities_list.append(citie_list)
print(cities_list)


# Challenge 
#Create a list of integers named int_crime_rates that contains just the crime rates - as integers - from the list rows.

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
int_crime_rates = []
for row in rows:
    values = row.split(',')
    crime_rate = int(values[1])
    int_crime_rates.append(crime_rate)
