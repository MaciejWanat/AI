import pandas as pd
import arcade
import random

from Field import Field
from app_resources.assets import polishDel
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

label_encoder = LabelEncoder()
image_path = "tallShroom_"

class Mushroom(Field):
    def __init__(self, x, y,center_x,center_y, reachable=False):
        self.isEdible = None
        self.vector = None
        self.loadConfig()

        super().__init__(x, y, center_x, center_y,
                         not self.isEdible and image_path + "red" or image_path + random.choice(["brown","tan"])
                         ,False)

    def loadConfig(self):
        testData = pd.read_csv('./test-A/test_in.tsv', sep='\t')

        y = testData[testData.columns[0]]

        vector = testData.drop(testData.columns[[0]], axis=1)

        for col in vector:
            vector[col] = label_encoder.fit_transform(vector[col])

        self.vector = vector.sample(n=1)

        index = self.vector.index.item()

        if(y[index] == 'e'):
            self.isEdible = 1
        else:
            self.isEdible = 0
