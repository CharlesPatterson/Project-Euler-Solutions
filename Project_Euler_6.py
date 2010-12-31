#!/usr/bin/env python
"""Solution to Problem 6 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=6 for the details.
"""
from Euler import sum_of_squares, triangle_number

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_6():
    '''Prints [the sum of the squares] -  [the square of the sum]
       of the first 100 natural numbers.
       See Euler.py for the two formulas used.'''
    print(sum_of_squares(100) - triangle_number(100)**2)

if __name__ == "__main__":
    project_euler_6()

    raw_input("Press Enter to Continue...")
