import arcade

image_path = "app_resources/images/"

class Field(arcade.Sprite):
    def __init__(self, x, y,center_x,center_y,filename,reachable):
        super().__init__(image_path + filename + ".png", 1)
        self.parent = None
        self.x = x
        self.y = y
        self.center_x = center_x
        self.center_y = center_y
        self.reachable = reachable
        self.g_cost = 0
        self.h_cost = 0
        self.g = 0
        self.h = 10
        self.f = 0

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.h <= other.h
        return NotImplemented

    def get_position(self):
        return (self.x, self.y)

    def f_cost(self):
        return self.g_cost + self.h_cost

    def set_parent(self, parent):
        self.parent = parent
