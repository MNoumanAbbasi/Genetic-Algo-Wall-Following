class Grid:
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.map = [ [ '_' for c in range(w)] for r in range(h) ]

    def add_walls(self):    # Add Walls to the Map
        """ Adds X on the walls of the map """
        for row in range(self.height):
            self.map[row][0] = 'X'
        for row in range(self.height):
            self.map[row][self.width-1] = 'X'
        for col in range(self.width):
            self.map[0][col] = 'X'
        for col in range(self.width):
            self.map[self.height-1][col] = 'X'
        self.map[3][6] = self.map[4][6] = 'X'

    def update_robot_pos(self, posX, posY): # Updates location of Robot on Grid
        """ Updates location of Robot on Grid's map """
        self.map[posX][posY] = 'R'

    def print_map(self):
        """ Prints entire map of Grid """
        for x in self.map:
            print(*x, sep=" ")
