# -*- coding: utf-8 -*-
"""LAB4_Task2_practice_DT_Iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12jtPj4IoTkdNWZF61vC-kYLOhtAEEaxe
"""

'''
Author: Dhruv B Kakadiya

'''

from google.colab import drive
drive.mount("/content/drive")

# Importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets, metrics
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from subprocess import call

# loading dataset
main_data = datasets.load_iris()

# printing the names
print("Features:", main_data.feature_names, sep="\n")

# printing the label type of wine(class_0, class_1, class_2)
print("\nLabels:", main_data.target_names)

# print data(feature)shape
print("features in the dataset are:", main_data.data.shape)

#split data set into train and test sets
from sklearn.model_selection import train_test_split


x_train, x_test, y_train, y_test = train_test_split(main_data.data, main_data.target, test_size = 0.3, random_state = 54)

x_train

y_test

#Create a Decision Tree Classifier (using Gini)
dtc = DecisionTreeClassifier(criterion = "gini")

#Train the model using the training sets
dtc.fit(x_train, y_train)

# Predict the classes of test data
pred = dtc.predict(x_test)
print("prediction:",pred)

# Model Accuracy, how often is the classifier correct?
Accuracy = metrics.accuracy_score(y_test, pred)
print("Accuracy:",Accuracy)

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

metrics.classification_report(y_test, pred)

disp = metrics.plot_confusion_matrix(dtc, x_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()

export_graphviz(dtc,out_file='iris_tree.dot',feature_names = list(main_data.feature_names),
               class_names=list(main_data.target_names), filled = True)

# Convert to png
call(['dot', '-Tpng', 'iris_tree.dot', '-o', 'iris_tree.png', '-Gdpi=600'])

# Display in python
plt.figure(figsize = (14, 18))
plt.imshow(plt.imread('iris_tree.png'))
plt.axis('off')
plt.show()

