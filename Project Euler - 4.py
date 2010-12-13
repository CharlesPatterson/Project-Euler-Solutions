from Euler import is_palindrome

def project_euler_4():
    '''Prints the largest palindrome made from the product of two 3-digit numbers.
    See the is_palindrome method in Euler.py for more details.'''
    print(max(i*j for i in range(100,1000) for j in range(100,1000) if is_palindrome(str(i*j))))

if __name__ == "__main__":
    project_euler_4()

    input("Press Enter to Continue...")		
