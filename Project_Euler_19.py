#!/usr/bin/env python
"""Solution to Problem 19 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=19 for the details.
"""
from datetime import datetime

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

def project_euler_19():
    '''Prints the number of sundays from 1901 to 2001.'''
    print(len([y for y in range(1901,2001) for m in range(1,13) if datetime(y,m,1).weekday() == 6]))
    
if __name__ == "__main__":
    project_euler_19()

    raw_input("Press Enter to Continue...")
