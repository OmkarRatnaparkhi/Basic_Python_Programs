
"""
    Problem statement :  Write a program which accept number from user and print even factors of that
number.
Input : 24
Output: 1 2 4 6 8 12
"""

from Module import*
    
#Entry point function    
def main():
    num = int(input("Enter the number: "))
    
    DisplayFactor(num)
    
#Code Starter
if __name__ == "__main__":
    main()