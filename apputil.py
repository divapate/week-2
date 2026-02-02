import numpy as np


def ways(n):
    """
    Return the number of ways to make n cents
    using only pennies (1¢) and nickels (5¢).
    """
    if n < 0:
        return 0

    return (n // 5) + 1


def lowest_score(names, scores):
    """
    Return the name of the student with the lowest test score.
    Works for both Python lists and NumPy arrays.
    """
    names = np.array(names)
    scores = np.array(scores)

    index = np.argmin(scores)
    return names[index]


def sort_names(names, scores):
    """
    Return a list of student names sorted by score
    from highest to lowest.
    Works for both Python lists and NumPy arrays.
    """
    names = np.array(names)
    scores = np.array(scores)

    sorted_indices = np.argsort(scores)[::-1]
    return list(names[sorted_indices])

