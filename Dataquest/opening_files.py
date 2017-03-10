# 1 - Opening Files

#To open a file in Python, we use the open() function. 
#This function accepts two different arguments (inputs) in the parentheses, always in the following order:
    #the name of the file (as a string)
    #the mode of working with the file (as a string) --- "r" = the mode for reading in files.

#The open() function returns a File object
open("story.txt", "r")
text = open("story.txt", "r")


# 2 - Readind Files

#File objects have a read() method that returns a string representation of the text in a file. 
#Unlike the append() method from the previous mission, the read() method returns a value instead of modifying the object 
#that calls the method.

    #Note that the File object, text, won't contain the actual contents of the file. 
    #It's instead an object that acts as an interface to the file
    #and contains methods for reading in and modifying the file's contents 

#<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
f = open("test.txt", "r")
g = f.read()


# 3 - To make our string object data more useful, let's convert it into a list. Here's a preview of how the dataset looks:
#Each line is separated by the string \n, which is referred to as the new-line character
    #Albuquerque,749\nAnaheim,371\nAnchorage,828\n
#the split() method to turn a string object into a list of strings

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows)


# 4 - Loops
#We now have a list representation of the dataset (rows). 
#Each element in the dataset is a string containing a comma (,) that separates the city name from the crime rate. 
#Because they're strings, we can use the split() method on each of them to separate those values. 


ten_rows = rows[0:10]

for item in ten_rows:
    print(item)
    
    
# 5 - List of Lists

#1. splits each element in three_rows (which contains the first three elements from rows) on the comma delimiter (,) -> String
#2. appends the resulting list (split_list) to a new list we create (final_list)  -> List
#3. displays the final list using the print() function

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []

for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])



# 6 - Splitting Elements In A List
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

final_data = []
for row in rows:
     # row is a list variable, not a string / Text is a string
    text  = row.split(',')
    #final_data is a list
    final_data.append(text)
print(final_data)
        
        
        
# 7 : Accessing Elements In A List Of Lists

#A list of lists has some unique interaction mechanisms. 
#Using bracket notation to retrieve an element at a certain index returns a list object. 
#However, using bracket notation on the resulting list will actually return a data point (such as a string or an integer).

print(five_elements) #List of List
            [['Albuquerque', '749'],
             ['Anaheim', '371'],
             ['Anchorage', '828'],
             ['Arlington', '503'],
             ['Atlanta', '1379']]
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
            #print crime_rates = ['749', '371', '828', '503', '1379']
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
