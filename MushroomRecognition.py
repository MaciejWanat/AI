from keras.models import model_from_json

class MushroomRecognition:
    def __init__(self):
        self.model = None
        self.loadModel('./mushrooms_recognition/model/model.json','./mushrooms_recognition/model/model.h5')

    def loadModel(self,modelFileName,modelWeightsName):
        json_file = open(modelFileName, 'r')
        self.model = json_file.read()
        json_file.close()
        self.model = model_from_json(self.model)
        self.model.load_weights(modelWeightsName)

    def compileModel(self):
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    def predict(self,test):
        prob = float(self.model.predict(test))
        print("------------------")
        print("Probability that a mushroom is poisonous: ",prob)

        return 1 if prob < 0.5 else 0

    def isEdible(self,test):
        return self.predict(test)
