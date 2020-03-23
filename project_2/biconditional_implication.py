# Author: Alex Sandberg-Bernard
# Johns Hopkins University
# Discrete Mathematics – EN.605.203.81.SP20

from functools import reduce
import sys

# get n from args
n = sys.argv[1]


rows = [[True, True, True],
        [True, True, False],
        [True, False, True],
        [True, False, False],
        [False, True, True],
        [False, True, False],
        [False, False, True],
        [False, False, False]]


def get_truth_value_row(row):
    return reduce(lambda x, y: x == y, row)


for row in rows:
    print(get_truth_value_row(row))
