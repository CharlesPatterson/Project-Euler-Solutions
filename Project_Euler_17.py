#!/usr/bin/env python
"""Solution to Problem 17 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=17 for the details.
"""
import time
from Euler import cross

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

# Preliminary starting words
ones  = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
         "seventeen", "eighteen", "nineteen"]
tens  = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
        "eighty", "ninety"]

# Word banks for numbers in 1:1000
under_hundreds = ones + teens + tens + cross(tens, ones)
bare_hundreds               = cross(ones, ["hundred"])
hundreds_with_ones          = cross(bare_hundreds, 
                                    ["and" + one for one in ones])
hundreds_with_teens         = cross(bare_hundreds, 
                                    ["and" + teen for teen in teens])
hundreds_with_tens          = cross(bare_hundreds, 
                                    ["and" + ten for ten in tens])
hundreds_with_tens_and_ones = cross(hundreds_with_tens, ones)
thousands = ["onethousand"]

# For iteration
word_banks = [under_hundreds, bare_hundreds, hundreds_with_ones, 
              hundreds_with_teens, hundreds_with_tens, 
              hundreds_with_tens_and_ones, thousands]

def project_euler_17():
    """Calculates the number of letters in the words of the numbers 1:1000

    The words follow standard British usage (e.g. "and" joins the hundreds
    with the tens+digits column 'one hundred and twenty'). White space
    and hyphens are ignored in the calculation."""
    total = 0
    for words in word_banks:
        for word in words:
            total += len(word)
    print(total)

if __name__ == "__main__":
    start = time.clock()
    project_euler_17()
    end = time.clock()

    print("Time Taken: %f" % (end-start))
    raw_input("Press Enter to Continue...")
