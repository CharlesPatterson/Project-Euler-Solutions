#!/usr/bin/env python
"""Solution to Problem 12 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=12 for the details.
"""
from math import sqrt
from Euler import triangle_number_gen
import time

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_12():
    """Calculates the first triangle number to have over 500 divisors.

    Every number has an even number of divisors except for squares.
    This allows us to double-count the divisors of n up to sqrt(n),
    giving the count for n, as long as we take care of the square case."""
    
    for n in triangle_number_gen():

        c = 0
        for i in xrange(1, int(sqrt(n))+1):
            if n % i == 0:
                c += 1

                # Count twice if n isn't a square number.
                if i * i != n:
                    c += 1

            # Short-circuit if we hit 500 divisors
            if c > 500:
                print(n)
                return

if __name__ == "__main__":
    start = time.clock()
    project_euler_12()
    end = time.clock()

    print("Total Time: %f" % (end-start))
    raw_input("Press Enter to Continue...")
