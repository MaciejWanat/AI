# -*- coding: utf-8 -*-
import arcade

from Grid import Grid
from AstarSolver import AstarSolver
from Network import Network
from Direction import Direction

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
        print(self.aStar.get_path_states(self.path))
        self.actionsPath = self.aStar.get_path_states(self.path)

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
        if self.actionsPath:
            direction = self.aStar.direction

            (action,step) = self.actionsPath.pop(0)

            if(action == 'Move'):
                if(direction == Direction.EAST):
                    self.grid.mushroomPicker.x += 1

                if(direction == Direction.NORTH):
                    self.grid.mushroomPicker.y += 1

                if(direction == Direction.WEST):
                    self.grid.mushroomPicker.x -= 1

                if(direction == Direction.SOUTH):
                    self.grid.mushroomPicker.y -= 1

            elif(action == 'Rotate'):
                self.aStar.direction = step

                if(step == Direction.NORTH):
                    self.grid.mushroomPicker.angle = 90

                if(step == Direction.EAST):
                    self.grid.mushroomPicker.angle = 0

                if(step == Direction.WEST):
                    self.grid.mushroomPicker.angle = -180

                if(step == Direction.SOUTH):
                  self.grid.mushroomPicker.angle = -270

            x1 =  (self.grid.field_width * self.grid.mushroomPicker.x + self.grid.field_width // 2 )
            y1 =  (self.grid.field_height * self.grid.mushroomPicker.y + self.grid.field_height // 2)

            self.grid.mushroomPicker.center_x = x1
            self.grid.mushroomPicker.center_y = y1
            self.gatherMushrooms((self.grid.mushroomPicker.x,self.grid.mushroomPicker.y))

    def gatherMushrooms(self,mushroomPickerPosition):

        nearestArea = self.aStar.get_adjacent_cells(mushroomPickerPosition[1],mushroomPickerPosition[0])

        for field in nearestArea:

            if(field.reachable == False):
                edible = self.gatherMushroomAlg.isEdible(field.vector)
                if(not edible):
                    field.center_y = -100
                    field.center_x = -100
                    self.score +=1
                print("The mushroom on posisition -> ",field.x,field.y, " is ", edible)



def main():
    window = App(1260,630,70)

    arcade.run()


main()
