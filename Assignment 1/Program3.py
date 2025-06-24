###################################################################################################
# Problem Statement: Write a program which contains one function named as Add() which accepts two
#                    numbers from user and return addition of that two numbers.
#
# Input : 11 5 
# Output : 16
#                   
##################################################################################################

def Add(No1,NO2):
    Ans = 0
    Ans = No1 + NO2
    return Ans


def  main():
    print("Enter the first Number")
    No1 =int(input())
    print("Enter the Second Number")
    No2 =int(input())
    iRet=Add(No1,No2)
    print("Addition is",iRet)
    

if __name__ =="__main__" :
    main()