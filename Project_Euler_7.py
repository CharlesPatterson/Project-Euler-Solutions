#!/usr/bin/env python
"""Solution to Problem 7 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=7 for the details.
"""
import time
from Euler import prime_generator

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_7():
    '''Prints the 10001st prime.
    See the prime_generator method in Euler.py for details.'''

    g = prime_generator()
    for i in range(10000): g.next()
    
    print(g.next())

if __name__ == "__main__":
    start = time.clock()
    project_euler_7()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
