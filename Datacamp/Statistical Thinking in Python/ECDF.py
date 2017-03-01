#Empirical cumulative distribution function (ECDF)

#Computing the ECDF 

#data = <class 'sklearn.datasets.base.Bunch'>


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data) #retourne 5

    # x-data for the ECDF: x
    x = np.sort(data) #Return a sorted copy of an array. Tri les données

    # y-data for the ECDF: y
    y = np.arange( 1, n+1) / n #the end value in np.arange() is not inclusive 

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


##
##print(x_set)  #50 valeurs
#[ 1.   1.1  1.2  1.2  1.3  1.3  1.3  1.3  1.3  1.3  1.3  1.4  1.4  1.4  1.4
#  1.4  1.4  1.4  1.4  1.4  1.4  1.4  1.4  1.5  1.5  1.5  1.5  1.5  1.5  1.5
# 1.5  1.5  1.5  1.5  1.5  1.5  1.5  1.6  1.6  1.6  1.6  1.6  1.6  1.6  1.7
# 1.7  1.7  1.7  1.9  1.9]

##y_set : divise toutes les valeurs par 50
#[ 0.02  0.04  0.06  0.08  0.1   0.12  0.14  0.16  0.18  0.2   0.22  0.24
#  0.26  0.28  0.3   0.32  0.34  0.36  0.38  0.4   0.42  0.44  0.46  0.48
#  0.5   0.52  0.54  0.56  0.58  0.6   0.62  0.64  0.66  0.68  0.7   0.72
# 0.74  0.76  0.78  0.8   0.82  0.84  0.86  0.88  0.9   0.92  0.94  0.96
#  0.98  1.  ]
