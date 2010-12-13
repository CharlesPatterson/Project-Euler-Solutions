from Euler import prime_sieve

def project_euler_10():
    '''Prints the sum of all the primes below two million.
    See the prime_sieve method in Euler.py for more details.'''

   # print(sum(prime_sieve(10)))
    print(sum(prime_sieve(2*10**6)))
    
if __name__ == "__main__":
    project_euler_10()

    input("Press Enter to Continue...")
