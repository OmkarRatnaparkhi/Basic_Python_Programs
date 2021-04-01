
#Defination of DisplayFactor funtion
#Function Name : DisplayFactor
#Description:   It is used to display even factor numbers
#Date :          29 March 2021
#Author name :   OMKAR NARENDRA RATNAPARKHI
def DisplayFactor(value):
    
    iCnt = 0
    
    if value < 0:
        value = -value
        
    if value == 0:
        print("Invalid Input")
    
    for iCnt in range(1, value//2+1):
        if ((value%iCnt)==0 and (iCnt%2)==0):
            print(iCnt, end = " ")
   