## Metrics for classification : Confusion Matrix / K-nn

# Import necessary modules
from sklearn.metrics import classification_report, confusion_matrix
# Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state = 42)
# Instantiate a k-NN classifier: knn
knn = KNeighborsClassifier(n_neighbors=6)
# Fit the classifier to the training data
knn.fit(X_train,y_train)
# Predict the labels of the test data: y_pred
y_pred = knn.predict(X_test)
# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


#PRECISION : TP / TP + FP [ Bien prédit / Prédit Spamé ]

#RECALL : TP / TP + FN [ Bien prédit / En réalité Spamé ]

#F1 score : 2 * ( (Precision * Recall) / (Precision + Recall))




## HYPERPARAMETERS

# Import necessary modules
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Setup the hyperparameter grid
c_space = np.logspace(-5, 8, 15)
param_grid = {'C': c_space}

# Instantiate a logistic regression classifier: logreg
logreg = LogisticRegression()

# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

# Fit it to the data
logreg_cv.fit(X,y)

# Print the tuned parameters and score
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_)) 
print("Best score is {}".format(logreg_cv.best_score_))

#retourne :
#Tuned Logistic Regression Parameters: {'C': 3.7275937203149381}
 #   Best score is 0.7708333333333334

# It looks like a 'C' of 3.727 results in the best performance.

## Hyperparameter tuning with RandomizedSearchCV
#not all hyperparameter values are tried out. 
#Instead, a fixed number of hyperparameter settings is sampled from specified probability distributions

# Import necessary modules
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV

# Setup the parameters and distributions to sample from: param_dist
param_dist = {"max_depth": [3, None],
              "max_features": randint(1, 9),
              "min_samples_leaf": randint(1, 9),
              "criterion": ["gini", "entropy"]}

# Instantiate a Decision Tree classifier: tree
tree = DecisionTreeClassifier()

# Instantiate the RandomizedSearchCV object: tree_cv
tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)

# Fit it to the data
tree_cv.fit(X,y)

# Print the tuned parameters and score
print("Tuned Decision Tree Parameters: {}".format(tree_cv.best_params_))
print("Best score is {}".format(tree_cv.best_score_))

##output
#   Tuned Decision Tree Parameters: {'criterion': 'entropy', 'max_features': 7, 'max_depth': 3, 'min_samples_leaf': 8}
 #   Best score is 0.7291666666666666

#Note that RandomizedSearchCV will never outperform GridSearchCV. Instead, it is valuable because it saves on computation time
