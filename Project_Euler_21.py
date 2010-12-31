#!/usr/bin/env python
"""Solution to Problem 21 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=21 for the details.
"""
from Euler import proper_divisors

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_21():
    """Calculates the sum of all amicable numbers under 10,000.

    Two numbers m,n are amicable if d(m) = n and d(n) = m,
    where d(n) is the sum of the proper divisors of n.
    Memoization is used to speed things up a bit."""

    limit = 10000
    memo = {}
    amicables = set()

    for i in range(limit):
        for j in range(i+1, limit):
            if not memo.has_key(i):
                memo[i] = sum(proper_divisors(i))
            if memo[i] == j:
                if not memo.has_key(j):
                    memo[j] = sum(proper_divisors(j))
                if memo[j] == i:
                    amicables.add(i)
                    amicables.add(j)

    print(sum(amicables))

if __name__ == "__main__":
    project_euler_21()
    
    raw_input("Press Enter to continue...")
