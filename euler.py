# A Collection of Useful Code for Project Euler Problems
from math import sqrt
from functools import reduce

# For getting the factors of a number
def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))

# For getting the prime factors of a number
def primeFactors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

# For getting a list of primes (Sieve of Eratosthenes)
def primes(n):
    if n < 2:
        return []
    elif n == 2:
        return [2]

    sieve = [True] * (n + 1)
    for x in range(3, int(sqrt(n)) + 1, 2):
        for y in range(3, (n // x) + 1, 2):
            sieve[(x * y)] = False

    return [2] + [i for i in range(3, n, 2) if sieve[i]]

# For determining whether a number is prime
def isPrime(n):
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2

    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2

    return True

# For determining if a number is pandigital (has digits from 1 to n of a size n number)
def isPandigital(n):
    number = str(n)
    size = len(number)
    if '0' in number:
        return False

    for i in range(1, size + 1):
        if str(i) not in number:
            return False

    return True


