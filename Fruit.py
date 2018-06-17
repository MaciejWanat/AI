import pandas as pd
import arcade
import random

from Field import Field
from random import randint

class Fruit(Field):
    def __init__(self, x, y,center_x,center_y, reachable=False):
        # self.isProtected = None
        self.fruitName = None
        self.picture = None
        self.loadConfig()
        super().__init__(x, y, center_x, center_y, self.fruitName, False)
        self.h = 1000

    def loadConfig(self):
        labels = os.listdir('./fruits_recognition/Test')
        self.fruitName = random.choice(labels)
        images = os.listdir('./fruits_recognition/Test/%s'%(self.fruitName))
        self.picture = random.choice(images)
    def __lt__(self, other):
        return self.h <= other.h
