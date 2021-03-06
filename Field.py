import arcade
from random import randint

image_path = "app_resources/images/"

# import pandas as pd
# filename = 'map ('+ str(randint(0, 10)) +').csv'
# gaGrid = pd.read_csv('app_resources/maps/'+filename, sep=',',header=None)
# gaGrid = pd.read_csv('app_resources/map.csv', sep=',',header=None)


class Field(arcade.Sprite):
    def __init__(self, x, y,center_x,center_y,filename,gaMap, reachable = True):
        super().__init__(image_path + filename + ".png", 0.5)

        self.parent = None
        self.x = x
        self.y = y
        self.picked = False
        self.center_x = center_x
        self.center_y = center_y
        self.reachable = reachable
        # self.g = randint(10, 200)
        self.h = 10
        # self.g = int(list(gaGrid[x][y])[1])
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
    def get_parent(self):
        return self.parent
    def set_action(self, action):
       self.action = action
