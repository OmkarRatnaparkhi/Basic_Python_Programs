
"""
    Problem statement :  Accept on character from user and check whether that character is vowel
(a,e,i,o,u) or not.
Input : E Output : TRUE
Input : d Output : FALSE

"""
def ChkVowel(cValue):     	
   
    if cValue in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    else:
        return False
        
        
#Entry point function    
def main():
    i = str(input("Enter the character: "))
    
    ret = ChkVowel(i)
    if ret == True:
        print("Character is vowel")
    else:
        print("Character is not vowel")
    
#Code Starter
if __name__ == "__main__":
    main()
    