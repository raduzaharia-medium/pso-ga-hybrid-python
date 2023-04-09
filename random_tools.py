"""Algorithm utilities providing random numbers"""

import random


def create_random_array(length):
    """Return an array of random numbers with the specified length."""
    return [random.random() for _ in range(length)]


def create_random_matrix(length, width):
    """
    Return a matrix of random numbers with the specified length and width.
    The matrix is represented as a list of lists, where each inner list represents a row.
    """
    return [create_random_array(width) for _ in range(length)]
