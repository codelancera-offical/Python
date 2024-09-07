import random


def generate_random_int(distribution='uniform', low=0, high=10, **kwargs):
    if distribution == 'uniform':
        return random.randint(low, high)