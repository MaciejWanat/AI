# -*- coding: utf-8 -*-
import arcade

from gaMap import gaMap

from Mushroom import Mushroom
from Flower import Flower
from FlowerPower import FlowerPower
from Grid import Grid
from AstarSolver import AstarSolver
from MushroomRecognition import MushroomRecognition
from Direction import Direction


class App(arcade.Window):
    def __init__(self, width, height,block_size,start_x,start_y):
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
        self.start_x = start_x
        self.start_y = start_y
        self.gaMap = gaMap()
        self.grid = Grid(self.grid_width,self.grid_height,self.block_size,self.start_x,self.start_y, self.gaMap)
        self.grid_map = self.grid.map
        self.aStar = AstarSolver(self.grid_map,self.start_x,self.start_y)
        self.actionsPath = self.aStar.solve()
        self.gatherMushroomAlg = MushroomRecognition()
        self.gatherFlowerAlg = FlowerPower()

    def on_draw(self):
        """
        Called when an update on a board has to be done
        """
        arcade.start_render()
        self.grid.background_list.draw()
        self.grid.items.draw()
        self.grid.mushroomPicker.draw()


        # Put the score on a screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        Visualization of movement on a board
        """
        if self.actionsPath:
            direction     = self.aStar.currentDirection
            print(direction)
            (action,step) = self.actionsPath.pop(0)
            print('current move -> ',action,step)
            self.gatherItemsFromMap((self.grid.mushroomPicker.x,self.grid.mushroomPicker.y))

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
                self.aStar.currentDirection = step

                if(step == Direction.NORTH):
                    self.grid.mushroomPicker.angle = 90

                if(step == Direction.EAST):
                    self.grid.mushroomPicker.angle = 0

                if(step == Direction.WEST):
                    self.grid.mushroomPicker.angle = -180

                if(step == Direction.SOUTH):
                  self.grid.mushroomPicker.angle = -90

            x1 =  (self.grid.field_width * self.grid.mushroomPicker.x + self.grid.field_width // 2 )
            y1 =  (self.grid.field_height * self.grid.mushroomPicker.y + self.grid.field_height // 2)

            self.grid.mushroomPicker.center_x = x1
            self.grid.mushroomPicker.center_y = y1


    def gatherItemsFromMap(self,mushroomPickerPosition):
        nearestArea = self.aStar.get_adjacent_cells_2(mushroomPickerPosition[1],mushroomPickerPosition[0])

        for field in nearestArea:
            if(True):
                if type(field) is Mushroom:
                    edible = self.gatherMushroomAlg.isEdible(field.vector)
                    realEdibility = field.isEdible

                    if(edible == realEdibility):
                        print("The mushroom on position -> ",field.x,field.y,
                              " is ",  "poisonous" if not edible else "edible")

                        if(edible):
                            field.center_y = -100
                            field.center_x = -100

                        self.score +=1

                    else:
                        print("I was wrong! What's a pity! You will die in a few minutes!")
                        self.score -=2

                    field.reachable = True

                elif type(field) is Flower:

                    protected = self.gatherFlowerAlg.isProtected(field)
                    predName = self.gatherFlowerAlg.getName(field)

                    if(not protected):
                        field.center_y = -100
                        field.center_x = -100
                        self.score +=1


                    print("------------------")
                    print("The flower on position -> ",field.x,field.y, " is ",  "protected" if protected else "not protected")
                    print("I think it's a " + predName + "!")

                    print("In fact, it was a " + str(field.flowerName).title() + " (picture " + str(field.picNum) + ").")

                    if(str(field.flowerName).title() != str(predName)):
                        print("Looks like I was wrong :(")
                        self.score -=2

                    field.reachable = True

def main():
    window = App(800,800,40,0,0)
    arcade.run()

main()
