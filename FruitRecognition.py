from keras.models import model_from_json
import os
from os import listdir

class FruitRecognition:
    def __init__(self):
        self.model = None
        self.loadModel('./fruits_recognition/model/model.json','./fruits_recognition/model/model.h5')
        self.labels = os.listdir('./fruits_recognition/Test')


    def loadModel(self,modelFileName,modelWeightsName):
        json_file = open(modelFileName, 'r')
        self.model = json_file.read()
        json_file.close()
        self.model = model_from_json(self.model)
        self.model.load_weights(modelWeightsName)

    def compileModel(self):
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    def predict(self,test):
        return self.labels[self.model.predict(test,verbose=1).tolist()[0].index(1.)]
        # prob = float(self.model.predict(test))
        # print("------------------")
        # print("Probability that a mushroom is poisonous: ",prob)


    def isEdible(self,test):
        return self.predict(test)
