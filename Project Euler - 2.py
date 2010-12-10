def project_euler_2_iterative():
    '''Prints the sum of all even-valued fibonacci numbers under 4 million.
    This method uses an iterative approach which is vastly more efficient
    than the naive recursive solution.'''

    sol,f1,f2 = 0,1,1
    while f2 < 4*(10**6):
            if f2 % 2 == 0:	sol += f2
            f1,f2 = f2,f1+f2

    print(sol)

if __name__ == "__main__":
    project_euler_2_iterative()

    input("Press Enter to Continue...")		
