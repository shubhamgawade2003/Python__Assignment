###################################################################################################
#Problem statement : Write a program which accept one number form user and return addition 
#                    of its factors.
#                    Input : 12 Output : 16 (1+2+3+4+6)
#
###################################################################################################
def Factors(Value):
    Add=0
    for i in range(1,int((Value/2)+1)):
        if((Value%i)==0):
            Add=Add + i
        
    return Add
        
def main():
    print("Enter the number")
    No =int(input())

    iRet =Factors(No)
    print(iRet)
    

if __name__ =="__main__":
    main()