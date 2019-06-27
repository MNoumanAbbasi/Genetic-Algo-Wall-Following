# Genetic-Algo-Wall-Following
Genetic Algorithm for a Wall Following bot (with 4 sensors)

## Overview of Algorithm
Generate a population of robots with random [actions strings](#Actions-String). Run each robot on the Grid and calculate its fitness value using a fitness function. The robot’s fitness value is used to calculate the robot’s expected count for the parents of the next generation. The parent robots are crossed over and mutated to produce off-springs which will populate the next generation. Each off-spring robot is run on the Grid and so the whole process is repeated until the max. value of fitness is reached, indicating that we may have reached the best possible solution (or actions string).

### Actions String
This is a string which encodes the entire actions that the robot can take. The actions are encoded as follows:  

|      Action Bit     | Encoding |
|:-------------------:|:--------:|
|      Do nothing     |    00    |
| Turn anti-clockwise |    10    |
|    Turn clockwise   |    01    |
|     Move forward    |    11    |

There are 28 actions that a robot can perform in one cycle so actions string length is 56 (28 * 2)

### Roulette Wheel Selection
Selection of robots for next generation based on Roulette Wheel Selection. The fitness function is:  
**Fitness function:** The number of walls followed by the robot without repetition.

### Default value of Parameters
**Population size:** 30  
**Crossover rate:** 0.85 (85%)  
**Mutation rate:** 0.01 (1%)  
