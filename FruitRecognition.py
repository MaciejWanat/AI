
# coding: utf-8

# # Fruits-360 - Transfer Learning using Keras and ResNet-50
# 
# * This notebook is a brief application of transfer learning on the Fruits-360 [Dataset](https://www.kaggle.com/moltean/fruits). 
# * This data set consists of 42345 images of 64 fruits.
# * We compare the Transfer learning approach to the regular approach.
# * Accuracy of 98.44% is achieved within 2 epochs.
# 
# 
# ### **Contents:**
# 
# *  **1. Brief Explanation of Transfer Learning**
# *  **2. Transfer Learning using Kaggle Kernels**
# *  **3. Reading and Visualizing the Data**   
# *  **4. Building and Compiling the Models**    
# *  **5. Training and Validating the Pretrained Model** 
# *  **6. Training and Validating Vanilla Model**
# *  **7. Comparison between Pretrained Models and Vanilla Model**

# In[15]:


import os
from os import listdir, makedirs
from os.path import join, exists, expanduser

from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential, Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
# Any results you write to the current directory are saved as output.


# ## 1. Transfer Learning
# 
# In transfer learning, we first train a base network on a base dataset and task, and then we repurpose the learned features, or transfer them, to a second target network to be trained on a target dataset and task. This process will tend to work if the features are general, meaning suitable to both base and target tasks, instead of specific to the base task.
# 
# Lisa Torrey and Jude Shavlik in their chapter on transfer learning describe three possible benefits to look for when using transfer learning:
# 
# * Higher start. The initial skill (before refining the model) on the source model is higher than it otherwise would be.
# * Higher slope. The rate of improvement of skill during training of the source model is steeper than it otherwise would be.
# * Higher asymptote. The converged skill of the trained model is better than it otherwise would be.
# 
# <center><img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2017/09/Three-ways-in-which-transfer-might-improve-learning.png"></center>
# 
# 
# Basically, we take a pre-trained model (the weights and parameters of a network that has been trained on a large dataset by somebody else) and “fine-tune” the model with our own dataset. The idea is that this pre-trained model will either provide the initialized weights leading to a faster convergence or it will act as a fixed feature extractor for the task of interest.
# 
# 
# 
# These two major transfer learning scenarios look as follows:
# 
# * Finetuning the convnet: Instead of random initializaion, we initialize the network with a pretrained network, like the one that has been trained on a large dataset like imagenet 1000. Rest of the training looks as usual. In this scenario the entire network needs to be retrained on the dataset of our interest
# 
# * ConvNet as fixed feature extractor: Here, we will freeze the weights for all of the network except that of the final fully connected layer. This last fully connected layer is replaced with a new one with random weights and only this layer is trained.
# 
# In this notebook we will demonstrate the first scenario.
# 

# ## 2. Transfer Learning using Kaggle Kernels
# 
# ### Using the Keras Pretrained Models dataset
# Kaggle Kernels cannot use a network connection to download pretrained keras models. This [Dataset](https://www.kaggle.com/moltean/fruits) helps us to use our favorite pretrained models in the Kaggle Kernel environment.
# 
# All we have to do is to copy the pretrained models to the cache directory (~/.keras/models) where keras is looking for them.

# In[16]:


# cache_dir = expanduser(join('~', '.keras'))
# if not exists(cache_dir):
#     makedirs(cache_dir)
# models_dir = join(cache_dir, 'models')
# if not exists(models_dir):
#     makedirs(models_dir)
    
# get_ipython().system('cp ../input/keras-pretrained-models/*notop* ~/.keras/models/')
# get_ipython().system('cp ../input/keras-pretrained-models/imagenet_class_index.json ~/.keras/models/')
# get_ipython().system('cp ../input/keras-pretrained-models/resnet50* ~/.keras/models/')

# print("Available Pretrained Models:\n")
# get_ipython().system('ls ~/.keras/models')


# ## 3. Reading and Visualizing the Data
# ### Reading the Data
# 
# Like the rest of Keras, the image augmentation API is simple and powerful. We will use the **ImageDataGenerator** to fetch data and feed it to our network
# 
# Keras provides the **ImageDataGenerator** class that defines the configuration for image data preparation and augmentation. Rather than performing the operations on your entire image dataset in memory, the API is designed to be iterated by the deep learning model fitting process, creating augmented image data for you just-in-time. This reduces your memory overhead, but adds some additional time cost during model training.
# 
# The data generator itself is in fact an iterator, returning batches of image samples from the directory when requested. We can configure the batch size and prepare the data generator and get batches of images by calling the **flow_from_directory()** function.

# In[17]:


# dimensions of our images.
img_width, img_height = 224, 224 # we set the img_width and img_height according to the pretrained models we are
# going to use. The input size for ResNet-50 is 224 by 224 by 3.

train_data_dir = 'F:\\fruits\\fruits-360\\Training'
validation_data_dir = 'F:\\fruits\\fruits-360\\Test'
# nb_train_samples = 31688
# nb_validation_samples = 10657
batch_size = 16


# In[18]:


train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical')


# # ### Visualizing the Data

# # In[19]:


# import pandas as pd
# from plotly.offline import init_notebook_mode, iplot
# import plotly.graph_objs as go
# init_notebook_mode(connected=True)


# # In[20]:


# training_data = pd.DataFrame(train_generator.classes, columns=['classes'])
# testing_data = pd.DataFrame(validation_generator.classes, columns=['classes'])


# # In[21]:


# def create_stack_bar_data(col, df):
#     aggregated = df[col].value_counts().sort_index()
#     x_values = aggregated.index.tolist()
#     y_values = aggregated.values.tolist()
#     return x_values, y_values


# # In[22]:


# x1, y1 = create_stack_bar_data('classes', training_data)
# x1 = list(train_generator.class_indices.keys())

# trace1 = go.Bar(x=x1, y=y1, opacity=0.75, name="Class Count")
# layout = dict(height=400, width=1200, title='Class Distribution in Training Data', legend=dict(orientation="h"), 
#                 yaxis = dict(title = 'Class Count'))
# fig = go.Figure(data=[trace1], layout=layout);
# iplot(fig);


# # In[23]:


# x1, y1 = create_stack_bar_data('classes', testing_data)
# x1 = list(validation_generator.class_indices.keys())

# trace1 = go.Bar(x=x1, y=y1, opacity=0.75, name="Class Count")
# layout = dict(height=400, width=1100, title='Class Distribution in Validation Data', legend=dict(orientation="h"), 
#                 yaxis = dict(title = 'Class Count'))
# fig = go.Figure(data=[trace1], layout=layout);
# iplot(fig);


# # > - As we can see, all the classes are extremely well-balanced in training as well as the validation.
# # 
# # ## 4. Building and Compiling the Model
# # ### Building the Models
# # 
# # Here, we load the ResNet-50 with the ImageNet weights. We remove the top so that we can add our own layer according to the number of our classes. We then add our own layers to complete the model architecture.
# # 
# # * ### Building Pretrained Model

# In[24]:


#import inception with pre-trained weights. do not include fully #connected layers
inception_base = applications.ResNet50(weights='imagenet', include_top=False)

# add a global spatial average pooling layer
x = inception_base.output
x = GlobalAveragePooling2D()(x)
# add a fully-connected layer
x = Dense(512, activation='relu')(x)
# and a fully connected output/classification layer
predictions = Dense(71, activation='softmax')(x)
# create the full network so we can train on it
inception_transfer = Model(inputs=inception_base.input, outputs=predictions)


# *  ### Building the Vanilla Model

# In[25]:


#import inception with pre-trained weights. do not include fully #connected layers
inception_base_vanilla = applications.ResNet50(weights=None, include_top=False)

# add a global spatial average pooling layer
x = inception_base_vanilla.output
x = GlobalAveragePooling2D()(x)
# add a fully-connected layer
x = Dense(512, activation='relu')(x)
# and a fully connected output/classification layer
predictions = Dense(71, activation='softmax')(x)
# create the full network so we can train on it
inception_transfer_vanilla = Model(inputs=inception_base_vanilla.input, outputs=predictions)


# ### Compiling the Models
# We set the loss function, the optimization algorithm to be used and metrics to be calculated at the end of each epoch.

# In[26]:


inception_transfer.compile(loss='categorical_crossentropy',
              optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])

inception_transfer_vanilla.compile(loss='categorical_crossentropy',
              optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])


# In[27]:


from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())


# ## 5. Training and Validating the Pretrained Model
# 
# We use the **fit_generator()** function because we are using object of the **ImageDataGenerator** class to fetch data.

# In[28]:

import tensorflow as tf
with tf.device("/device:GPU:0"):
    optionsGPU = tf.GPUOptions(per_process_gpu_memory_fraction=0.4)
    configGPU = tf.ConfigProto(gpu_options=optionsGPU)
    with tf.Session(config=configGPU):
        history_pretrained = inception_transfer.fit_generator(train_generator,epochs=5, shuffle = True, verbose = 1, validation_data = validation_generator)
        


# In[29]: 


with tf.device("/device:GPU:0"):
    optionsGPU = tf.GPUOptions(per_process_gpu_memory_fraction=0.4)
    configGPU = tf.ConfigProto(gpu_options=optionsGPU)
    with tf.Session(config=configGPU):
        history_vanilla = inception_transfer_vanilla.fit_generator(train_generator,epochs=5, shuffle = True, verbose = 1, validation_data = validation_generator)


# In[30]:


import matplotlib.pyplot as plt
# summarize history for accuracy
plt.plot(history_pretrained.history['val_acc'])
plt.plot(history_vanilla.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['Pretrained', 'Vanilla'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history_pretrained.history['val_loss'])
plt.plot(history_vanilla.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['Pretrained', 'Vanilla'], loc='upper left')
plt.show()

