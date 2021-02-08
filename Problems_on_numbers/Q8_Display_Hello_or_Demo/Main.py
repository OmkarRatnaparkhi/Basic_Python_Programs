
#    Problem statement :   Problem statement : Accept one number from user if number is less than 10 then print “Hello” otherwise print “Demo”
from Module import*

#Entry point function
def main():
    print("Enter the number")
    no = int(input())
    
    bRet = Display(no)
    if (bRet == True):
        print("Hello")
    else:
        print("Demo")

#Code Starter 
if __name__ == "__main__": 
    main()