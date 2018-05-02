import arcade
import re
import ast
import random

from Field import Field
from app_resources.assets import polishDel

image_path = "tallShroom_"


class Mushroom(Field):
    def __init__(self, x, y,center_x,center_y, reachable=False):
        self.config = self.loadConfig()
        self.isEdible = self.getEdiableFromConfig()
        super().__init__(x, y, center_x, center_y,
                         not self.isEdible and image_path + "red" or image_path + random.choice(["brown","tan"])
                         ,False)

    def loadConfig(self):
        config_file = random.choice(list(open("mushrooms_train/train.tsv",'r')))
        return config_file

    def getEdiableFromConfig(self):
        if(self.config[0] == 'e'):
            return 1
        else:
            return 0
