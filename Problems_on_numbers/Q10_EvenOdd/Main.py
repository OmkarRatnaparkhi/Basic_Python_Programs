
#    Problem statement : Problem statement :Accept number from user and check whether number is even or odd.
from Module import*

#Entry point function
def main():
    print("Enter the number")
    no = int(input())
    
    bRet = EvenOdd(no)
    if (bRet == True):
        print("Number is even")
    else:
        print("Number id odd")

#Code Starter 
if __name__ == "__main__": 
    main()