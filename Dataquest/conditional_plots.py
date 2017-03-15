import pandas as pd

titanic = pd.read_csv('train.csv')
titanic = titanic[["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
titanic = titanic.dropna()


#Seaborn

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



