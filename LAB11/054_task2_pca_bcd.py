# -*- coding: utf-8 -*-
"""054_Task2_PCA_BCD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gqMxbUcyrEGkBJMUjqYeE3AvZne94sis
"""

'''
Author: Dhruv B Kakadiya

'''

# Commented out IPython magic to ensure Python compatibility.
# importing libraries

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# %matplotlib inline

# for dataset
from sklearn.datasets import load_breast_cancer

# for splitting training and testing part
from sklearn.model_selection import train_test_split

# for decompositions
from sklearn import decomposition
from sklearn import svm

main_data=load_breast_cancer()
main_data.keys()

X_train, X_test, y_train, y_test = train_test_split(main_data.data, main_data.target, random_state = 54, test_size = 0.2)
print(X_train.shape, X_test.shape)

pca = decomposition.PCA(n_components=2,whiten=True)
pca.fit(X_train)

print(pca.components_.shape)

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print(X_train_pca.shape)

print(X_test_pca.shape)

from sklearn import svm
clf = svm.SVC(C=5., gamma=0.001)
clf.fit(X_train_pca, y_train)

from sklearn import metrics
y_pred = clf.predict(X_test_pca)
print(metrics.classification_report(y_test, y_pred))
