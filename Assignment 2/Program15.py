###################################################################################################
#Problem statement : Write a program which accept one number for user and check whether number 
#                    is prime or not.
#                    Input : 5 Output : It is Prime Number
#
###################################################################################################
def Prime(Value):
    if(Value <= 1):
        return False
        
    for i in range(2,int(Value/2)):
        if((Value % i)==0):
            return False
    
    return True
    
def main():
    print("Enter the number")
    No =int(input())

    bRet = Prime(No)
    if(bRet==True):
        print("It is Prime number")
    else:
        print("It is not a prime number")    
    
if __name__ =="__main__":
    main()
