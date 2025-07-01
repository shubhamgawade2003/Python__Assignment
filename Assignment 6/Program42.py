###################################################################################################
#Problem statement : Accept a number from the user and check whether it is prime or not.
# Expected Input:
# Enter a number: 11
# Expected Output:
# 11 is a prime number.
###################################################################################################
def PrimeCheck(NO):
    bFlag = False
    if(NO<1):
        return bFlag
    for i in range(2,int(NO/2)+2):
        if((NO % i)== 0):
            break
        else:
           bFlag = True
    return bFlag

def main():
   bRet = False

   print("Enter the number")
   no = int(input())
   
   bRet = PrimeCheck(no)
   if(bRet== True):
    print(no,"is prime number")
   else:
    print(no ,"is not a prime number")
      
if __name__ == "__main__":
    main()