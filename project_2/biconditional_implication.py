# Author: Alex Sandberg-Bernard
# Johns Hopkins University
# Discrete Mathematics – EN.605.203.81.SP20

from functools import reduce
import sys

# n represents the number of propositions in the chained biconditional
n = int(sys.argv[1])

# rows needed for truth table
rows_num = 2 ** n


def create_truth_table(rows):
    '''
    Creates truth table using binary representation for truth values.
    Each number in the range of "rows" is translated to a binary value,
    where 0 represents False and 1 represents True. Truth table is returned
    with each entry being a row of truth values in list form.
    '''

    table = []

    # loop through each row and create truth values
    for num in range(rows):

        # remove "0b" from each value and preserve leading 0's using zfill
        num = bin(num)[2:].zfill(n)

        # append each binary digit as int value to row list
        row = [int(x) for x in num]

        # append value to truth table
        table.append(row)
        # print(f'Binary for num {num} is {bin(num)[2:].zfill(n)}')

    return table


# create truth table using calculated number of rows
truth_table = create_truth_table(rows_num)


def get_truth_value_row(row):
    '''
    Implements biconditional logic to evaluate truth value
    for a row of chained biconditional propositions.
    '''
    return reduce(lambda x, y: x == y, row)


for row in truth_table:
    print('\nROW: ')
    print(row)
    print(get_truth_value_row(row))
