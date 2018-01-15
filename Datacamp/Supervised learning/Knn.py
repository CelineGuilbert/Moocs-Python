# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y =df['party'].values
X =df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn =KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X,y)

#KNeighborsClassifier(algorithm='auto',
#leaf_size=30, metric='minkowski', metric_params=None, n_jobs=1, n_neighbors=6,
#p=2,  weights='uniform')




