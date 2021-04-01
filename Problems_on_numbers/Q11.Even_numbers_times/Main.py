
"""
    Problem statement :  Write a program which accept one number from user and print that number of
even numbers on screen.
Input : 7
Output: 2 4 6 8 10 12 14
"""

from Module import*
    
#Entry point function    
def main():
    num = int(input("Enter the number: "))
    
    Display(num)
    
#Code Starter
if __name__ == "__main__":
    main()