def project_euler_9():
    '''Prints the product of the unique pythagorean triplet 
    for which a+b+c=1000. This is a naive brute-force solution 
    that cuts down some possibilities by framing it entirely
    in terms of a and b.'''

    for a in range(1,998):
        for b in range(a+1,998-a):
                if a**2 + b**2 == (1000-a-b)**2:
                    print(a*b*(1000-a-b))
                    return

if __name__ == "__main__":
    project_euler_9()

    input("Press Enter to Continue...")
