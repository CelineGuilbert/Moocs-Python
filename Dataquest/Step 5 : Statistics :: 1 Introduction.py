fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]
degrees_zero = [i+459.67 for i in fahrenheit_degrees] 
population_zero = yearly_town_population



# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey_scale = ["none", "a few", "some", "a lot"]
survey_numbers = [survey_scale.index(response)
 for response in survey_responses] #retourne : [0, 2, 3, 0, 1, 0, 0]
average_smoking = sum(survey_numbers) / len(survey_numbers)  
    

#Compute the average savings for everyone who is "male". Assign the result to male_savings.
#Compute the average savings for everyone who is "female". Assign the result to female_savings.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]


male_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "male"]
female_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "female"]

male_savings = sum(male_savings_list) / len(male_savings_list)
female_savings = sum(female_savings_list) / len(female_savings_list
         
                                                
                                                
                                                
## Histogramm
                                                
# Let's say that we watch cars drive by and calculate average speed in miles per hour
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed)
plt.show()                           
# Let's say we measure student test scores from 0-100
student_scores = [15, 80, 95, 100, 45, 75, 65]
plt.hist(student_scores)
                                                
plt.hist(average_speed, bins=2)
plt.show()
                                                
                                                
##Measuring Data Skew
#Skew refers to asymmetry in the data. When data is concentrated on the right side of the histogram, for example, we say it has
#a negative skew. When the data is concentrated on the left, we say it has a positive skew. 
                                                
# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.                                               
from scipy.stats import skew
positive_skew=skew(test_scores_positive)
negative_skew=skew(test_scores_negative)
no_skew=skew(test_scores_normal)
                                                
##Checking For Outliers With Kurtosis
#Kurtosis measures whether the distribution is short and flat, or tall and skinny. 
#In other words, it assesses the shape of the peak.                                                
#A high kurtosis may indicate problems with outliers (very large or very small values that skew the data).
                                                
# We can measure kurtosis with the kurtosis function.
# Negative values indicate platykurtic distributions, positive values indicate leptokurtic distributions, and values near 0 are mesokurtic.
from scipy.stats import kurtosis
kurt_platy=kurtosis(test_scores_platy)
kurt_lepto=kurtosis(test_scores_lepto)
kurt_meso=kurtosis(test_scores_meso)
 
                                                
                                                
# We can do the same with the positive side.
# Notice how the very high values pull the mean to the right more than we would expect.
plt.hist(test_scores_positive)
plt.axvline(test_scores_positive.mean())
plt.show()
mean_normal = test_scores_normal.mean()
mean_negative = test_scores_negative.mean()
mean_positive = test_scores_positive.mean()
   
                                                
                                                
                                                
##MEDIAN
# Let's plot the mean and median side-by-side in a negatively skewed distribution.
# Unfortunately, arrays don't have a nice median method, so we have to use a numpy function to compute it.
import numpy
import matplotlib.pyplot as plt

# Plot the histogram
plt.hist(test_scores_negative)
# Compute the median
median = numpy.median(test_scores_negative)

# Plot the median in blue (the color argument of "b" means blue)
plt.axvline(median, color="b")

# Plot the mean in red
plt.axvline(test_scores_negative.mean(), color="r")

# Notice how the median is further to the right than the mean.
# It's less sensitive to outliers, and isn't pulled to the left.
plt.show()                                

                                                
                                                
                                                
##DROP NAN values to a DF
 
new_titanic_survival = titanic_survival.dropna(subset=["age",'sex'])

 
##recap
mean_age = new_titanic_survival['age'].mean()
median_age=new_titanic_survival['age'].median()

from scipy.stats import skew,kurtosis
skew_age=skew(new_titanic_survival['age'])
kurtosis_age=kurtosis(new_titanic_survival['age'])
                            
                                                
                                                
                                                
                                                
##Standard Deviation
# Make a list of values
values = [2, 4, 5, -1, 0, 10, 8, 9]
# Compute the mean of the values
values_mean = sum(values) / len(values)
# Find the difference between each of the values and the mean by subtracting the mean from each value.
differences = [i - values_mean for i in values]
# This equals 0.  If you'd like, try changing the values around to verify that it still equals 0.
print(sum(differences))

# We can use the median function from numpy to find the median.
# The median is the "middle" value in a set of values. If we sort the values in order, it's the one in the center (or the average of the two in the center if there are an even number of items in the set).
# You'll see that the differences from the median don't always add up to 0.  You might want to play around with this and think about why that is.
from numpy import median
values_median = median(values)
median_difference_sum = [i - values_median for i in values]                                               
       
                                                
                                                
                                                
#compute Variance
                                                
import matplotlib.pyplot as plt
import pandas as pd
# We've already loaded the NBA data into the nba_stats variable.
# Find the mean value of the column.
pf_mean = nba_stats["pf"].mean()
# Initialize variance at zero.
variance = 0
# Loop through each item in the "pf" column.
for p in nba_stats["pf"]:
    # Calculate the difference between the mean and the value.
    difference = p - pf_mean
    # Square the difference. This ensures that the result isn't negative.
    # If we didn't square the difference, the total variance would be zero.
    # ** in python means "raise whatever comes before this to the power of whatever number is after this."
    square_difference = difference ** 2
    # Add the difference to the total.
    variance += square_difference
# Average the total to find the final variance.
variance = variance / len(nba_stats["pf"])

 
                                                
                                                
                                                
#ith a function
                                               
def std(var):
    var_mean = var.mean()
    variance=0
    for i in var:
        difference = i - var_mean
        square_difference = difference ** 2
        variance += square_difference
    result=(variance / len(var)) ** (1/2)
    return(result)

mp_dev = std(nba_stats['mp'])
ast_dev = std(nba_stats['ast'])
                                                
                                                
                                                
