#!/usr/bin/env python
"""Solution to Problem 30 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=30 for the details.
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

def project_euler_30():
    """Finds the sum of the numbers that can be written as the sum
    of the fifth powers of their digits."""
    total = 0

    cubed_values = {9:59049, 8:32768, 7:16807, 6:7776, 5:3125, 4:1024, 3:243, 2:32, 1:1, 0:0}

    for x in range(2, 1000000):
        cubed_digit_sum = sum([cubed_values[int(y)] for y in str(x)])
        if x == cubed_digit_sum: total += cubed_digit_sum

    print(total)

if __name__ == "__main__":
    start = time.clock()
    project_euler_30()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
