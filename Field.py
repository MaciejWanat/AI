import arcade
import gaMap
import sys
from random import randint

image_path = "app_resources/images/"

class Field(arcade.Sprite):
    def __init__(self, x, y,center_x,center_y,filename,gaMap, reachable = True):
        super().__init__(image_path + filename + ".png", 0.5)

        self.parent = None
        self.x = x
        self.y = y
        self.center_x = center_x
        # possiton on tail \/
        self.center_y = center_y - 40
        self.reachable = reachable
        self.h = 10
        self.f = randint(10, 200)
        
        self.gaMap = gaMap
        self.g = self.gaMap.getCost(x,y) * 10
        
        self.action = []

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.h <= other.h
        return NotImplemented

    def get_position(self):
        return (self.x, self.y)

    def f_cost(self):
        return self.g_cost + self.h_cost

    def set_parent(self, parent):
        self.parent = parent
    def set_action(self, action):
       self.action = action
