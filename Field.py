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


        # for x in range(-70, 71, 70):
        #     for y in range(-70, 701, 70):
        #         if x == 0 and y == 0:
        #             continue

        #         check_x = self.x + x
        #         check_y = self.y + y

        #         x_index = int(check_x*0.01)
        #         y_index = int(check_y*0.01)

        #         if (x_index >= 0 and x_index < self.width and y_index >= 0 and y_index < self.height):
        #             neighbours.insert(len(neighbours), self.grid[y_index][x_index])

        # return neighbours
