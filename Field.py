import arcade


image_path = "app_resources/images/"

class Field(arcade.Sprite):
    def __init__(self, x, y,filename,reachable):
        super().__init__(image_path + filename + ".png", 1)
        self.x = x
        self.y = y
        self.center_x = x
        self.center_y = y
        self.reachable = reachable
        self.g_cost = 0
        self.h_cost = 0

    def get_position(self):
        return (self.x, self.y)

    def f_cost(self):
        return self.g_cost + self.h_cost

    def set_parent(self, parent):
        self.parent = parent

    # def get_is_wall_field(self):
    #     if (x == (width-1) and (y == (width-1))):
    #         is_wall_field = False
    #     else:
    #         is_wall_field = random.randrange(12) == 1
    #     return is_wall_field
