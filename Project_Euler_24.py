#!/usr/bin/env python
"""Solution to Problem 1 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=1 for the details.
"""
import time
from itertools import permutations

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_24():
    """Prints the millionth lexicographic permutation of 0123456789.

    The itertools module solves the problem. permutations() creates
    an iterator that generates the permutations in lexicographic order."""
    j = list()
    p = permutations("0123456789")
    
    for i in range(10**6):
        j = next(p)

    print(j)
        
if __name__ == "__main__":
    start = time.clock()
    project_euler_24()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
