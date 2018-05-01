# coding: utf-8
import arcade
from Field import Field
from Mushroom import Mushroom
from MushroomPicker import MushroomPicker
from Physics import Physics

import random
from random import randint

class Grid:
    def __init__(self, field_width=62, field_height=62,  width=11, height=11):
        self.grid = []
        self.width = width
        self.height = height
        self.path = []
        self.field_height = field_height
        self.field_width = field_width
        self.background_list = None
        self.mushroomPicker = None
        self.SPRITE_SCALING = 1
        self.setup()


    def setup(self):
        self.mushroomPicker = MushroomPicker(120,250,"app_resources/images/mushroompicker.png", self.SPRITE_SCALING)
        self.background_list = arcade.SpriteList()
        self.items = arcade.SpriteList()
        self.drawBackground()
        self.map = self.get_map()
        self.grid = map
        self.drawMap(map)
        self.physics_engine = Physics(self.mushroomPicker,self.items)

    def get_map(self):
        map_file = open("app_resources/maps/map" + str(randint(0,3)) + ".csv")
        map_array = []

        for line in map_file:
            line = line.strip()
            map_row = line.split(",")
            for index, item in enumerate(map_row):
                map_row[index] = int(item)
            map_array.append(map_row)

        return map_array

    def drawMap(self,map):

        position_x = 0;
        position_y = 15;
        mushroom_number = 0

        for horizontal in self.map:
            for vertical in horizontal:
                if(vertical):
                    mushroom = Mushroom(
                        position_x,
                        position_y + 32,
                        "app_resources/images/tallShroom_" + random.choice(["brown","red","tan"])+".png",
                         self.SPRITE_SCALING,
                        "bot_" + str(mushroom_number)
                    )
                    mushroom.width = 70;
                    mushroom.height = 70;
                    id = Mushroom.id;
                    mushroom.center_x = position_x
                    mushroom.center_y = position_y + 32
                    self.items.append(mushroom)

                position_x += 62

            position_y += 55
            position_x = 0
            mushroom_number += 1

    def drawBackground(self):

        position_x = 0;
        position_y = 0;

        for x in range(self.width):
            for y in range(self.height):
                background_sprite = arcade.Sprite("app_resources/images/background.png", self.SPRITE_SCALING)
                background_sprite.width = self.field_width;
                background_sprite.height = self.field_height;
                background_sprite.center_x = position_x
                background_sprite.center_y = position_y
                self.background_list.append(background_sprite)
                position_x += self.field_height

            position_y += self.field_width
            position_x = 0

    def getBackgroundList(self):
        return self.background_list

    def getMushroomsList(self):
        return self.items

        # for y in range(0, height):
        #     horizontal = []
        #     for x in range(0, width):
        #         is_wall_field = self.get_is_wall_field(width, x, y)
        #         is_bomb = self.is_bomb_field(not is_wall_field)
        #         # field_params = self.generate_non_bomb_field_params(params_data)
        #         field_params = self.generate_bomb_field_params(params_data) if is_bomb else self.generate_non_bomb_field_params(params_data)
        #         field = Field(x, y, field_params, field_width, field_height, not is_wall_field, is_bomb)
        #         horizontal.insert(len(horizontal), field)
        #     self.grid.insert(len(self.grid), horizontal)


    # def get_is_wall_field(self, width, x, y):
    #     if (x == (width-1) and (y == (width-1))):
    #         is_wall_field = False
    #     else:
    #         is_wall_field = random.randrange(12) == 1
    #     return is_wall_field

    # def is_bomb_field(self, is_walkable):
    #     if is_walkable:
    #         return random.randrange(30) == 1
    #     else:
    #         return False

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
