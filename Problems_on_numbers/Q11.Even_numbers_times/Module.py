
#Defination of Display funtion
#Function Name : Display
#Description:   It is used to display even numbers
#Date :          29 March 2021
#Author name :   OMKAR NARENDRA RATNAPARKHI
def Display(value):
    
    iCnt = 0
    
    if value < 0:
        value = -value
        
    if value == 0:
        print("Invalid Input")
    
    for iCnt in range(2, value*2+1):
        if (iCnt%2) == 0:
            print(iCnt, end = " ")
    