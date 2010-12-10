def project_euler_1_bruteforce():
    '''Prints the sum of the natural numbers < 1000 divisible by 3 or 5.
    This method uses brute force.'''
    print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))

if __name__ == "__main__":
    project_euler_1_bruteforce()
    
    input("Press Enter to continue...")
