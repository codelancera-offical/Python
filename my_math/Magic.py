from my_math.Discrete import *
def pigeon(n, pigeonholes=365):
    return 1 - A(pigeonholes, n) / pigeonholes**n

def is_prime(num:int) -> bool:
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        while i*i <= num:
            if num % i == 0 or num % (i + 2) == 0:  # can divided by a prime?
                return False
            i += 6
        return True


def generate_primes(count=10):
    primes = []
    
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    return primes

