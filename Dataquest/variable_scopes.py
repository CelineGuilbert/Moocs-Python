##2: Built-In Functions
#Use the sum() function to add 6 and 11 and assign the result to total.
total = sum([6,11]) #Remember that in order to use the sum() function, you have to pass in a list

##4: Scopes
#When we write functions, we're writing reusable blocks of code. This means that no matter what's happening with the rest of the code 
#we write, the function should operate in exactly the same way each time.

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

total = sum(borrower_default_count_240)
average= find_average(principal_outstanding_240)
print(total)




##9: Global Variables
#Global variables are variables that are available across all scopes.
#We can access and change the value of a global variable inside any global scope or local scope.

def test_function():
    global a
    a = 10

test_function()
print(a)
