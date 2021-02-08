
#    Problem statement : Accept two numebrs from user and return its division.

from Arithematic import*

#Entry point function
def main():
    print("Enter First number")
    value1 = int(input())
    
    print("Enter Second number")
    value2 = int(input())
    
    ret1 = Division(value1,value2)
    
    print("Division of two numbers is : ",ret1)

#Code Starter
if __name__ == "__main__":
    main()