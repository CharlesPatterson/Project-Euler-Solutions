from Euler import is_prime

def project_euler_3():
    '''Prints the largest prime factor of 600851475143.
    See the is_prime method in Euler.py for more details.'''
    print(max(i for i in range(1, int(600851475143**.5) +1) if 600851475143 % i == 0 and is_prime(i)))

if __name__ == "__main__":
    project_euler_3()

    input("Press Enter to Continue.")
