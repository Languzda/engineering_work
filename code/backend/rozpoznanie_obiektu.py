

import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(
        '/home/Alusya/Desktop/inzynierka/robot/zdj/zdj',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
        '/home/Alusya/Desktop/inzynierka/robot/zdj/zdj_val',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

"""## Moja architektóra"""

cnn = tf.keras.models.Sequential()

cnn.add(tf.keras.layers.Conv2D(filters = 32, kernel_size= 3, activation='relu', input_shape = [64,64,3] ))
cnn.add(tf.keras.layers.MaxPool2D(pool_size= 2, strides=2))
cnn.add(tf.keras.layers.Dropout(0.5))

cnn.add(tf.keras.layers.Conv2D(filters = 64, kernel_size= 3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size= 2, strides=2))
cnn.add(tf.keras.layers.Dropout(0.5))

cnn.add(tf.keras.layers.Conv2D(filters = 128, kernel_size= 3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size= 2, strides=2))
cnn.add(tf.keras.layers.Dropout(0.5))

cnn.add(tf.keras.layers.Conv2D(filters = 32, kernel_size= 3, activation='tanh'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size= 2, strides=2))
cnn.add(tf.keras.layers.Flatten())

cnn.add(tf.keras.layers.Dense(128, activation='relu'))
cnn.add(tf.keras.layers.Dense(3, activation='softmax'))

cnn.compile(optimizer ='adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
cnn.fit(train_generator,validation_data = test_generator, epochs = 70)

cnn.save("object_detection.h5")

