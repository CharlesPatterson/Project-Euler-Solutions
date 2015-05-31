#!/usr/bin/env python
"""Solution to Problem 26 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=26 for the details.
"""
import time
from Euler import is_prime, mult_order_mod

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_26():
    """Calculates the value of d < 1000 for which 1/d contains the longest
    recurring cycle in its decimal fraction part.
    
    Decimal fraction parts only repeat if d is relatively prime to 10,
    so we filter out non-primes from consideration. Next, the number
    of digits is equal to the multiplicative order of 10 mod d."""
    best, index = 0, 0

    for x in [i for i in range(10,1000) if is_prime(i)]:
        y = mult_order_mod(x)
        if y > best:
            index = x
            best = y
    print(index)

if __name__ == "__main__":
    start = time.clock()
    project_euler_26()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
