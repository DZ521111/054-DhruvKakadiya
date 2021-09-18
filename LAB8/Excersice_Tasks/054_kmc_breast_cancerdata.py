# -*- coding: utf-8 -*-
"""054_KMC_Breast_CancerData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RZOX6-JyXBu_pWu9soopK_Qh98-JxOhr
"""

'''
Author: Dhruv B kakadiya

'''

# importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# for PCA Analysis
from sklearn.decomposition import PCA 

# model
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler

from sklearn import datasets

main_data = datasets.load_breast_cancer()
print(main_data)

print("\n\nShapes of data feature and target\n")
print(main_data.data.shape)
print(main_data.target.shape)

# analysing the features of data

print(main_data.feature_names)

import seaborn as sns

# converting numpy to pandas for graphs
df = pd.DataFrame(main_data.data, columns = main_data.feature_names)
df['class'] = main_data.target

sns.color_palette("husl", 8)
sns.pairplot(df.iloc[:, : 10])

# targets 
# 0 = benign
# 1 = malignant

print(main_data.target_names)

plt.scatter(main_data.data[:, 0], main_data.target, c = 'green', marker='.')
plt.xlabel('Features')
plt.ylabel('Type of Cancer')
plt.show()

# create a model
kmeans = KMeans(n_clusters = 4, random_state = 54)

# prediction
prediction = kmeans.fit_predict(main_data.data)
print(prediction)

# shapes of clusters

print("\n\nshapes of clustering!!!!\n\n")
print(kmeans.cluster_centers_.shape)

print("\n\nclusters\n\n")
print(kmeans.cluster_centers_)

plt.scatter(main_data.data[:, 0], main_data.target, c = 'green', marker = '.')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'red', marker = '+')
plt.title('Data points and cluster centroids')
plt.show()

# import scipy
from scipy.stats import mode

labels = np.zeros_like(prediction)
print(labels)
for _ in range(10):
  temp = (prediction == _)
  labels[temp] = mode(main_data.target[temp])[0]
  print("print mode[0]", mode(main_data.target[temp])[0])
  print(labels[temp])
print(labels)

from sklearn.metrics import accuracy_score, confusion_matrix

accuracy_score(main_data.target, labels)

"""## 83.47% Accuracy"""

mat = confusion_matrix(main_data.target, labels)
ax = sns.heatmap(mat.T, square = True, annot = True, cbar = False, xticklabels = main_data.target_names, yticklabels = main_data.target_names)

plt.xlabel('true label')
plt.ylabel('predicted label')

df['class']
