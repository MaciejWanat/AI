import os
from os import listdir, makedirs
from os.path import join, exists, expanduser
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential, Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from keras import backend as K

img_width, img_height, rgb = 100, 100, 3 
train_data_dir = 'F:/fruits/fruits-360/Training'
validation_data_dir = 'F:/fruits/fruits-360/Test'
batch_size = 8
epochs = 3

train_datagen = ImageDataGenerator(rescale=1. / 255,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1. / 255)
train_generator = train_datagen.flow_from_directory(train_data_dir, target_size = (img_height, img_width), batch_size = batch_size, class_mode = 'categorical')
validation_generator = test_datagen.flow_from_directory(validation_data_dir, target_size = (img_height, img_width), batch_size = batch_size, class_mode = 'categorical')

def createModel(nClasses,inputShape):
    model = Sequential()
    model.add(Conv2D(32, (8, 8), padding='same', activation='relu', input_shape=inputShape))
    model.add(Conv2D(32, (8, 8), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, (8, 8), padding='same', activation='relu'))
    model.add(Conv2D(64, (8, 8), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, (8, 8), padding='same', activation='relu'))
    model.add(Conv2D(64, (8, 8), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nClasses, activation='softmax'))
    return model

model = createModel(32,(img_width, img_height, rgb))
model.compile(loss='categorical_crossentropy', optimizer=optimizers.SGD(lr=1e-4, momentum=0.9), metrics=['accuracy'])

# ## 5. Training and Validating the Pretrained Model
# We use the **fit_generator()** function because we are using object of the **ImageDataGenerator** class to fetch data.
import tensorflow as tf
with tf.device("/device:GPU:0"):
    # optionsGPU = tf.GPUOptions(per_process_gpu_memory_fraction=0.4, allow_growth=True)
    # configGPU = tf.ConfigProto(gpu_options=optionsGPU)
    # session = tf.Session(config=configGPU)
    fit_history = model.fit_generator(train_generator,epochs=epochs, shuffle = True, verbose = 1, validation_data = validation_generator)
    # serialize model to JSON
    model_json = model.to_json()
    with open("./model/model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("./model/model.h5")
    print("Saved model to disk")

import matplotlib.pyplot as plt
plt.plot(fit_history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['CNN'], loc='upper left')
plt.show()
plt.plot(fit_history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['CNN'], loc='upper left')
plt.show()

