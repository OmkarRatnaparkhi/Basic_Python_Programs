"""
Problem statement : Accept two numbers from user and display first number in second
number of times.

Input : 12 5
Output : 12 12 12 12 12

Input : -2 3
Output : -2 -2 -2

Input : 21 -3
Output : 21 21 21

Input : -2 0
Output :
"""
from Module import*

#Entry point function
def main():
    print("Enter First number")
    no1 = int(input())
    
    print("Enter Second number")
    no2 = int(input())
    
    Display(no1,no2)

#Code Starter 
if __name__ == "__main__": 
    main()