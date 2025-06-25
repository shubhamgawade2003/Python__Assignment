###################################################################################################
#Problem statement :Write a program which accept number from user and return number of digits in
#                   that number.
#Input : 5187934 Output : 7
###################################################################################################
def Count(Value):
    iCount = 0
    while(Value!=0):
        
        Value=Value//0
        iCount=iCount+1

    return iCount

    
        
def main():
    print("Enter the number")
    No =int(input())

    iRet =Count(No)
    print(iRet)
    
    

if __name__ =="__main__":
    main()