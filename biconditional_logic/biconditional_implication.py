# Author: Alex Sandberg-Bernard
# Johns Hopkins University
# Discrete Mathematics – EN.605.203.81.SP20

from functools import reduce
from tabulate import tabulate
import sys

# validate args length is 2
if (len(sys.argv) is not 2):
    sys.exit("program takes 2 arguments: (1) program name, (2) integer value for 'n'")

# n represents the number of propositions in the chained biconditional
n = sys.argv[1]

# cast n to int
try:
    n = int(n)
except ValueError as e:
    print(e)
    sys.exit('argument must be of type integer')

# validate input is > 2
if (n < 2):
    sys.exit("'n' must be at least 2")

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
    return 'T' if reduce(lambda x, y: x == y, row) else 'F'


def create_results_table_headers(truth_table):
    '''
    Creates headers for results table. Returns list with row, numbered headers
    for each proposition, "m", and resulting compound proposition.
    '''

    # generate header
    header = ["row"]

    # used for subscripting output
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    # add headers for each proposition
    for num in range(n):
        header.append(f'p{num+1}'.translate(SUB))

    # add header for final compound proposition
    if (n == 2):
        header.append(f'p1 \u2B64 p2'.translate(SUB))
    elif (n == 3):
        header.append(f'p1 \u2B64 p2 \u2B64 p3'.translate(SUB))
    else:
        header.append(
            f'p1 \u2B64 p2 \u2B64 \u22EF \u2B64 p{n}'.translate(SUB))

    header.append('m')  # m value

    return header


def create_results_table_body(truth_table):
    '''
    Compiles results of truth table and returns in list form. Entries are lists for each row, 
    containing the truth value of each proposition, a value for "m", which represents the number
    of True values in the row, and the overall truth value for the row.
    '''

    # reverse table so 1st row is all "T" values
    truth_table.reverse()

    results = []

    # add values row by row
    for row_num, row in enumerate(truth_table, start=1):

        # list for storing each row's data
        row_result = []

        # add row number as first item
        row_result.append(row_num)

        # replace 1's and 0's with "T"'s and "F"'s
        for val in row:
            row_result.append('F') if val == 0 else row_result.append('T')

        # append overall truth value for row
        row_result.append(get_truth_value_row(row))

        # m represents the number of true vals
        m = row_result.count('T')
        row_result.append(m)

        results.append(row_result)

    return results


def get_m_value_if_true(results):

    m_values_true = []

    # go row by row
    for row in results:
        # get truth val for row (last item)
        truth_val = row[len(row) - 1]

        # get m val for row (2nd to last item)
        m = row[len(row) - 2]

        if (truth_val):
            m_values_true.append(m)

    return set(m_values_true)


# create truth table using calculated number of rows
truth_table = create_truth_table(rows_num)

# create results table headers
headers = create_results_table_headers(truth_table)

# create results table body
results_body = create_results_table_body(truth_table)

# get all m values when row evaluates to true
m_vals = get_m_value_if_true(results_body)

# create table from results
results_table = tabulate(results_body, headers=headers, tablefmt="github")

# print(results_table)

# output file is name using n value
output_name = f'output_n_{n}.txt'

# write results to output.txt file
with open(output_name, mode='w') as output_txt:
    output_txt.write(f'\nn = {n}\n\n')
    output_txt.write(results_table)
    output_txt.write(f'\n\nvalues of m when row is True: {m_vals}\n\n')
