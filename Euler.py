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
