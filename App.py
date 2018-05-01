# -*- coding: utf-8 -*-
import arcade
import random

from random import randint
from Grid import Grid

class App(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height, title="Inteligentny Grzybiarz")
        self.score = 0
        self.wilhelm = arcade.sound.load_sound("app_resources/sounds/wilhelm.ogg")
        self.grid = Grid();

    def on_draw(self):
        arcade.start_render()

        self.grid.background_list.draw()
        self.grid.items.draw()
        self.grid.mushroomPicker.draw()

        self.on_key_release(65361, 0)
        self.on_key_release(65362, 0)

        # Put the text on the screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)



def main():
    window = App(620,620)
    arcade.run()


main()
