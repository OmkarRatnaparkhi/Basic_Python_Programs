
#Defination of Display funtion
#Function Name : Display
#Description:  It is use to display first number in second number times   
#Date :          08 Feb 2021
#Author name :   OMKAR NARENDRA RATNAPARKHI
def Display(no,frequency):

    if (frequency < 0):
        frequency = -frequency
    
    for iCnt in range (0,frequency,+1):
        print(no,end =" ")