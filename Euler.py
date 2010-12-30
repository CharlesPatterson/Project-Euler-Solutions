#!/usr/bin/env python
"""Miscellaneous helper functions for Project Euler problems."""

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def is_prime(n):
    '''Returns True if n is prime, False if n is composite.
    is_prime is best used for once-off primality tests,
    and the expected input is a positive integer.
    In other cases, a sieving method may work better.'''

    # Working from left to right, eliminate negatives and 1
    if n < 2: return False

    # 2 and 3 are primes
    if n < 4: return True

    # We caught 2 and 3, so eliminate their multiples
    if n % 2 == 0 or n % 3 == 0: return False

    # Remaining n < 9 e.g. (5, 7) are primes.
    if n < 9: return True

    # We only need to check up to sqrt(n)
    limit = int(n**.5)

    # Every prime can be written as 6k+-1, so use that for more efficient steps
    # 6(1)-1 = 5, 6(1)+1 = 7, 6(2)-1 = 11, 6(2)+1 = 13. Get it?
    for i in range(5, limit+1, 6):
      if n % i == 0: return False
      if n % (i+2) == 0: return False

    # After exhausting possible factors up to sqrt(n), it must be prime.
    return True

def prime_sieve(limit):
    '''Returns the set of primes up to the limit.
    This method uses the sieve of Eratosthenes.
    See http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes.'''

    # Start our sieve with 2
    primes = set([2])

    # Build our list to check off candidates 
    # (0 == prime, 1 == composite)
    nums = [0]*limit

    prime = 3
    while prime < limit:
        # If we hit a prime, add it to our set and mark off its multiples.
        if nums[prime] == 0:
            primes.add(prime)
            i = prime
            while i < limit:
                nums[i] = 1
                i += prime
        # Else iterate further.
        else:
            prime += 2
    return primes

def prime_generator():
    '''Returns the primes in succession.'''

    # Take care of the first few primes.
    yield 2
    yield 3
    yield 5
    yield 7

    # We iterate just like the is_prime method.
    i = 11
    while True:
      if is_prime(i): yield i
      if is_prime(i+2): yield i+2
      i += 6

def is_palindrome(n):
    '''Returns True if n is a palindrome, False if n is not.
    This method uses string indexing to compare elements.
    Both strings and integers are acceptable inputs,
    as integers are just converted to strings for processing.'''

    # Convert ints to strs
    if type(n) == int: n = str(n)

    # Checking half the word is equivalent to checking the whole word.
    for i in range(len(n)/2):
      if n[i] != n[len(n)-1-i]:
        return False
    return True

def gcd(a, b):
    '''Returns the Greatest Common Divisor of a and b.
    This method uses an iterative version of Euclid's algorithm.'''
    while b != 0: a, b = b, a % b
    return a

def lcm(a, b):
    '''Returns the Least Common Divisor of a and b.
    The expression returned is a convenient theorem I learned
    from Gallian's Contemporary Abstract Algebra textbook.'''
    return a * b / gcd(a, b)

def sum_of_squares(n):
    '''Returns the sum of the squares from 1 to n.
    Done in O(1) time with the explicit formula below.'''
    return (n * (n+1) * (2*n+1)) / 6

def triangle_number(n):
    '''Returns the nth triangle number.
    Also the sum of the first n natural numbers.'''
    return n * (n+1) / 2

def digit_sum(n):
    '''Returns the digit sum of n.
    This method works on both integers and strings,
    as we convert integers to strings.'''
    
    if type(n) == int: n = str(n)
    return sum(int(x) for x in n)

def digit_product(n):
    '''Returns the digit product of n.
    This method works on both integers and strings,
    as we convert integers to iterable strings.'''

    if type(n) == int: n = str(n)
    return product(n)
    
def product(iterable):
    '''Returns the product of all the elements in iterable.
    Guido apparently vetoed the inclusion of a product method
    like the sum method. How irritating, though easy to fix.'''
    p = 1
    for e in iterable: p *= int(e)
    return p

def cross(A, B):
    '''Returns the cross product of A with B.'''
    return [a+b for a in A for b in B]

def proper_divisors(n):
    """Returns a list of the proper divisors of n."""
    return [x for x in range(1, n/2+1) if n % x == 0]

def is_abundant(n):
    """Returns true if n is an abundant number.

    An abundant number n is one in which d(n) > n.
    The sum of its divisors is greater than the number itself.
    One such number is 12: 1+2+3+4+6 = 16 > 12."""
    if sum(proper_divisors(n)) > n:
        return True
    else:
        return False
