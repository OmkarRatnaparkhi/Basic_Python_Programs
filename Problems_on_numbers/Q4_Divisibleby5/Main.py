
#      Problem statement : Accept one number and check whether is is divisible by 5 or not.
    
from Module import*

#Entry point function
def main():
    print("Enter the number")   
    value = int(input())
    
    bRet = Divisible(value)
    if bRet == True:
        print("Number is Dvisible by 5")
    else:
        print("Number is not Dvisible by 5");

#Code Starter 
if __name__ == "__main__":
    main()