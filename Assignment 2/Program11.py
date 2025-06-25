###################################################################################################
#Problem statement : Create on module named as Arithmetic which contains 4 functions as Add() for
#                    addition, Sub()for subtraction, Mult() for multiplication and Div() for
#                    division. All functions accepts two parameters as number and perform the 
#                    operation. Write on python program which call all the functions from 
#                    Arithmetic module by accepting the parameters from user.
#                   
###################################################################################################

import Arthmetic as A

def main():
    print("Enter the first number")
    No1 =int(input())
    print("Enter the Second number")
    No2 =int(input())

    iRet =A.Add(No1,No2)
    print("Addition is :",iRet)

    iRet =A.Sub(No1,No2)
    print("Substraction is :",iRet)

    iRet =A.Mult(No1,No2)
    print("Multiplication is :",iRet)

    iRet =A.Div(No1,No2)
    print("Division is :",iRet)

if __name__ =="__main__":
    main()