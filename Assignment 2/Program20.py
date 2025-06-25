###################################################################################################
#Problem statement :Write a program which accept number from user and return addition of digits 
#                   in that number.
#                   Input : 5187934 Output : 37
###################################################################################################
def Count(Value):
    iAdd = 0
    while(Value!=0):
        iDigit =Value%10
        iAdd=iAdd+iDigit

        Value=Value//10
        

    return iAdd

    
        
def main():
    print("Enter the number")
    No =int(input())

    iRet =Count(No)
    print(iRet)
    
    

if __name__ =="__main__":
    main()