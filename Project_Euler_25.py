#!/usr/bin/env python
"""Solution to Problem 25 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=25 for the details.
"""

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_25():
    """Calculates the first term in the Fibonacci sequence to contain
    over 1000 digits."""

    f1,f2,n = 1,1,2
    while len(str(f2)) < 1000:
        f1,f2 = f2,f1+f2
        n += 1

    print(n)

if __name__ == "__main__":
    project_euler_25()
    
    raw_input("Press Enter to continue...")
