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
                print(grid[row][column].reachable)

        return grid

    def drawBackground(self):
        for row in range(self.height):
            for column in range(self.width):
                x =  self.field_width * column + self.field_width // 2
                y =  self.field_height * row + self.field_height // 2

                background_sprite = arcade.Sprite("app_resources/images/background.png", self.SPRITE_SCALING)
                background_sprite.width = self.field_width;
                background_sprite.height = self.field_height;
                background_sprite.center_x = x
                background_sprite.center_y = y
                self.background_list.append(background_sprite)

    def getBackgroundList(self):
        return self.background_list

    def getMushroomsList(self):
        return self.items


    # def get_neighbours(self, field):
    #     neighbours = []

    #     for x in range(-100, 101, 100):
    #         for y in range(-100, 101, 100):
    #             if x == 0 and y == 0:
    #                 continue

    #             check_x = field.x + x
    #             check_y = field.y + y

    #             x_index = int(check_x*0.01)
    #             y_index = int(check_y*0.01)

    #             if (x_index >= 0 and x_index < self.width and y_index >= 0 and y_index < self.height):

    #                 neighbours.insert(len(neighbours), self.grid[y_index][x_index])

    #     return neighbours

    # def set_path(self, path):
    #     self.path = path

    # def first_and_last(self):
    #     return [self.grid[0][0], self.grid[self.width-1][self.height-1]]

    # def generate_bomb_field_params(self, params_data):
    #     # 1. Filtrujemy tablice na YES
    #     params_with_yes = list(filter(lambda x: x[-1] == '1', params_data))
    #     # 2. Robimy randoma od 0 do tyle ile jest pól YES
    #     how_many_yeses = len(params_with_yes)
    #     n = random.randrange(how_many_yeses)
    #     # 3. Wybeiramy na podstawie randoma paramsy z tablicy
    #     return params_with_yes[n]

    # def generate_non_bomb_field_params(self, params_data):
    #     params_with_no = list(filter(lambda x: x[-1] == '0', params_data))
    #     how_many_no = len(params_with_no)
    #     n = random.randrange(how_many_no)
    #     return params_with_no[n]
