from keras.models import model_from_json

class Network:
    def __init__(self):
        self.model = None
        self.loadModel('model/model.json','model/model.h5')

    def loadModel(self,modelFileName,modelWeightsName):
        json_file = open(modelFileName, 'r')
        self.model = json_file.read()
        json_file.close()
        self.model = model_from_json(self.model)
        self.model.load_weights(modelWeightsName)

    def compileModel(self):
        self.model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    def predict(self,test):
        prob = float(self.model.predict(test))
        if prob >= 0.5:
            return 1
        else:
            return 0

    def isEdible(self,test):
        return self.predict(test)
