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
fig = plt.figure(figsize=(12, 12)) # figsize=(width,height) of each graphic

for sp in range(0,4): #4 pck il y a 4 modalités dans major_cats donc on demande 4 graphiques
    ax = fig.add_subplot(2,2,sp+1)  #= subplot layout, ici deux graphs par ligne donc 2 lignes / 2 colonnes
                                    #  pour avoir les graph sur une seule ligne (1,4,sp+1)
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
    ax = fig.add_subplot(2,2,sp+1) #the subplot layout 
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


# Setting Line Color Using RGB
cb_orange = (255/255,128/255,14/255)
 ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c=cb_orange, label='Men')
# Setting Line Width
 ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c=cb_orange, label='Men', linewidth=3)
  
  
 #Annotating In Matplotlib

  #Add the following text annotations in the leftmost chart:
    #The string "Men" at the x-axis coordinate of 2005 and the y-axis coordinate of 87.
    #The string "Women" at the x-axis coordinate of 2002 and the y-axis coordinate of 8.
  #Add the following text annotations in the rightmost chart:
    #The string "Men" at the x-axis coordinate of 2005 and the y-axis coordinate of 62.
    #The string "Women" at the x-axis coordinate of 2001 and the y-axis coordinate of 35.


fig = plt.figure(figsize=(18, 3))
for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    if sp == 0:
            ax.text(2005,87,"Men")
            ax.text(2002,8,"Women")
    if sp == 5:
            ax.text(2005,62,"Men")
            ax.text(2001,35,"Women")
plt.show()
