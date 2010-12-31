#!/usr/bin/env python
"""Solution to Problem 20 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=20 for the details.
"""
from math import factorial

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_20():
    '''Prints the sum of the digits of 100!.'''
    print(sum([int(x) for x in str(factorial(100))]))

if __name__ == "__main__":
    project_euler_20()

    raw_input("Press Enter to Continue...")
