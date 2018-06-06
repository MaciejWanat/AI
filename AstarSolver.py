import heapq
from Direction import Direction

class AstarSolver(object):
    def __init__(self,grid,start_x,start_y):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = grid
        self.grid_height = len(grid)
        self.grid_width = len(grid[0])
        self.start = self.cells[start_y][start_x]
        self.direction = Direction.EAST
        self.end = self.cells[self.grid_height - 1][self.grid_width -1]

    def get_heuristic(self, cell):
        return (abs(cell[0].x - self.end.x) + abs(cell[0].y - self.end.y))

    def get_cell(self, x, y):

        return self.cells[x][y]
    
    def get_adjacent_cells_2(self, x, y):                                                                                                               
                                                                                                                                                      
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

    def get_adjacent_cells(self, x, y):

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

#poprzednio ta linijka byla zwracana
        adjFields = [self.cells[x][y] for (x,y) in toCheck]
        print("adjfields: ", adjFields)
        adjFieldsWithAction=[]
        for element in adjFields:
            dir = self.computeState(y,x,element.y,element.x)
            print("dir value; ",dir)
            if dir == Direction.EAST:
                adjFieldsWithAction.append((element,[('Move',0)]))
            if dir == Direction.NORTH:
                adjFieldsWithAction.append((element,[('Move',0),('Rotate',dir)]))

        return adjFieldsWithAction

    def get_path(self):
        cell = self.end
        path = [cell.action]
        if cell.parent is not None:
            while cell.parent is not self.start:
                cell = cell.parent
                path.append(cell.action)
        else:
            return path

        # path.append(self.start.action)
        print(path)
        path.reverse()
        return [y for x in path for y in x]

    def get_path_states(self,path):
        states = []
        direction = self.direction

        for i in range(len(path)-1):
            new_direction = self.computeState(path[i][0],path[i][1],path[i+1][0],path[i+1][1])

            if(direction == new_direction):
                states.append(("Move",0))
            else:
                states.append(("Rotate",new_direction))
                states.append(("Move",0))
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
        adj[0].g = cell.g + 10
        adj[0].h = self.get_heuristic(adj)
        adj[0].parent = cell
        
        #lista krotek akcji jakie wykonamy by dojść do adj
        cell.action = adj[1]
        
        adj[0].f = adj[0].h + adj[0].g
        #print('Updated coordinates: ', adj.x, adj.y)

    def solve(self):
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            f, cell = heapq.heappop(self.opened)

            self.closed.add(cell)
            print(cell)
            if cell is self.end:
                return self.get_path()


            adj_cells = self.get_adjacent_cells(cell.x,cell.y)
            print(adj_cells)
            for adj_cell in adj_cells:
                print(adj_cell)
                if adj_cell[0].reachable and adj_cell[0] not in self.closed:
                    if (adj_cell[0].f, adj_cell[0]) in self.opened:

                        if adj_cell[0].g > cell.g + 10:
                            self.update_cell(adj_cell, cell)

                    else:
                        self.update_cell(adj_cell, cell)
                        heapq.heappush(self.opened, (adj_cell[0].f, adj_cell[0]))
