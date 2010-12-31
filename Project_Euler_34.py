#!/usr/bin/env python
"""Solution to Problem 34 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=34 for the details.
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

def project_euler_34():
    """Calculates the sum of the numbers from 3 : 100000 
    whose digits' factorial sum is the number itself.
    
    E.g. 1! + 4! + 5! = 1 + 24 + 120 = 145"""
    digitvals = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 
                 6: 720, 7: 5040, 8: 40320, 9: 362880}

    print(sum([n for n in range(3,100000) 
                if n == sum([digitvals[int(d)] for d in str(n)])]))

if __name__ == "__main__":
    start = time.clock()
    project_euler_34()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
