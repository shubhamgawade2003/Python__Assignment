###################################################################################################
#Problem statement : Write a program which accept one number from user and return its factorial.
#                    Input : 5 Output : 120
#
###################################################################################################
def Factorial(Value):
    iFact =1
    for i in range(1,Value+1):
        iFact= iFact*i
    return iFact 
        
def main():
    print("Enter the number")
    No =int(input())

    iRet =Factorial(No)
    print(iRet)
    

if __name__ =="__main__":
    main()