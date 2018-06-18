import arcade
import random
import os
from os import listdir
from Field import Field
from random import randint

class Fruit(Field):
    def __init__(self, x, y,center_x,center_y, gaMap, reachable=True):
        # self.isProtected = None
        self.fruitName = None
        self.picture = None
        self.gaMap = gaMap
        self.loadConfig()
        super().__init__(x, y, center_x, center_y, self.fruitName, self.gaMap,reachable)

        self.h = 1000

    def loadConfig(self):
        labels = os.listdir('./fruits_recognition/Test')
        self.fruitName = random.choice(labels)
        images = os.listdir('./fruits_recognition/Test/%s'%(self.fruitName))
        self.picture = random.choice(images)
    def __lt__(self, other):
        return self.h <= other.h
