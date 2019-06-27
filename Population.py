from Robot import Robot
from Grid import Grid
import copy
import random
# random.seed(0)
class Population:
    
    generation_num = 0
    def __init__(self, size, crs_rate=0.85, mt_rate=0.01): 
        self.size = size
        self.robots_list = []
        self.crossover_rate = crs_rate      # Crossover rate
        self.mutation_rate = mt_rate        # Mutation rate
        
    def populate_robots(self):  # Initializes Population of robots for generation 0
        """ Initializes Population of robots for generation 0 """
        for i in range(self.size):
            rand_bit_string = ''.join(random.choices('10', k=56))
            self.robots_list.append(Robot('E', 1, 1, rand_bit_string))
        Population.generation_num += 1
        
    def calculate_exp_counts(self): # Calculates expected count of each robots in next gen
        """ Calculates expected count of each robots in next gen """
        sum_fitness = 0
        for robot in self.robots_list:
            sum_fitness += robot.fitness_value
        for robot in self.robots_list:
            robot.exp_count = int(round(self.size * (robot.fitness_value/sum_fitness)))

    def make_next_gen_pop(self):    # Make the robots for the next generation using expected count
        """ Make the robots for the next generation using expected count """
        self.calculate_exp_counts()
        self.robots_list.sort(key=lambda x: x.fitness_value, reverse=True)
        temp_robot_list = []
        for robot in self.robots_list:
            for _ in range(robot.exp_count):
                temp_robot_list.append(Robot('E', 1, 1, robot.actions_string))
        
        del self.robots_list[:]
        temp_robot_list.sort(key=lambda x: x.exp_count, reverse=True)
        self.robots_list = copy.deepcopy(temp_robot_list[:self.size])
        del temp_robot_list[:]

        Population.generation_num += 1

    ######      Genetic Algorithm Crossover and Mutations       ######

    def mutate_robots(self):    # Mutations of Robots
        """ Mutates each current generations' robot's action_string based on mutation_rate """
        for robot in self.robots_list:
            temp_string = ""
            for bit in robot.actions_string:
                rand_num = random.uniform(0, 1)
                if rand_num <= self.mutation_rate:
                    if bit == '0':
                        bit = '1'
                    else:
                        bit = '0'
                temp_string += bit
                robot.actions_string = temp_string
    
    def crossover_robots(self): # Crossover of Robots
        """ Crossovers current generation robots by randomly making pairs """
        random.shuffle(self.robots_list)
        for robot1,robot2 in zip(self.robots_list[0::2], self.robots_list[1::2]):
            rand_num = random.uniform(0, 1)
            if rand_num <= self.crossover_rate:
                rand_pos = random.randint(1, len(robot1.actions_string)-2)
                first_string1, second_string1 = robot1.actions_string[:rand_pos], robot1.actions_string[rand_pos:]
                first_string2, second_string2 = robot2.actions_string[:rand_pos], robot2.actions_string[rand_pos:]
                robot1.actions_string = first_string1 + second_string2
                robot2.actions_string = first_string2 + second_string1
