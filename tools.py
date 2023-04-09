"""Extra algorithm tools providing comparison and rounding"""

import json


def memoize(func):
    """
    Return a memoized version of the input function.

    Parameters:
        func (callable): The function to be memoized.

    Returns:
        callable: A memoized version of the input function.
    """
    cache = {}

    def memoized_func(*args):
        key = json.dumps(args)

        if key not in cache:
            cache[key] = func(*args)
        return cache[key]

    return memoized_func


def same(first, second):
    """Return True if a and b have the same elements in the same order, False otherwise."""
    return all(v1 == v2 for v1, v2 in zip(first, second))


def round_all(array):
    """Return a new array with all elements rounded to 2 decimal places."""
    return [round(e, 2) for e in array]
