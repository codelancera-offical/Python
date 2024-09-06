from my_math.Basic import *

# Combinatorics

def A(n ,k):
    """
    Permutation A(n, k)
    Formula: A(n, k) = n! / (n - k)!
    """
    if k > n:
        return 0    # If k is greater than n, it's not possible to arrange k item
    
    return factorial(n) // factorial(n - k)

def C(n, k):
    """
    Combination C(n, k)
    Formula: C(n, k) = n! / (k! * (n-k)!)
    """

    if k > n:
        return 0    # If k is greater than n, it's not possible to choose k item
    
    return factorial(n) // (factorial(k) * factorial(n-k))
    