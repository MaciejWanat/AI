import heapq
from enum import Enum

class Direction(Enum):
     NORTH = 1
     EAST  = 2
     WEST  = 3
     SOUTH = 4

class AstarSolver(object):
    def __init__(self,grid):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = grid
        self.grid_height = len(grid)
        self.grid_width = len(grid[0])
        self.start = self.cells[0][0]
        self.direction = Direction.EAST
        self.end = self.cells[self.grid_height -1][self.grid_width -1]

    def get_heuristic(self, cell):
        """Compute the heuristic value H for a cell.
        Distance between this cell and the ending cell multiply by 10.
        @returns heuristic value H
        """
        return 10 *(abs(cell.x - self.end.x) + abs(cell.y - self.end.y))

    def get_cell(self, x, y):
        """Returns a cell from the cells list.
        @param x cell x coordinate
        @param y cell y coordinate
        @returns cell
        """
        return self.cells[x][y]

    def get_adjacent_cells(self, x, y):
        """Returns adjacent cells to a cell.
        @param x, x position in grid
        @param y, y position in grid
        @returns adjacent cells list.
        """

        # Size of "board"
        Y = self.grid_width - 1
        X = self.grid_height - 1
        skewNeighbors = [(x - 1, y - 1),(x + 1, y - 1),
                         (x - 1, y + 1), (x + 1, y + 1)]



        neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                       for y2 in range(y-1, y+2)
                                       if (-1 < x <= X and
                                           -1 < y <= Y and
                                           (x != x2 or y != y2) and
                                           (0 <= x2 <= X) and
                                           (0 <= y2 <= Y))]

        toCheck = list(set(neighbors(x,y)) - set(skewNeighbors))
        return [self.cells[x][y] for (x,y) in toCheck]

    def get_path(self):
        cell = self.end
        path = [(cell.x, cell.y)]
        if cell.parent is not None:
            while cell.parent is not self.start:
                cell = cell.parent
                path.append((cell.x, cell.y))
        else:
            return path

        path.append((self.start.x, self.start.y))
        path.reverse()
        return path

    def get_path_states(self,path,start_dir):

        states = []
        direction = Direction.EAST

        for i in range(len(path)-1):
            new_direction = self.computeState(path[i][0],path[i][1],path[i+1][0],path[i+1][1])

            if(direction == new_direction):
                states.append("Move")
            else:
                states.append("Rotate to -> " + str(new_direction))
                direction = new_direction

        return states

    def computeState(self,Y,X,y,x):
        dir_x = x - X
        dir_y = y-Y


        if(dir_x == 1):
            return Direction.EAST
        if(dir_y == 1):
            return Direction.NORTH
        if(dir_x == -1):
            return Direction.WEST

        return Direction.SOUTH

    def update_cell(self, adj, cell):
        """Update adjacent cell.
        @param adj adjacent cell to current cell
        @param cell current cell being processed
        """
        adj.g = cell.g + 10
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g
        #print('Updated coordinates: ', adj.x, adj.y)

    def solve(self):
        """Solve maze, fiCCnd path to ending cell.
        @returns path or None if not found.
        """
        # add starting cell to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):

            # pop cell from heap queue
            f, cell = heapq.heappop(self.opened)
            # add cell to closed list so we don't process it twice
            self.closed.add(cell)
            # if ending cell, return found path
            if cell is self.end:
                return self.get_path()
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell.x,cell.y)

            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        # if adj cell in open list, check if current path is
                        # better than the one previously found
                        # for this adj cell.
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell, cell)
                            #print('Checked better path: ', adj_cell.x, adj_cell.y)
                    else:
                        self.update_cell(adj_cell, cell)
                        # add adj cell to open list
                        #print('Heap push: ', adj_cell.x, adj_cell.y)
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))
