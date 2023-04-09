"""Main program using GA and PSO to optimize a problem"""

from operations import next_generation, fitness
from random_tools import create_random_matrix, create_random_array

population = create_random_matrix(500, 20)
best = create_random_matrix(500, 20)
global_best = create_random_array(20)

for i in range(20):
    population = next_generation(population, best, global_best, 0.4)

    for j, individual in enumerate(population):
        if fitness(individual) < fitness(best[j]):
            best[j] = individual
        if fitness(best[j]) < fitness(global_best):
            global_best = best[j]

    print(global_best, round(fitness(global_best), 2))
