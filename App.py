# -*- coding: utf-8 -*-
import arcade

from Grid import Grid
from AstarSolver import AstarSolver

class App(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, title="Inteligentny Grzybiarz")
        self.score = 0
        self.wilhelm = arcade.sound.load_sound("app_resources/sounds/wilhelm.ogg")
        self.grid = Grid();
        self.grid_map = self.grid.map
        self.aStar = AstarSolver(self.grid_map)
        self.path = self.aStar.solve()
        print(self.aStar.solve())

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

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if self.path:
            y,x = self.path.pop(0)
            print(x,y)


            x =  (self.grid.field_width * x + self.grid.field_width // 2 )
            y =  (self.grid.field_height * y + self.grid.field_height // 2)

            self.grid.mushroomPicker.center_x = x
            self.grid.mushroomPicker.center_y = y



def main():
    window = App(1260,630)
    arcade.run()


main()
