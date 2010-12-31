#!/usr/bin/env python
"""Solution to Problem 10 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=10 for the details.
"""
from Euler import prime_sieve

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_10():
    '''Prints the sum of all the primes below two million.
    See the prime_sieve method in Euler.py for more details.'''

   # print(sum(prime_sieve(10)))
    print(sum(prime_sieve(2*10**6)))
    
if __name__ == "__main__":
    project_euler_10()

    raw_input("Press Enter to Continue...")
