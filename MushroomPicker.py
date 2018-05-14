import arcade

class MushroomPicker(arcade.Sprite):
    def __init__(self,x,y,X,Y, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.x = x
        self.y = y
        self.center_x = X
        self.center_y = Y
