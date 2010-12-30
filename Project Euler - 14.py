#!/usr/bin/env python
"""Solution to Problem 14 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=14 for the details.
"""

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

collatz_memo = {1:1}

def collatz(n):
    """Calculates the length of the Collatz sequence of n 
    recursively using memoization to speed up calculations."""
    if not collatz_memo.has_key(n):
        if n % 2 == 0:
            collatz_memo[n] = collatz(n/2) + 1
        else:
            collatz_memo[n] = collatz(3*n + 1) + 1
    return collatz_memo[n]

def project_euler_14():
    """Calculates which number under 1 million has the longest Collatz chain."""

    # Starting from the highest number going backwards 
    # encourages the memoization dict to grow faster
    for j in range(10**6,0,-1):
        collatz(j)

    # Search the dict for the highest valued key
    best = (0, 0)
    for k,v in collatz_memo.items():
        if v > best[1]:
            best = (k,v)

    print(best)

if __name__ == "__main__":
    project_euler_14()

    raw_input("Press Enter to Continue.")
