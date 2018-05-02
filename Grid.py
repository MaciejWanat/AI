# coding: utf-8
import arcade
from Field import Field
from Mushroom import Mushroom
from MushroomPicker import MushroomPicker
from Physics import Physics

import random
from random import randint

class Grid:
    def __init__(self, field_width=70, field_height=70, width=18, height=9):
        self.grid = []
        self.walls = [()]
        self.path = []
        self.width = width
        self.height = height
        self.field_height = field_height
        self.field_width = field_width
        self.background_list = None
        self.mushroomPicker = None
        self.SPRITE_SCALING = 1
        self.setup()

    def setup(self):
        self.mushroomPicker = MushroomPicker(35,35,"app_resources/images/mushroompicker.png", self.SPRITE_SCALING)
        self.background_list = arcade.SpriteList()
        self.items = arcade.SpriteList()
        self.drawBackground()
        self.map = self.create_map()
        self.grid = map
        self.physics_engine = Physics(self.mushroomPicker,self.items)

    def create_map(self):
        grid = []

        for row in range(self.height):
            grid.append([])
            for column in range(self.width):

                x =  self.field_width * column + self.field_width // 2
                y =  self.field_height * row + self.field_height // 2

                if(row % 2 and random.randint(0, 1) == 1):
                    grid[row].append(Mushroom(x,y))
                else:
                    grid[row].append(Field(x,y,"field",True))

                self.items.append(grid[row][column])

        neighbours = self.get_neighbours(5,5)
        for (x,y) in neighbours:
            state = grid[x][y]
            if state.reachable == False:
                print(state.isEdible)


        return grid

    def drawBackground(self):
        for row in range(self.height):
            for column in range(self.width):
                x =  self.field_width * column + self.field_width // 2
                y =  self.field_height * row + self.field_height // 2

                background_sprite = arcade.Sprite("app_resources/images/background_lines.png", self.SPRITE_SCALING)
                background_sprite.width = self.field_width;
                background_sprite.height = self.field_height;
                background_sprite.center_x = x
                background_sprite.center_y = y
                self.background_list.append(background_sprite)

    def getBackgroundList(self):
        return self.background_list

    def getMushroomsList(self):
        return self.items

    def get_neighbours(self,x,y):
        # Size of "board"
        X = 18
        Y = 9

        neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                       for y2 in range(y-1, y+2)
                                       if (-1 < x <= X and
                                           -1 < y <= Y and
                                           (x != x2 or y != y2) and
                                           (0 <= x2 <= X) and
                                           (0 <= y2 <= Y))]

        return neighbors(x,y)

    # def set_path(self, path):
    #     self.path = path

    # def first_and_last(self):
    #     return [self.grid[0][0], self.grid[self.width-1][self.height-1]]
