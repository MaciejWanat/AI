# coding: utf-8
import random
import arcade

from Field import Field
from Mushroom import Mushroom
from Flower import Flower
from MushroomPicker import MushroomPicker
from random import randint


import gaMap
import sys



class Grid:
    def __init__(self, width, height, block_size,start_x,start_y):
        self.grid = []
        self.width = width
        self.height = height
        self.field_height = block_size
        self.field_width = block_size
        self.background_list = None
        self.mushroomPicker = None
        self.mushroomPicker_start_x = start_x
        self.mushroomPicker_start_y = start_y
        self.SPRITE_SCALING = 0.9
        self.setup()

    def setup(self):
        x =  (self.field_width * self.mushroomPicker_start_x + self.field_width // 2 )
        y =  (self.field_height * self.mushroomPicker_start_y + self.field_height // 2)

        self.mushroomPicker = MushroomPicker(self.mushroomPicker_start_x,self.mushroomPicker_start_y,x,y,"app_resources/images/mushroompicker.png", self.SPRITE_SCALING)
        self.background_list = arcade.SpriteList()
        self.items = arcade.SpriteList()
        self.drawBackground()
        self.map = self.create_map()
        self.grid = map


    def create_map(self):
        grid = []

        for row in range(self.height):
            grid.append([])
            for column in range(self.width):

                x =  self.field_width * column + self.field_width // 2
                y =  self.field_height * row + self.field_height // 2

                if(row % 2 and random.randint(0, 1) == 1):
                    mushOrFlower = randint(0, 1)
                    if(mushOrFlower == 0):
                        grid[row].append(Flower(row,column,x,y))
                    else:
                        grid[row].append(Mushroom(row,column,x,y,2)) 
                else:
                    grid[row].append(Field(row,column,x,y,"field",True))

                self.items.append(grid[row][column])


        return grid

    def drawBackground(self):

        for row in range(self.height):
            for column in range(self.width):
                x =  self.field_width * column + self.field_width // 2
                y =  self.field_height * row + self.field_height // 2
                filename = gaMap.getFilename(row,column)
                print(filename)

                background_sprite = arcade.Sprite("app_resources/images/" + filename + ".png", self.SPRITE_SCALING*100)
                background_sprite.width = self.field_width
                background_sprite.height = self.field_height
                background_sprite.center_x = x
                background_sprite.center_y = y
                self.background_list.append(background_sprite)

    def getBackgroundList(self):
        return self.background_list

    def getMushroomsList(self):
        return self.items
