class Field:
    def __init__(self, x, y, params, width, height,reachable, poisonous = False):
        self.x = x * width
        self.y = y * height
        self.reachable = reachable
        self.poisonous = poisonous
        self.g_cost = 0
        self.h_cost = 0

    def get_position(self):
        return (self.x, self.y)

    def f_cost(self):
        return self.g_cost + self.h_cost

    def set_parent(self, parent):
        self.parent = parent
