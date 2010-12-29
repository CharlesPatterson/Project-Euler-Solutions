#!/usr/bin/env python
"""Solution to Problem 2 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=2 for the details.
"""

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_2_iterative():
    '''Prints the sum of all even-valued fibonacci numbers under 4 million.
    This method uses an iterative approach which is vastly more efficient
    than the naive recursive solution.'''

    sol,f1,f2 = 0,1,1
    while f2 < 4*(10**6):
            if f2 % 2 == 0:	sol += f2
            f1,f2 = f2,f1+f2

    print(sol)

if __name__ == "__main__":
    project_euler_2_iterative()

    input("Press Enter to Continue...")		
