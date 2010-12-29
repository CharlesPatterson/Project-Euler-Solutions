#!/usr/bin/env python
"""Solution to Problem 36 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=36 for the details.
"""
from Euler import is_palindrome

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_36():
    """Prints the sum of numbers that are palindromic and have a palindromic
    binary bit-string that are under 1 million."""
    print(sum([n for n in range(1, 1000000) if is_palindrome(str(n)) and is_palindrome(bin(n)[2:])]))

if __name__ == "__main__":
    project_euler_36()

    raw_input("Press Enter to Continue...")
