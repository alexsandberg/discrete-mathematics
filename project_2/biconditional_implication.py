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


def get_truth_value_row(row):
    '''
    Implements biconditional logic to evaluate truth value
    for a row of chained biconditional propositions.
    '''
    return reduce(lambda x, y: x == y, row)


def compile_results(truth_table):
    '''
    Compiles results of truth table and formats for output. An object is generated
    for each row and includes the row number, a string representation of each proposition,
    a value for "m", which represents the number of True values in the row, and the overall
    truth value for the row. A list of objects is returned.
    '''

    results = []

    for row_num, row in enumerate(truth_table, start=1):

        # generate string representation of each proposition val
        row_str_list = []
        for num, val in enumerate(row, start=1):
            truthy = False if (val == 0) else True
            row_str_list.append(f'p{num}: {truthy}')

        # get truth value for row
        truth_val = get_truth_value_row(row)

        # m represents the number of true vals
        m = row.count(1)

        # add data to object for each row
        row_obj = {
            'row number': row_num,
            'truth values': row_str_list,
            'm': m,
            'row truth value': truth_val
        }

        results.append(row_obj)

    return results


# create truth table using calculated number of rows
truth_table = create_truth_table(rows_num)

# compile the results
results = compile_results(truth_table)

for row in results:
    print(row)
