#Empirical cumulative distribution function (ECDF)

#Computing the ECDF 

#data = <class 'sklearn.datasets.base.Bunch'>


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data) #retourne 5

    # x-data for the ECDF: x
    x = np.sort(data) #Return a sorted copy of an array.

    # y-data for the ECDF: y
    y = np.arange( 1, n+1) / n #the end value in np.arange() is not inclusive # le résultat final ira de 0.2 à 1

    return x, y
  
  
# 1ere utilisation
# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()


# 2e utilisation de la fonction pour compiler plusieurs courbes de fonction cumulative sur un même graphique

# Compute ECDFs
x_set, y_set   = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)


# Plot all ECDFs on the same plot
plt.plot(x_set, y_set,marker=".",linestyle="none")
plt.plot(x_vers, y_vers,marker=".",linestyle="none")
plt.plot(x_virg, y_virg,marker=".",linestyle="none")

# Make nice margins
plt.margins(0.02)

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
