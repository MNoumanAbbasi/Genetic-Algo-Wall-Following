from Population import Population
import time
start_time = time.time()
# logFile make a log of time taken for increment in best fitness value
logFile = open("logTime.txt","w+")

# Setting up population and robots for generation 0
population_size = 30
mutation_rate = 0.01
crossover_rate = 0.85
max_fitness = 20                    # MAX FITNESS BEFORE PROGRAM STOPS (lower to let program stop early)
# MENU
print("Genetic Algorithm Simulation for Wall Crawling Robot")
choice = 0
while True:
    print("\nPopulation Size:", population_size)
    print("Crossover rate:", crossover_rate, "\nMutation rate:", mutation_rate)
    choice = int(input("Enter '1' to start algorithm or '2' to change above parameters: "))
    if choice != 2:
        break
    user_pop_size = int(input("Enter population size (default " + str(population_size) + "): "))
    population_size = user_pop_size if 1 < user_pop_size < 500 else population_size
    user_crossover_rate = float(input("Enter crossover rate (default "+str(crossover_rate)+"):"))
    crossover_rate = user_crossover_rate if 0 < user_crossover_rate < 1 else crossover_rate
    user_mutation_rate = float(input("Enter mutation rate (default "+str(mutation_rate)+"):")) 
    mutation_rate = user_mutation_rate if 0 < user_mutation_rate < 1 else mutation_rate

if choice == 1:
    myPopulation = Population(population_size, crossover_rate, mutation_rate)
    myPopulation.populate_robots()
    # Simulating generation 0
    for robot in myPopulation.robots_list:
        robot.follow_actions()

    best_fitness = myPopulation.robots_list[0].fitness_value
    best_robot = myPopulation.robots_list[0]

    # Simulating all generations
    max_generation = 500                           # MAX GENERATION: 5000
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
else:
    print("Exiting.")