from Euler import sum_of_squares, triangle_number

def project_euler_6():
    '''Prints [the sum of the squares] -  [the square of the sum]
       of the first 100 natural numbers.
       See Euler.py for the two formulas used.'''
    print(sum_of_squares(100) - triangle_number(100)**2)

if __name__ == "__main__":
    project_euler_6()

    input("Press Enter to Continue...")
