# Import KNeighborsClassifier from sklearn.neighborsfrom sklearn.neighbors import KNeighborsClassifier
# Create arrays for the features and the response variabley = df['party'].valuesX = df.drop('party', axis=1).values
# Create a k-NN classifier with 6 neighborsknn = KNeighborsClassifier(n_neighbors=6)
# Fit the classifier to the dataknn.fit(X,y)
