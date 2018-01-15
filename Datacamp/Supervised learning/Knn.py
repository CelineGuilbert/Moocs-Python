● Basic idea: Predict the label of a data point by :
  ● Looking at the ‘k’ closest labeled data points
  ● Taking a majority vote




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

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)print("Prediction: {}".format(new_prediction))


