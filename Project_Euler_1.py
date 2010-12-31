#!/usr/bin/env python
"""Solution to Problem 1 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=1 for the details.
"""

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_1_bruteforce():
    '''Prints the sum of the natural numbers < 1000 divisible by 3 or 5.
    This method uses brute force.'''
    print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))

if __name__ == "__main__":
    project_euler_1_bruteforce()
    
    raw_input("Press Enter to continue...")
