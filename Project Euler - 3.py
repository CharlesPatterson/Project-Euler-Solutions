#!/usr/bin/env python
"""Solution to Problem 3 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=3 for the details.
"""
from Euler import is_prime

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_3():
    '''Prints the largest prime factor of 600851475143.
    See the is_prime method in Euler.py for more details.'''
    print(max(i for i in range(1, int(600851475143**.5) +1) if 600851475143 % i == 0 and is_prime(i)))

if __name__ == "__main__":
    project_euler_3()

    input("Press Enter to Continue.")
