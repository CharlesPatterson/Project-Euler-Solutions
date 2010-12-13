from Euler import lcm

def project_euler_5():
    '''Prints the smallest number divisible by the numbers 1 to 20.
    Intuitively, the number must be the lcm(1,2,3,...,20).
    It's not hard to show that this will produce the minimum number
    with the required factors. 
    See the lcm method in Euler.py for more details.'''
    j = 1
    for i in range(1,21):
        j = lcm(j,i)
        
    print(j)

if __name__ == "__main__":
    project_euler_5()

    input("Press Enter to Continue...")
