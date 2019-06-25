# -*- coding: utf-8 -*-

#changer le répertoire courant
import os
os.chdir("D:/DataMining/Databases_for_mining/dataset_for_soft_dev_and_comparison/regression/lasso")

#charger les données
import pandas
bb = pandas.read_excel("Baseball.xlsx",sheet_name=0)

#description
print(bb.shape)
print(bb.describe())

#subdivision
from sklearn.model_selection import train_test_split
bbTrain, bbTest = train_test_split(bb,train_size = 200,random_state=69780)

#vérifications
print(bbTrain.shape)
print(bbTest.shape)

#matrice des explicatives
XTrain = bbTrain.iloc[:,:16]
print(XTrain.shape)

#à laquelle est ajoutée la constante
import statsmodels.api as sm
X1Train = sm.add_constant(XTrain)

#vérification
print(X1Train.head())

#vecteur cible
yTrain = bbTrain.iloc[:,16]

#lancer la régression
reg = sm.OLS(yTrain,X1Train)
resReg = reg.fit()

#affichage
print(resReg.summary())

#matrice des descripteurs pour échantillon test
XTest = bbTest.iloc[:,:16]
X1Test = sm.add_constant(XTest)

#appliquer le modèle
ypReg = reg.predict(resReg.params,X1Test)
print(ypReg)

#y obs. sur l'échantillon test
yTest = bbTest.iloc[:,16]

#librairie numpy
import numpy

#graphique
import matplotlib.pyplot as plt
plt.scatter(yTest,ypReg)
plt.plot(numpy.arange(4,10,0.5),numpy.arange(4,10,0.5))
plt.xlabel("Observed values")
plt.ylabel("Predicted values")
plt.show()

#mesurer le MSE
from sklearn.metrics import mean_squared_error
print(mean_squared_error(yTest,ypReg))

#vérification
print(numpy.mean((yTest-ypReg)**2))

#centrer et réduire les données d'apprentissage
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
ZTrain =sc.fit_transform(bbTrain)

#moyennes des variables
print(sc.mean_)

#variance des variables
print(sc.var_)

#affichage des moyennes après transformations
print(numpy.mean(ZTrain,axis=0))

#affichage des variances itou
print(numpy.var(ZTrain,axis=0))

#régression Lasso, paramètres par défaut (alpha  = 1.0)
from sklearn.linear_model import Lasso
regLasso1 = Lasso(fit_intercept=False,normalize=False)
print(regLasso1)

#apprentissage
regLasso1.fit(ZTrain[:,:16],ZTrain[:,16])

#les coefficients
print(regLasso1.coef_)

#lasso path (valeurs de alpha à tester)
my_alphas = numpy.array([0.001,0.01,0.02,0.025,0.05,0.1,0.25,0.5,0.8,1.0])

#obtention des valeurs des coefs. corresp.
from sklearn.linear_model import lasso_path
alpha_for_path, coefs_lasso, _ = lasso_path(ZTrain[:,:16],ZTrain[:,16],alphas=my_alphas)

#dim. matrice des coefficients
print(coefs_lasso.shape)

#alpha utilisés
print(alpha_for_path)

#jeu de couleurs pour faire joli
import matplotlib.cm as cm
couleurs = cm.rainbow(numpy.linspace(0,1,16))

#graphique lasso path (une courbe par variable)
for i in range(coefs_lasso.shape[0]):
    plt.plot(alpha_for_path,coefs_lasso[i,:],c=couleurs[i])
    
plt.xlabel('Alpha')
plt.ylabel('Coefficients')
plt.title('Lasso path')
plt.show()

#nombre de coefs. non-nuls pour chaque alpha
nbNonZero = numpy.apply_along_axis(func1d=numpy.count_nonzero,arr=coefs_lasso,axis=0)
    
#affichage miexu roganisé alpha vs. nombre de coefs non-nuls 
print(pandas.DataFrame({'alpha':alpha_for_path,'Nb non-zero coefs':nbNonZero}))

#ou sous forme graphique
plt.plot(alpha_for_path,nbNonZero)
plt.xlabel('Alpha')
plt.ylabel('Nb. de variables')
plt.title('Nb. variables vs. Alpha')
plt.show()
 
#nom des variables
nom_var = bb.columns[:16]

#coefficients pour alpha=0.25 (colonne n°3)
coefs25 = coefs_lasso[:,3]

#affichage des coefficients  pour alpha = 0.25
print(pandas.DataFrame({'Variables':nom_var,'Coefficients':coefs25}))

#validation croisée pour Lasso
from sklearn.linear_model import LassoCV

#outil pour la détection de la solution la plus performante en validation croisée
lcv = LassoCV(alphas=my_alphas,normalize=False,fit_intercept=False,random_state=0,cv=5)
    
#lancement sur l'échantillon d'apprentissage
lcv.fit(ZTrain[:,:16],ZTrain[:,16])    

#valeurs des alphas qui ont été testés
print(lcv.alphas_)

#valeurs des MSE en validation croisée
print(lcv.mse_path_)

#moyenne mse en validation croisée pour chaque alpha
avg_mse = numpy.mean(lcv.mse_path_,axis=1)

#alphas vs. MSE en cross-validation
print(pandas.DataFrame({'alpha':lcv.alphas_,'MSE':avg_mse}))

#sous-forme graphique
plt.plot(lcv.alphas_,avg_mse)
plt.xlabel('Alpha')
plt.ylabel('MSE')
plt.title('MSE vs. Alpha')
plt.show()

#best alpha
print(lcv.alpha_)

#transformation des variables des données test
ZTest = sc.transform(bbTest)

#prediction avec ce modèle
ypzLasso = lcv.predict(ZTest[:,:16])

#dé-standardization de la prédiction
ypLasso = ypzLasso*numpy.sqrt(sc.var_[-1]) + sc.mean_[-1]

#performances en prédiction
print(mean_squared_error(yTest,ypLasso))


### ******************************************************************
### NON décrit dans le tutoriel : la même chose mais avec GridSearchCV
### ******************************************************************

##outil pour la détection de la solution la plus performante en validation croisée
#from sklearn.model_selection import GridSearchCV
#clf = GridSearchCV(estimator=regLasso1,param_grid=parametres,scoring='neg_mean_squared_error',cv=5)
#clf.fit(ZTrain[:,:16],ZTrain[:,16])
#
##résultats
#print(pandas.DataFrame({'alpha':clf.cv_results_['param_alpha'],'MSE':-clf.cv_results_['mean_test_score']}))
#
##paramètre optimal
#print(clf.best_params_)
#
##sous-forme graphique
#plt.plot(my_alphas,-clf.cv_results_['mean_test_score'])
#plt.xlabel('Alpha')
#plt.ylabel('MSE')
#plt.title('MSE vs. Alpha')
#plt.show()
#
##transofmration des variables des données test
#ZTest = sc.transform(bbTest)
#
##utilisation du meilleur modèle pour la prédiction
#ypzLasso = clf.predict(ZTest[:,:16])
#
##dé-standardization de la prédiction
#ypLasso = ypzLasso*numpy.sqrt(sc.var_[-1]) + sc.mean_[-1]
#
##performances
#print(mean_squared_error(yTest,ypLasso))
