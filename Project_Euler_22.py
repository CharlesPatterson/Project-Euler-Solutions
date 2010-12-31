#!/usr/bin/env python
"""Solution to Problem 22 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=22 for the details.
"""
import time
import os

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_22():
    """Takes the given file with 50,000 names, converts each letter to its
    alphabetic numeric value (e.g. A=1, C=3), sums that up for each name,
    multiplies that sum by the name's line number."""
    filename = os.path.join(os.getcwd(), 'names.txt')

    names = sorted([x.strip('"') for x in open(filename,'r').read().split(',')])

    total = 0
    a = ord('A')
    for i in range(len(names)):
        total += sum([ord(b)-a+1 for b in names[i]]) * (i+1)
    print(total)

if __name__ == "__main__":
    start = time.clock()
    project_euler_22()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
