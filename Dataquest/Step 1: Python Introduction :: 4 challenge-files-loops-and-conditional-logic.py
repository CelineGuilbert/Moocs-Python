#Create a new list of lists called numerical_list where:
#The element at index 0 for each list is the unisex name (as a string)
#The element at index 1 for each list is the number of people who share that name (as a float)
#To accomplish this:
#"Create an empty list and assign it to numerical_list.
#Write a for loop that iterates over nested_list. In the loop body:
Retrieve the element at index 0 and assign it to a variable.
Retrieve the element at index 1, convert it to a float, and assign it to a variable.
Create a new list containing these two elements (in the same order).
Use the append() method to add this new list to numerical_list.
Finally, display the first five elements in numerical_list.


print(nested_list[0:5])

numerical_list = []
for nl in nested_list:
    name = nl[0]
    nb = float(nl[1])
    new_list = [name, nb]
    numerical_list.append(new_list)

print(numerical_list[0:5])




#Create a new list of strings called thousand_or_greater that only contains the names shared by 1,000 people or more.
#To accomplish this:
#Create an empty list and assign it to thousand_or_greater.
#Write a for loop that iterates over numerical_list.
#In the loop body, use an if statement to determine if the value at index 1 for that element (which is a list) is greater than or equal to 1000.
#If the value is greater than or equal to 1000, use the append() method to add its name to thousand_or_greater.
"Finally, display the first 10 elements in thousand_or_greater.
# The last value is ~100 people


numerical_list[len(numerical_list)-1]
thousand_or_greater = []

for nl in numerical_list:
    if nl[1]>=1000:
        thousand_or_greater.append(nl[0])
 print(thousand_or_greater[0:10])      
        
        
#Parsing The File
#Open it with the open() function. This will return a File object.
"Read the open file into a variable using the read() method. This will return in a string.
"Split the data into rows on the newline character (\n). This will result in a list.
"Loop through each row, and split each row into a list on the comma character (,). This will result in a list of lists.
        
weather_data = []
f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)
    
