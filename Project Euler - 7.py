from Euler import prime_generator

def project_euler_7():
    '''Prints the 10001st prime.
    See the prime_generator method in Euler.py for details.'''

    g = prime_generator()
    for i in range(10000): g.next()
    
    print(g.next())

if __name__ == "__main__":
    project_euler_7()
    
    input("Press Enter to continue...")

