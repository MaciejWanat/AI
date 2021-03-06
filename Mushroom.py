import pandas as pd
import arcade
import random

from Field import Field
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

label_encoder = LabelEncoder()
image_path = "tallShroom_"

testData = pd.read_csv('./mushrooms_recognition/test-A/test_in.tsv', sep='\t')

y = testData[testData.columns[0]]
vector = testData.drop(testData.columns[[0]], axis=1)

class Mushroom(Field):
    def __init__(self, x, y,center_x,center_y, gaMap,reachable=True):
        self.isEdible = None
        self.vector = None
        self.loadConfig()
        self.gaMap = gaMap

        super().__init__(x, y, center_x, center_y,
                         not self.isEdible and image_path + "red" or image_path + random.choice(["brown","tan"])
                         ,self.gaMap, reachable)
        self.h = 100

    def loadConfig(self):
        for col in vector:
            vector[col] = label_encoder.fit_transform(vector[col])

        self.vector = vector.sample(n=1)

        index = self.vector.index.item()

        if(y[index] == 'e'):
            self.isEdible = 1
        else:
            self.isEdible = 0

    def __lt__(self, other):
        return self.h <= other.h