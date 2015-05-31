#!/usr/bin/env python
"""Solution to Problem 28 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=1 for the details.
"""
import time

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_28():
    """Calculates the sum of the numbers along the diagonal
    of the following square:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    as it grows. This is done simply by noting the properties of the square,
    for example, at each step, the square grows in width by 2. The points
    that lie along the diagonal are equidistant from each other. This distance
    grows by 2 at each iteration. The math follows in the code below."""

    total = 1
    n = 1
    square_dx = 2
    square_width = 1

    while square_width < 1001:

        total += (n + 1*square_dx) + \
                 (n + 2*square_dx) + \
                 (n + 3*square_dx) + \
                 (n + 4*square_dx) 

        n += (4*square_dx)
        square_dx += 2
        square_width += 2

    print(total)

if __name__ == "__main__":
    start = time.clock()
    project_euler_28()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
