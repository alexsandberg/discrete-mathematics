import random
import sys

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


successes = run_trials(n)

print('trials: ', n)
print('successes: ', successes)
print(f'success probability: {successes/n}')
