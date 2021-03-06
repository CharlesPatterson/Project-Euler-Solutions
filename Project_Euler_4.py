#!/usr/bin/env python
"""Solution to Problem 4 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=4 for the details.
"""
import time
from Euler import is_palindrome

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_4():
    '''Prints the largest palindrome made from the product of two 3-digit numbers.
    See the is_palindrome method in Euler.py for more details.'''
    print(max(i*j for i in range(100,1000) for j in range(100,1000) if is_palindrome(str(i*j))))

if __name__ == "__main__":
    start = time.clock()
    project_euler_4()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")		
