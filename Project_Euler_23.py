#!/usr/bin/env python
"""Solution to Problem 23 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=23 for the details.
"""
from Euler import is_abundant

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_23():
    """Finds the sum of all numbers under 28124 that can't be written
    as the sum of two abundant numbers."""

    limit = 28124
    abundants = set([x for x in range(limit) if is_abundant(x)])

    abundant_sums = set()
    for x in abundants:
        for y in abundants:
            abundant_sums.add(x+y)

    print(sum([x for x in range(limit) if x not in abundant_sums]))
   
if __name__ == "__main__":
    project_euler_23()
    
    raw_input("Press Enter to continue...")
