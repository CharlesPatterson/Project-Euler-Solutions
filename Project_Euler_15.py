#!/usr/bin/env python
"""Solution to Problem 15 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=15 for the details.
"""
from math import factorial

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_15():
    """Prints the number of routes in a 20x20 grid from the top-left 
    to the bottom-right."""
    print(factorial(40)/(factorial(20))**2)

if __name__ == "__main__":
    project_euler_15()

    raw_input("Press Enter to Continue...")
