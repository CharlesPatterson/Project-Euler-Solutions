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
    return a*b/gcd(a, b)
