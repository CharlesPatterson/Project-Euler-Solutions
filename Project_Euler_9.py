#!/usr/bin/env python
"""Solution to Problem 9 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=9 for the details.
"""

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_9():
    '''Prints the product of the unique pythagorean triplet 
    for which a+b+c=1000. This is a naive brute-force solution 
    that cuts down some possibilities by framing it entirely
    in terms of a and b.'''

    for a in range(1,998):
        for b in range(a+1,998-a):
                if a**2 + b**2 == (1000-a-b)**2:
                    print(a*b*(1000-a-b))
                    return

if __name__ == "__main__":
    project_euler_9()

    raw_input("Press Enter to Continue...")
