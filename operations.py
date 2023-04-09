"""Main GA and PSO operations"""

import random

from typing import List
from random import random, randint
from tools import memoize, same


def crossover(parent1, parent2, cross_point):
    """
    Return a new individual resulting from 
    crossing over the two parent individuals at the specified index.

    Parameters:
        parent1 (list): The first parent individual.
        parent2 (list): The second parent individual.
        cross_point (int): The index at which to cross over the parent individuals.

    Returns:
        list: A new individual resulting from the crossover.
    """
    return parent1[:cross_point] + parent2[cross_point:]


def mutate(individual, rate):
    """
    Return a new individual with some of its elements mutated by a random amount.

    Parameters:
        individual (list): The individual to mutate.
        rate (float): The probability of each element being mutated.

    Returns:
        list: A new individual with some of its elements mutated.
    """
    return [e * random() + random() if random() < rate else e for e in individual]


@memoize
def fitness(individual):
    """
    Return the fitness score of the individual, 
    which is the absolute difference between the sum of its elements and the target value of 50.

    Parameters:
        individual (list): The individual to evaluate.

    Returns:
        float: The fitness score of the individual.
    """
    return abs(sum(individual) - 50)


def pick_best(*args):
    """
    Return the individual with the lowest fitness score out of the input individuals.

    Parameters:
        *args (list): A variable number of individuals to choose from.

    Returns:
        list: The individual with the lowest fitness score.
    """
    return min(args, key=fitness)


def create_child(parent1, parent2, mutation_rate):
    """
    Return a new child individual created by crossing over 
    the two parent individuals and potentially mutating the result.

    If the two parent individuals are the same, 
    a new random individual is created instead of crossing them over.

    Parameters:
        parent1 (list): The first parent individual.
        parent2 (list): The second parent individual.
        mutation_rate (float): The probability of each element being mutated.

    Returns:
        list: A new child individual created by 
        crossing over the parent individuals and potentially mutating the result.
    """
    if same(parent1, parent2):
        return [random() for _ in range(len(parent1))]

    cross_point = randint(0, len(parent1) - 1)
    child = crossover(parent1, parent2, cross_point)
    mutant = mutate(child, mutation_rate)

    return pick_best(parent1, parent2, child, mutant)


def pick_random(population):
    """
    Return a random individual from the input population.

    Parameters:
        population (list): The population to choose from.

    Returns:
        list: A random individual from the population.
    """
    return population[randint(0, len(population) - 1)]


def approach(parent1: List[float], parent2: List[float], best: List[float]) -> List[float]:
    """
    Given two parent arrays and the best array, generates a new array
    by taking a weighted average of the elements of the parents and the best array.

    Args:
    - parent1: A list of floating-point numbers representing the first parent array.
    - parent2: A list of floating-point numbers representing the second parent array.
    - best: A list of floating-point numbers representing the best array.

    Returns:
    - A list of floating-point numbers 
    representing the new array generated using Particle Swarm Optimization.
    """
    return [abs(e + 2 * random()
                * (best[index] - e) + 2 * random()
                * (parent2[index] - e)) for index, e in enumerate(parent1)]


def next_generation(population: List[List[float]], best: List[List[float]],
                    global_best: List[float], mutation_rate: float) -> List[List[float]]:
    """
    Generates a new population by applying the genetic algorithm.

    Args:
    - population: A list of lists of floating-point numbers representing the current population.
    - best: A list of lists of floating-point numbers representing the best individuals.
    - globalBest: A list of floating-point numbers representing the best individual so far.
    - mutationRate: A floating-point number representing the mutation rate.

    Returns:
    - A list of lists of floating-point numbers representing the new population.
    """
    new_population = []
    for element in population:
        if random() < 0.5:
            new_population.append(create_child(
                element, pick_random(population), mutation_rate))
        else:
            new_population.append(
                approach(element, pick_random(best), global_best))
    return new_population
