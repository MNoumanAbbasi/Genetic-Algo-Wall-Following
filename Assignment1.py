from Population import Population
import time
start_time = time.time()
# logFile make a log of time taken for increment in best fitness value
logFile = open("logTime.txt","w+")

# Setting up population and robots for generation 0
population_size = 30
myPopulation = Population(population_size, [])
myPopulation.populate_robots()
myPopulation.robots_list
max_fitness = 20                    # MAX FITNESS BEFORE PROGRAM STOPS (lower to let program stop early)
# MENU
print("Genetic Algorithm Simulation for Wall Crawling Robot")
print("\nPopulation Size:", population_size)
print("Crossover rate:", myPopulation.crossover_rate, "\nMutation rate:", myPopulation.mutation_rate)
choice = input("Enter 'y' to start algorithm:")

if choice == 'y' or choice == 'Y':
    # Simulating generation 0
    for robot in myPopulation.robots_list:
        robot.follow_actions()

    best_fitness = myPopulation.robots_list[0].fitness_value
    best_robot = myPopulation.robots_list[0]

    # Simulating all generations
    max_generation = 5000                           # MAX GENERATION: 5000
    for i in range(max_generation):
        myPopulation.make_next_gen_pop()
        myPopulation.crossover_robots()                         # Crossing robots
        myPopulation.mutate_robots()                            # Mutating robots
        for robot in myPopulation.robots_list:
            robot.follow_actions()       # Running on Grid to calculate fitness
            if robot.fitness_value > best_fitness:
                best_robot = robot
                best_fitness = robot.fitness_value
                logFile.write(str(best_fitness) +"  "+  str(time.time() - start_time) +"\n")
        print("\n"*100)
        print("Best fitness of generation", myPopulation.generation_num, ": ", best_fitness)
        if best_fitness >= max_fitness:              
            break

    print("----------------------------------------")

    print("Gen number: ", myPopulation.generation_num)
    print("Best fitness: " + str(best_fitness))
    print("Best actions: " + str(best_robot.actions_string))
    best_robot.grid.print_map()

    print("This program took", time.time() - start_time, "s to reach above solution")
    logFile.write("Program runtime: " + str(time.time() - start_time))
    logFile.close()
