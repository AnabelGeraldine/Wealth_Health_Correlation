#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:22:24 2022

@author: anabelgeraldine

1. Clean dataset (dekete null rows) (done)
2. k-nearest
3. Eval

"""


import pandas as pd
from math import sqrt
from sklearn import metrics
from sklearn import neighbors
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


df = pd.read_csv('dataStage3.csv')
#print(df[['Suicide-2019','Income-2019','Death Crude-2019']])

X = df[['Suicide-2019','Income-2019']]         
y = df['Death Crude-2019']       
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
neigh = neighbors.KNeighborsRegressor(n_neighbors=5).fit(X_train, y_train)


sample = [20,200]
sample_pred = neigh.predict([sample])
print('----- Sample case -----')
#print("Region           :",df['Region'].where(df['colormap'] == sample[0]).unique()[1])
print("Suicide-2019     :",sample[0])
print("Income-2019      :",sample[1])
print('Predicted number of Death Crude:', int(sample_pred))
print('-----------------------')


y_pred = neigh.predict(X_test)
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
print('R-squared score:', metrics.r2_score(y_test, y_pred))


#model

n_neighbors = 5

for i, key in enumerate(["Suicide-2019", "Income-2019"]):
    knn = neighbors.KNeighborsRegressor(n_neighbors)
    X_test = X_test.sort_values(by=[key])
    #print(X_test)
    y_ = knn.fit(X_train, y_train).predict(X_test)
    plt.subplot(2, 1, i + 1)
    plt.scatter(X_test[key], y_test, color="darkorange", label="data")
    plt.plot(X_test[key], y_, color="navy", label="prediction")
    plt.axis("tight")
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, key = '%s')" % (n_neighbors, key))

plt.tight_layout()
plt.show()

