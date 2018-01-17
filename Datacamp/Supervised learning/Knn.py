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
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))





# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors): 
  
 # Setup a k-NN Classifier with k neighbors: knn   
knn = KNeighborsClassifier(n_neighbors=k)
 
# Fit the classifier to the training data   
knn.fit(X_train, y_train)        

#Compute accuracy on the training set    
train_accuracy[i] = knn.score(X_train, y_train)
#Compute accuracy on the testing set    
test_accuracy[i] =  knn.score(X_test, y_test)
# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()
