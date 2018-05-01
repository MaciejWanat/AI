import arcade
import re
import ast
import random

from app_resources.assets import polishDel

image_path = "app_resources/images/tallShroom_"

class Mushroom(arcade.Sprite):
    id = 0

    def __init__(self,x,y,filename,sprite_scaling,bot_resources_variable):
        self.config = self.loadConfig(bot_resources_variable)
        self.isEdible = self.getEdiableFromConfig()
        super().__init__( not self.isEdible and image_path + "red.png" or image_path + random.choice(["brown","tan"])+".png", sprite_scaling)

        Mushroom.id = Mushroom.id + 1
        self.center_x = x
        self.center_y = y
        self.id = Mushroom.id

    def loadConfig(self,filename):
        config_file = random.choice(list(open("mushrooms_train/train.tsv",'r')))
        return config_file

    def getEdiableFromConfig(self):
        if(self.config[0] == 'e'):
            return 1
        else:
            return 0
