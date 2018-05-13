# -*- coding: utf-8 -*-
import arcade

from Grid import Grid
from AstarSolver import AstarSolver
from Network import Network

class App(arcade.Window):
    def __init__(self, width, height,block_size):
        """Create whole app.
        @param width -> width of the app window in px
        @param height -> height of the app window in px
        @param block_size -> size of a block/state on map
        """
        super().__init__(width, height, title="Inteligentny Grzybiarz")
        self.block_size = block_size
        self.grid_width = int(width / self.block_size )
        self.grid_height = int(height / self.block_size )
        self.score = 0
        self.grid = Grid(self.grid_width,self.grid_height,self.block_size)
        self.grid_map = self.grid.map
        self.aStar = AstarSolver(self.grid_map)
        self.path = self.aStar.solve()
        self.gatherMushroomAlg = Network()
        # print(self.path)
        # print(self.aStar.get_path_states(self.path,1))

    def on_draw(self):
        """
        Called when update on a board has to be done
        """
        arcade.start_render()
        self.grid.background_list.draw()
        self.grid.items.draw()
        self.grid.mushroomPicker.draw()


        # Put the text on the screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        Visualization of movement on a board
        """
        if self.path:
            y,x = self.path.pop(0)

            x1 =  (self.grid.field_width * x + self.grid.field_width // 2 )
            y1 =  (self.grid.field_height * y + self.grid.field_height // 2)

            self.grid.mushroomPicker.center_x = x1
            self.grid.mushroomPicker.center_y = y1
            self.grid.mushroomPicker.x = x
            self.grid.mushroomPicker.y = y
            self.gatherMushrooms((self.grid.mushroomPicker.x,self.grid.mushroomPicker.y))

    def gatherMushrooms(self,mushroomPickerPosition):

        nearestArea = self.aStar.get_adjacent_cells(mushroomPickerPosition[1],mushroomPickerPosition[0])

        for field in nearestArea:

            if(field.reachable == False):
                edible = self.gatherMushroomAlg.isEdible(field.vector)
                print()
                if(not edible):
                    field.center_y = -100
                    field.center_x = -100
                print("The mushroom on posisition -> ",field.x,field.y, " is ", edible)



def main():
    window = App(1260,630,70)

    arcade.run()


main()
