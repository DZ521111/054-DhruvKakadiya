# -*- coding: utf-8 -*-
"""054_Lab3_02_digits_Processing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18WlwhEaC5nBrnFO2K0OEpUnpjd1dNkBN
"""

'''
Author: Dhruv B Kakadiya

'''

from google.colab import drive
drive.mount("/content/drive")

"""# Roll number is **54** so I have to perform **ONE HOT ENCODING** on features"""

# Importing needful libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, preprocessing

# naive and gaussian model
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.model_selection import train_test_split

# for accuracy
from sklearn import metrics

# print precision and recall
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

# My roll number is 54 so I have to perform ONE HOT ENCODING on features

from sklearn.datasets import load_digits

# Loading digits dataset from sklearn

main_data = load_digits()

plt.figure(figsize = (20, 20))

for i in range(32):
    plt.subplot(8, 8, i + 1)
    plt.imshow(main_data.images[i])

from sklearn import preprocessing

ohe = preprocessing.OneHotEncoder()

"""# Roll No is **54** :- Split **65**% - **35**%"""

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(main_data.data, main_data.target, test_size = 0.35, random_state = 48)

# # Reshape the data

# print(f"X shape :- {X_train.shape}")

# print(f"Y shape :- {Y_train.shape}")

# # x_train and y_test
# # X_train = X_train
# # X_test = X_test

# # ohe.fit(X_train)
# # transformed_X_train = ohe.transform(X_train).toarray()

# # ohe.fit(X_test)
# # transformed_X_test = ohe.transform(X_test).toarray()

# # print("X_transformed shape :- ", transformed_X_train.shape)
# # print(X_train[7])
# # print(transformed_X_train[7])


# # y_train and y_test
# Y_train = Y_train.reshape(-1, 1)
# Y_test = Y_test.reshape(-1, 1)

# ohe.fit(Y_train)
# transformed_Y_train = ohe.transform(Y_train).toarray().reshape(1168, )

# ohe.fit(Y_test)
# transformed_Y_test = ohe.transform(Y_test).toarray()

# print(Y_test[7])
# print(transformed_Y_test[7])

# print(transformed_Y_train.shape)

# Gaussina models

gnb = GaussianNB()

# train model
gnb.fit(X_train, Y_train)

# training completed
Y_predicted = gnb.predict(X_test)

print(f"Accuracy :- {metrics.accuracy_score(Y_test, Y_predicted)}")

"""# **83** % Accuracy"""

main_data.images[3]

"""# True Prediction"""

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, prediction in zip(axes, X_test, Y_predicted):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'Prediction: {prediction}')

print(f"Classification report for classifier {gnb}:\n"
      f"{metrics.classification_report(Y_test, Y_predicted)}\n")

disp = metrics.plot_confusion_matrix(gnb, X_test, Y_test)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()
