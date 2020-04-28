import random
import sys
from decimal import Decimal

# Author: Alex Sandberg-Bernard
# Johns Hopkins University
# Discrete Mathematics – EN.605.203.81.SP20


# VALIDATION –––––––––––––––––––

# ensure n arg is given
if (len(sys.argv) != 2):
    sys.exit('program requires a single runtime argument for n (integer value)')


# get n from args and cast to int
try:
    n = int(sys.argv[1])
except ValueError as e:  # catch value errors if n is not an integer
    print(e)
    sys.exit('n must be integer')

# validate n > 0
if n < 1:
    sys.exit('please enter a value greater than 0')


# ––––––––––––––––––––––––––––––


def trial():
    '''
    Runs a trial, which is accomplished by generating and returning a list of
    randomly generated integers between 1 and 6.
    '''

    result = [random.randint(1, 6) for a in range(12)]

    return result


def check_trial(trial):
    '''
    Checks if a trial was a success by reducing the trial list to a set in order
    to ignore duplicates, then comparing that set to the set of integers between
    1 and 6. Returns a boolean value based on comparison.
    '''

    return {1, 2, 3, 4, 5, 6} == set(trial)


def run_trials(n, set):
    '''
    Executes a given number of trials and keeps track of the number of successes 
    in the set. The first parameter is an integer value that determines the number
    of trials. The second parameter is the set number, which is used to identify
    the set. Trial data is written to an output file after each trial is run. An
    integer value of number of successes in the trial is returned.
    '''

    # store number of successes
    success = 0

    # write results to output.txt file
    with open('restaurant_probability_trials.txt', mode='a') as output_txt:

        # output headers
        output_txt.write(f'\n-----------------------------------------\n')
        output_txt.write(f'\nSet {set+1}\n\n')

        # run n trials
        for i in range(n):

            # run the trial and check the result
            result = trial()
            check = check_trial(result)
            outcome = 'success' if check else 'failure'

            # write results to output file
            output_txt.write(f'\n{result}\n')
            output_txt.write(f'{outcome}\n\n')

            # if trial was success, incrememt successes
            if (check):
                success += 1

    # return total number of successes in set of trials
    return success


def series(n):
    '''
    Runs a series (10) of trials. Accepts integer value as parameter,
    which is passed to run_trials method as argument for number of trials
    to be run. Returns array of results, where each entry is an object
    containing the number of successes in the trial and the success
    probability of the trial.
    '''

    # list for storing results
    results = []

    # run series of 10 sets of n trials
    for i in range(10):

        # run trials and add successes to results
        successes = run_trials(n, i)
        results.append({
            'successes': successes,
            'probability': Decimal(successes) / Decimal(n)
        })

    # return list of results of series
    return results


def series_probability(results):
    '''
    Calculates and returns series probability estimate by averaging the
    probability for each set of trials. This function does not consider
    significant digits, and is simply a rough estimate.
    '''

    subtotal = 0

    # iterate through each result and sum probabilities
    for entry in results:
        subtotal += entry['probability']

    # return average probability
    return Decimal(subtotal) / Decimal(len(results))


# get series results and probability
results = series(n)
probability = series_probability(results)


print(f'\nTrials: {n:,}')
print(f'\nSeries:')

# iterate through all results and print to console
for num, result in enumerate(results):
    print(f'\n{num+1}.')
    print(f"successes: {result['successes']:,}")
    print(f"set probability: {result['probability']}")

print(f'\nseries success probability (average): {probability}\n')


# write results to output.txt file
with open('restaurant_probability_output.txt', mode='w') as output_txt:

    # output headers
    output_txt.write(f'\nTrials: {n:,}\n\nSeries:')

    # write results of each set of trials
    for num, result in enumerate(results):
        output_txt.write(f'\n\n{num+1}.')
        output_txt.write(f"successes: {result['successes']:,}\n")
        output_txt.write(f"set probability: {result['probability']}")
    output_txt.write(
        f'\n\nseries success probability (average): {probability}\n')
