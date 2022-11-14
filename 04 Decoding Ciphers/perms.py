"""For a total number of columns, find all unique column arrangements.

Builds a list of lists containing all possible unique arrangements of individual column
numbers, including negative values for route direction (read up column vs. down).

Input:
-total number of columns

Returns:
-list of lists of unique column orders, including negative values for
route cipher encryption direction

"""
from itertools import permutations, product

# Build list of lists of possible comumn number combinations
def perms(num_columns):
    """Take number of columns integer & generate pos & neg permutations."""
    results= []
    columns = [x for x in range (1, num_columns+1)]
    for perm in permutations(columns):
        for signs in product([-1, 1], repeat=len(columns)):
            results.append([i*sign for i, sign in zip(perm, signs)])

    return results
