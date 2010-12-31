#!/usr/bin/env python
"""Solution to Problem 27 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=27 for the details.
"""
import time
from Euler import is_prime

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_27():
    """Finds the product of a and b for that produces the most primes for 
    consecutive values of n, starting with n = 0. For n^2 + an + b where
    |a| < 1000 and |b| < 1000."""
    best = (0, -1001, -1001)

    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while is_prime(abs(n*n + a*n + b)): n += 1
            if n > best[0]: best = (n, a, b)
    print(best[1]*best[2])

if __name__ == "__main__":
    start = time.clock()
    project_euler_27()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
