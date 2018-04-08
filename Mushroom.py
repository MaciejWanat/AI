import arcade
import re
import ast
import random

from rivescript import RiveScript
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
        self.brain = RiveScript(utf8=True)
        self.brain.unicode_punctuation = re.compile(r'[.,!?;*]')
        self.brain.load_file("app_resources/bot_resources/student.rive")
        self.brain.load_file("app_resources/bot_resources/" + bot_resources_variable)
        self.brain.sort_replies()
        self.id = Mushroom.id
        print(self.isEdible)
        print(self.config)


    def loadConfig(self,filename):
        config_file = random.choice(list(open("mushrooms_train/train.tsv",'r')))
        return config_file

    def answer(self,input):

        reply = self.brain.reply("localuser", polishDel(input))
        print('Student ' + self.name + ' ' + self.surname + ':',reply)

    def getName(self):
        return regexCheck("name",self.config )
        return regexCheck("name",self.config )

    def getEdiableFromConfig(self):
        if(self.config[0] == 'e'):
            return 1
        else:
            return 0


    def getSurname(self):
        return regexCheck("surname",self.config )

    def checkCheatStatus(self):
        return ast.literal_eval(regexCheck("cheat",self.config ))

def regexCheck(to_check,in_dict):
    regex = re.compile('! var (%s) = (.*)'%to_check)
    for item in in_dict:
        if(regex.findall(item)):
            match = regex.findall(item)
            return match[0][1]
