# First graph

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
plt.plot(women_degrees['Year'],women_degrees['Biology'])
plt.show()

#Visualizing the gender gap

plt.plot(women_degrees['Year'], women_degrees['Biology'], c='blue', label='Women')
plt.plot(women_degrees['Year'], 100-women_degrees['Biology'], c='green', label='Men')
plt.tick_params(bottom = "off", top= "off", left= "off", right= "off")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc='upper right')
plt.show()
###
fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
# Add your code here
ax.spines["right"].set_visible(False)
ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()



##Comparing Gender Gap Across Degree Categories

#Generate a line chart using the women and men percentages for Biology in the top left subplot.
#Generate a line chart using the women and men percentages for Computer Science in the top right subplot.
#Generate a line chart using the women and men percentages for Engineering in the bottom left subplot.
#Generate a line chart using the women and men percentages for Math and Statistics in the bottom right subplot.

#For all subplots:
  #For the line chart visualizing female percentages, set the line color to "blue" and the label to "Women".
  #For the line chart visualizing male percentages, set the line color to "green" and the label to "Men".
  #Set the x-axis limit to range from 1968 to 2011.
  #Set the y-axis limit to range from 0 to 100.
  #Hide all of the spines and tick marks.
  #Set the title of each subplot to the name of the major category (e.g. "Biology", "Computer Science").
#Place a legend in the upper right corner of the bottom right subplot.
#Display the plot.


major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    # Add your code here.

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()



#improve precedent example by adding title of each graph and an unique x/y limit axis
major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()
