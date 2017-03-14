
f = open('US_births_1994-2003_CDC_NCHS.csv','r')
data = f.read()

rows = data.split('\n')
final_list=[]
for row in rows:
    split_list = row.split(',')
    final_list.append(split_list)
restrict_list= final_list[1:11]
final_list = final_list[1:-1]
   
    
# Calculating Number Of Births Each Month

#Create a function named month_births() that:
  #Takes a single, required argument, a list of lists.
  #Creates an empty dictionary, births_per_month, to store the monthly totals.
  #Uses a for loop to:
    #Iterate over the list of lists,
    #Extract the value in the month and births columns,
    #If the month value already exists as a key in births_per_month, the births value is added to the existing value,
    #If the month value doesn't exist as a key in births_per_month, it's created and the associated value is the births value.
  #After the loop, return the births_per_month dictionary.
#Use the month_births() function to calculate the monthly totals for the dataset and assign the result to cdc_month_births. Display the dictionary.


def month_births(listoflist):
    births_per_month={}
    for item in listoflist:
        month = item[1]
        births = int(item[4])
        if month in births_per_month:
            births_per_month[month] =  births_per_month[month] + births
        else:
            births_per_month[month] = births
    return(births_per_month)

cdc_month_births =month_births(final_list)
print(cdc_month_births)





#You may have noticed that there was a lot of similarity between the two functions you just wrote. 
#While we can also create separate functions to calculate the totals for the year and date_of_month columns, 
#it's better to create a single function that works for any column and specify the column we want as a parameter each time we call 
#the function.


def calc_counts(data, column):
    births_per_column = {}
    for item in data:
        births = int(item[4])
        col = item[column]
        if col in births_per_column:
            births_per_column[col] = births_per_column[col] + births
        else:
            births_per_column[col] = births
    return(births_per_column)          

cdc_year_births = calc_counts(final_list, 0)
cdc_month_births = calc_counts(final_list, 1)
cdc_dom_births = calc_counts(final_list, 2)
cdc_dow_births = calc_counts(final_list, 3)


