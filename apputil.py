import numpy as np


def ways(n):
    """
    Return:
    1) the number of ways to make n cents
    2) a list of (pennies, nickels) combinations
    using only pennies (1¢) and nickels (5¢)
    """
    combos = []

    if n < 0:
        return 0, combos

    for nickels in range((n // 5) + 1):
        pennies = n - (nickels * 5)
        combos.append((pennies, nickels))

    return len(combos), combos


def lowest_score(names, scores):
    """
    Return the name of the student with the lowest test score.
    """
    index = np.argmin(scores)
    return names[index]


def sort_names(names, scores):
    """
    Return a list of student names sorted by score
    from highest to lowest.
    """
    sorted_indices = np.argsort(scores)[::-1]
    return [str(name) for name in names[sorted_indices]]


# --------------------
# Test cases
# --------------------

print(ways(12))
print(ways(20))
print(ways(3))
print(ways(0))

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

print(lowest_score(names, scores))
print(sort_names(names, scores))
