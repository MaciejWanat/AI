class Field:
    def __init__(self, x, y, params, width, height, walkable = True, poisonous = False):
        self.x = x * width
        self.y = y * height
        self.params = {
            'picture': "path/to/file",
            'is_beeping': "1",
            'metal_detector_beeping': "weak",
            'is_dugged_up': '1',
            'war_here?': "trenches"
        }
        self.walkable = walkable
        self.has_bomb = has_bomb

        self.color = (0,0,0) if not walkable else (0,255,0)

        self.g_cost = 0
        self.h_cost = 0

    def get_position(self):
        return (self.x, self.y)

    def f_cost(self):
        return self.g_cost + self.h_cost

    def set_parent(self, parent):
        self.parent = parent
