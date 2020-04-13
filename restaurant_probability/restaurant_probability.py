import random
import sys
from decimal import Decimal

# ensure n arg is given
if (len(sys.argv) != 2):
    sys.exit('program requires a single runtime argument for n (integer value)')


# get n from args and cast to int
try:
    n = int(sys.argv[1])
except ValueError as e:
    print(e)
    sys.exit('n must be integer')


# validate n > 0
if n < 1:
    sys.exit('please enter a value greater than 0')


# constants
CHARLIE = 1
DEE = 2
DENNIS = 3
FRANK = 4
MAC = 5
JACK = 6


def trial():
    return [random.randint(1, 6) for a in range(12)]


def check_trial(trial):
    return {1, 2, 3, 4, 5, 6} == set(trial)


def run_trials(n):
    success = 0
    for i in range(n):
        if (check_trial(trial())):
            success += 1
    return success


def series(n):
    results = []
    # run series of 10 sets of n trials
    for i in range(10):
        successes = run_trials(n)
        results.append({
            'successes': successes,
            'probability': Decimal(successes) / Decimal(n)
        })
    return results


def series_probability(results):
    subtotal = 0
    for entry in results:
        subtotal += entry['probability']

    return Decimal(subtotal) / Decimal(len(results))


# get series results and probability
results = series(n)
probability = series_probability(results)


print(f'\ntrials: {n}')

# print out results of each set of trials
for num, result in enumerate(results):
    print(f'\n{num+1}.')
    print(f"successes: {result['successes']}")
    print(f"set probability: {result['probability']}")

print(f'\nseries success probability: {probability}\n')
