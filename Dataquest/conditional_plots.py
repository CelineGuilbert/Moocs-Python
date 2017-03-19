import pandas as pd

titanic = pd.read_csv('train.csv')
titanic = titanic[["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
titanic = titanic.dropna()


####################### #Seaborn
##http://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid
  
  

#To get familiar with seaborn, we'll start by creating the familiar histogram. We can generate a histogram of the Fare column using 
#the seaborn.distplot() function:
# seaborn is commonly imported as `sns`.
import seaborn as sns
sns.distplot(titanic["Fare"])
plt.show()

#Under the hood, seaborn creates a histogram using matplotlib, scales the axes values, and styles it. In addition, seaborn uses a technique
#called kernel density estimation, or KDE for short, to create a smoothed line chart over the histogram. If you're interested in learning
#about how KDE works, you can read more on Wikipedia.

#Generating A Kernel Density Plot
#While having both the histogram and the kernel density plot is useful when we want to explore the data,
#it can be overwhelming for someone who's trying to understand the distribution.
#To generate just the kernel density plot, we use the seaborn.kdeplot() function:
sns.kdeplot(titanic["Fare"])

import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(titanic['Age'], shade=True) # we can shade the area under the line by setting the shade parameter to True.
plt.xlabel('Age')


##Modifying The Appearance Of The Plots
#Set the style to the style sheet that hides the coordinate grid and sets the background color to white.
#Generate a kernel density plot of the "Age" column, with the area under the curve shaded.
#Despine all of the axes.

sns.set_style("white")
sns.kdeplot(titanic['Age'], shade=True)
sns.despine(left=True, bottom=True)
plt.xlabel('Age')

##Conditional Distributions Using A Single Condition

#In seaborn, we can create a small multiple by specifying the conditioning criteria and the type of data visualization we want.
#For example, we can visualize the differences in age distributions between passengers who survived and those who didn't by creating a
#pair of kernel density plots.

# Condition on unique values of the "Survived" column.
g = sns.FacetGrid(titanic, col="Survived", size=6)
# For each subset of values, generate a kernel density plot of the "Age" columns.
g.map(sns.kdeplot, "Age", shade=True)

#Instead of subsetting the data and generating each plot ourselves, seaborn allows us to express the plots we want as parameter values. 
#The seaborn.FacetGrid object is used to represent the layout of the plots in the grid and the columns used for subsetting the data. 
#The word "facet" from FacetGrid is another word for "subset"
#Once we've created the grid, we use the FacetGrid.map() method to specify the plot we want for each unique value of Survived. 
#Seaborn generated one kernel density plot for the ages of passengers that survived and one kernel density plot for the ages of 
#passengers that didn't survive.

g = sns.FacetGrid(titanic, col="Survived", size=6)
g.map(plt.hist, "Age")

#exemple with Pclass -> KDE Age

g = sns.FacetGrid(titanic, col="Pclass", size=6)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True,bottom=True)
plt.show()

##Creating Conditional Plots Using Two Conditions
#When creating a FacetGrid, we use the row parameter to specify the column in the dataframe we want used to subset across the rows in
#the grid. 

g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

##Creating Conditional Plots Using Three Conditions
#When subsetting data using two conditions, the rows in the grid represented one condition while the columns represented another. 
#We can express a third condition by generating multiple plots on the same subplot in the grid and color them differently. 
#Thankfullg = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex", size=3)

  #Use a FacetGrid instance to generate a grid of plots using the following conditions:
   #The Survived column across the columns in the grid.
   #The Pclass column across the rows in the grid.
   #The Sex column using different hues.

g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()y, we can add a condition just by setting the hue parameter to the column name from the dataframe.

##Adding A Legend
##options : http://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid
g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex", size=3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)
plt.show()



