#!/usr/bin/env python
"""Solution to Problem 5 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=5 for the details.
"""
import time
from Euler import lcm

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_5():
    '''Prints the smallest number divisible by the numbers 1 to 20.
    Intuitively, the number must be the lcm(1,2,3,...,20).
    It's not hard to show that this will produce the minimum number
    with the required factors. 
    See the lcm method in Euler.py for more details.'''
    j = 1
    for i in range(1,21):
        j = lcm(j,i)
        
    print(j)

if __name__ == "__main__":
    start = time.clock()
    project_euler_5()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
