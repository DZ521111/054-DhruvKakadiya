# -*- coding: utf-8 -*-
"""054_Task_CNN_Fruits.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18q26ItG14hcQUiwGAByhEAfuzqX-fQuT
"""

'''
Author: Dhruv B kakadiya

'''

# importing libraries

import os
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# models
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from PIL import Image
from glob import glob

# to mount a drive
from google.colab import drive

# Commented out IPython magic to ensure Python compatibility.
#Mounting the drive
drive.mount('/content/gdrive')

#Setting kaggle configuration directory
os.environ['KAGGLE_CONFIG_DIR'] = "/content/gdrive/My Drive/Sem7_ML_Data/Kaggle"
# %cd /content/gdrive/My Drive/Kaggle

#Downloading and unzip dataset
!kaggle datasets download -d moltean/fruits
!unzip \*.zip && rm *.zip

# printing Images
#Setting Training & Test dir paths
train_path = './fruits-360_dataset/fruits-360/Training/'
test_path = './fruits-360_dataset/fruits-360/Test/'

#Displaying the image
img = load_img(train_path + "Watermelon/r_8_100.jpg", target_size=(100, 100))
plt.imshow(img)
plt.axis("off")
plt.show()

#Printing the shape of the image array 
x = img_to_array(img)
print(x.shape)

"""The dataset is rich in terms of the variety of fruits it contains. Let’s explore some more images of the fruits. We’ll specify some fruit names in the images list and display them on a plot. We’ll do this using the matplotlib library."""

#Visualizing more Images

images = ['Orange', 'Cauliflower', 'Cactus fruit', 'Eggplant', 'Avocado', 'Watermelon','Lychee', 'Walnut']
fig = plt.figure(figsize = (10, 5))
for i in range(len(images)):
    ax = fig.add_subplot(3, 3, i + 1, xticks = [], yticks = [])
    plt.title(images[i])
    plt.axis("off")
    ax.imshow(load_img(train_path + images[i] +"/0_100.jpg", target_size=(100, 100)))

"""We’ll find the 4 most frequent fruits in the dataset. For this, we’ll create a list named fruits and populate it with all the occurrences of fruits. Then, we’ll use Counter from the collections library to find out the 4 most frequently occurring fruits in the ‘fruits’ list."""

#Storing occurences of fruits in a list
fruits = []
fruits_image = []
for i in os.listdir(train_path):
    for image_filename in os.listdir(train_path + i):
        fruits.append(i) 
        fruits_image.append(i + '/' + image_filename)

#Finding top 5 frequent Fruits
newData = Counter(fruits)
frequent_fruits = newData.most_common(4)
print("Top 5 frequent Fruits:")
frequent_fruits

"""We’ll find out the total number of classes for the dataset. To do this, we’ll use glob. The glob module finds all the pathnames matching a specified pattern and returns them in arbitrary order. The directory containing a particular fruit’s image has the name same as that of the fruit. So, we’ll be able to get the classes of fruits from directory names."""

#Finding number of classes
className = glob(train_path + '/*')
number_of_class = len(className)
print(number_of_class)

"""First, we’ll call an ‘empty’ sequential model. We’ll add to this empty model one layer at a time. The first layer is a convolutional layer with a depth of 32 and a filter size of 3x3.
Activation: "relu"

We need to specify an input size only for our first layer as the subsequent layers can infer the input size from the output size of the previous layer. Here, our input size is (100, 100, 3).
"""

'''
There is a MaxPooling2D layer after every convolutional layer.
This layer downsamples the input representation by taking the maximum value over a window.
‘Pooling’ is basically the process of merging for the purpose of reducing the size of the data.
'''

#Creating the model
model = Sequential()
model.add(Conv2D(32,(3,3),input_shape = x.shape))
model.add(Activation("relu"))
model.add(MaxPooling2D())

model.add(Conv2D(32,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D())

model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D())

model.add(Flatten())
model.add(Dense(1024))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(number_of_class)) 
model.add(Activation("softmax"))

#Compiling the model
model.compile(loss = "categorical_crossentropy",
optimizer = "rmsprop",
metrics = ["accuracy"])

#Getting model's summary
model.summary()

#Specifing epochs & batch size
epochs = 50
batch_size = 64

#Creating an object of ImageDataGenerator.
train_datagen = ImageDataGenerator(rescale= 1./255,
shear_range = 0.3,
horizontal_flip=True,
zoom_range = 0.3)
test_datagen = ImageDataGenerator(rescale= 1./255)

#Generating batches of Augmented data.
train_generator = train_datagen.flow_from_directory(
directory = train_path,
target_size= x.shape[:2],
batch_size = batch_size,
color_mode= "rgb",
class_mode= "categorical")

# test generator
test_generator = test_datagen.flow_from_directory(
directory = test_path,
target_size= x.shape[:2],
batch_size = batch_size,
color_mode= "rgb",
class_mode= "categorical")

#Fitting the model
hist = model.fit_generator(
generator = train_generator,
steps_per_epoch = 1600 // batch_size,
epochs=epochs,
validation_data = test_generator,
validation_steps = 800 // batch_size)

#Plotting train & validation loss
plt.figure()
plt.plot(hist.history["loss"],label = "Train Loss", color = "green")
plt.plot(hist.history["val_loss"],label = "Validation Loss", color = "mediumvioletred", linestyle="dashed",markeredgecolor = "purple", markeredgewidth = 2)
plt.title("Model Loss", color = "darkred", size = 13)
plt.legend()
plt.show()

#Plotting train & validation accuracy
plt.figure()
plt.plot(hist.history["accuracy"],label = "Train Accuracy", color = "yellow")
plt.plot(hist.history["val_accuracy"],label = "Validation Accuracy", color = "mediumvioletred", linestyle="dashed",markeredgecolor = "purple", markeredgewidth = 2)
plt.title("Model Accuracy", color = "darkred", size = 13)
plt.legend()
plt.show()

