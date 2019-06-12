from Grid import Grid

class Robot:
    
    faces_list = ['N', 'E', 'S', 'W']   # clockwise

    def __init__(self, facing, posX, posY, act_string):
        self.facing = facing
        self.posX = posX
        self.posY = posY
        self.grid = Grid(8, 8)
        self.grid.add_walls()
        self.grid.update_robot_pos(posX, posY)
        self.actions_string = act_string   # Random action bits assigned to tobot
        self.fitness_value = 0
        self.exp_count = 0
        self.cells_crawlled = []

    # Takes action for the two encoded bits (action_bits) passed as argument
    def take_action(self, action_bits):
        if action_bits == '00':     # Do nothing
            return
        elif action_bits == '01':   # Turn right (+90)
            self.facing = self.faces_list[(self.faces_list.index(self.facing) + 1) % 4 ]
        elif action_bits == '10':   # Turn left (-90)
            self.facing = self.faces_list[(self.faces_list.index(self.facing) - 1) % 4 ]
        elif action_bits == '11':   # Move forward
            newPosX = self.posX
            newPosY = self.posY
            if self.facing == 'N':
                newPosX = newPosX - 1
            elif self.facing == 'E':
                newPosY = newPosY + 1
            elif self.facing == 'S':
                newPosX = newPosX + 1
            else:
                newPosY = newPosY - 1
            
            if self.grid.map[newPosX][newPosY] != 'X':       # If not reached a wall
                self.grid.map[self.posX][self.posY] = '.'
                self.posX = newPosX
                self.posY = newPosY
                self.grid.map[self.posX][self.posY] = 'O'

            self.grid.update_robot_pos(self.posX, self.posY)

    # Follow actions and robots run on the Grid
    def follow_actions(self):
        for i in range(0, len(self.actions_string), 2):
            self.take_action(self.actions_string[i:i+2])
            # calculating and updating fitness_value
            self.update_fitness()
            # adding crawlled cell to cells_crawlled list
            cordinates = str(self.posX)+str(self.posY)
            if cordinates not in self.cells_crawlled:
                self.cells_crawlled.append(cordinates)
            #if self.cells_crawlled[0] == '11' and self.fitness_value > 10:
            #    self.cells_crawlled.pop(0)

    # Calculates fitness aka FITNESS FUNCTION
    def update_fitness(self):
        pX = self.posX
        pY = self.posY
        # Fitness is incremented if the robot's cell has a wall near it
        if str(pX)+str(pY) not in self.cells_crawlled:
            if self.grid.map[pX+1][pY] == 'X':
                self.fitness_value += 1
            elif self.grid.map[pX-1][pY] == 'X':
                self.fitness_value += 1
            elif self.grid.map[pX][pY+1] == 'X':
                self.fitness_value += 1
            elif self.grid.map[pX][pY-1] == 'X':
                self.fitness_value += 1
