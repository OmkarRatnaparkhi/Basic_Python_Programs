
"""
    Problem statement :  Accept one character from user and convert case of that character.
Input : a Output : A
Input : D Output : d

"""
##############################################################################################################################################
# 
#   Python ord() and chr() are built-in functions. They are used to convert a character to an int and vice versa.
#
#   Python ord() and chr() functions are exactly opposite of each other.
#
#   Python chr() function takes integer argument and return the string representing a character at that code point.
#
#   Since chr() function takes an integer argument and converts it to character, there is a valid range for the input.
#
##############################################################################################################################################


def DisplayConvert(cValue):
    if(cValue>='A' and cValue<='Z'):
        cValue1 = chr(ord(cValue) + 32)
        print(cValue1)
    elif(cValue>='a' and cValue<='z'):
        cValue1 = chr(ord(cValue) - 32)
        print(cValue1)
        
#Entry point function    
def main():
    i = str(input("Enter the character: "))
    
    DisplayConvert(i)
    
#Code Starter
if __name__ == "__main__":
    main()