import tensorflow as tf
import numpy as np 

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# Reshaping the data to be compatible with the model
IMG_SIZE = 28
x_trainr = np.array(x_train).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
x_testr = np.array(x_test).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.Sequential()

#1st Convolutional Layer
model.add(tf.keras.layers.Conv2D(32, (3,3), input_shape = x_trainr.shape[1:], activation = 'relu'))
model.add(tf.keras.layers.MaxPooling2D(2,2))

#2nd Convolutional Layer
model.add(tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'))
model.add(tf.keras.layers.MaxPooling2D(2,2))

#3rd Convolutional Layer
model.add(tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'))
model.add(tf.keras.layers.MaxPooling2D(2,2))

#Flatten the data for the fully connected layers
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation = 'relu'))

# Fully Connected Layer
model.add(tf.keras.layers.Dense(32, activation = 'relu'))

# Fully Connected Layer
model.add(tf.keras.layers.Dense(10, activation = 'softmax'))


model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
model.fit(x_trainr, y_train, epochs = 5, validation_split = 0.3)
