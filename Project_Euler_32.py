#!/usr/bin/env python
"""Solution to Problem 32 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=32 for the details.
"""
import time
from Euler import has_repeated_digits

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_32():
    """Calculates the sum of all numbers 
    that can be written as pandigital products.
    
    E.g. 39 * 186 = 7254 contains all the digits only once
    in a correct product."""
    result = set()

    for i in range(98766):
        if has_repeated_digits(str(i)): continue

        for j in range(98766):
            if has_repeated_digits(str(j)): continue

            digits = str(i)+str(j)

            if len(digits) > 5: break

            if has_repeated_digits(digits): continue

            prod = i*j

            if has_repeated_digits(str(prod)): continue

            digits += str(prod)

            if len(digits) != 9: continue

            if not has_repeated_digits(digits):
                result.add(prod)            

    print(sum(result))

if __name__ == "__main__":
    start = time.clock()
    project_euler_32()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")

