from keras.models import model_from_json
from keras.preprocessing.image import img_to_array, load_img

import os
from os import listdir

class FruitRecognition:
    def __init__(self, targetFruits):
        self.model = None
        self.targetFruits = targetFruits
        self.loadModel('./fruits_recognition/model/model.json','./fruits_recognition/model/model.h5')
        self.validation_data_dir = './fruits_recognition/Test'
        self.labels = os.listdir(self.validation_data_dir)


    def loadModel(self,modelFileName,modelWeightsName):
        json_file = open(modelFileName, 'r')
        self.model = json_file.read()
        json_file.close()
        self.model = model_from_json(self.model)
        self.model.load_weights(modelWeightsName)

    def predict(self,test):
        img = load_img(self.validation_data_dir+'/'+test.fruitName+'/'+test.picture) # this is a PIL image
        x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
        x = x.reshape((1,) + x.shape)
        pred_vect = self.model.predict(x,verbose=1).tolist()[0]
        print(pred_vect)
        prediction = self.labels[pred_vect.index(1.)]
        isInteresting = prediction in self.targetFruits
        return [prediction,isInteresting]
