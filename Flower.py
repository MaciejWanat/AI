import pandas as pd
import arcade
import random

from Field import Field
from app_resources.assets import polishDel
from random import randint

class Flower(Field):
    def __init__(self, x, y,center_x,center_y, reachable=False):
        self.isProtected = None
        self.flowerName = None
        self.picNum = None
        self.loadConfig()

        super().__init__(x, y, center_x, center_y, self.flowerName, False)
        self.h = 10000

    def loadConfig(self):
        labelsFile = open('./flowerTest/labels.tsv')
        labels = labelsFile.read().split("\t")

        self.picNum = randint(1, 21)
        self.flowerName = labels[self.picNum - 1]
        if (self.flowerName == 'snowdrop'):
            self.isProtected = 1
        else:
            self.isProtected = 0
        
        labelsFile.close()

    def __lt__(self, other):
        return self.h <= other.h
