import random

# constants
CHARLIE = 1
DEE = 2
DENNIS = 3
FRANK = 4
MAC = 5
JACK = 6


def run_trial():
    return [random.randint(1, 6) for a in range(12)]


def check_trial(trial):
    return {1, 2, 3, 4, 5, 6} == set(trial)
