#!/usr/bin/env python
"""Solution to Problem 18 of Project Euler.

See http://projecteuler.net/index.php?section=problems&id=18 for the details.
"""

__author__ = "Charles Patterson"
__copyright__ = "Copyright 2010"
__credits__ = []

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charles Patterson"
__email__ = "charles@cmpatterson.com"
__status__ = "Production"

t = [[75],
    [95,64],
    [17,47,82],
    [18,35,87,10],
    [20,04,82,47,65],
    [19,01,23,75,03,34],
    [88,02,77,73,07,63,67],
    [99,65,04,28,06,16,70,92],
    [41,41,26,56,83,40,80,70,33],
    [41,48,72,33,47,32,37,16,94,29],
    [53,71,44,65,25,43,91,52,97,51,14],
    [70,11,33,28,77,73,17,78,39,68,17,57],
    [91,71,52,38,17,14,91,43,58,50,27,29,48],
    [63,66,04,68,89,53,67,30,73,16,69,87,40,31],
    [04,62,98,27,23,9,70,98,73,93,38,53,60,04,23]]

def project_euler_18():
    """Finds the maximum sum traveling through the given triangle
    using Dynamic Programming.
    
    The triangle has overlapping sub-problems and a sub-optimal substructure.
    Thus DP is a great choice for solving the problem.
    Because of the data's triangle structure, implementation details get hairy,
    but the general solution is given by the formula:
    m[i][j] = max(m[i-1][j-1], m[i-1][j]) + t[i][j]
    The many cases are due to avoiding out-of-bounds cases"""

    m = []
    t_height = len(t)
    for i in range(t_height):

        m.append([])
        t_row_width = len(t[i])

        for j in range(t_row_width):
            # Bottom Row Case
            if i == 0:
                m[i].append(t[i][j])
            # Left Endpoint Case
            elif j == 0:
                m[i].append(m[i-1][j] + t[i][j])
            # Right Endpoint Case
            elif j == t_row_width-1:
                m[i].append(m[i-1][j-1] + t[i][j])
            # Middle Case
            else:
                m[i].append(max(m[i-1][j-1], m[i-1][j]) + t[i][j])

    print(max([x for x in m[len(t)-1]]))

if __name__ == "__main__":
    project_euler_18()
    
    raw_input("Press Enter to continue...")
