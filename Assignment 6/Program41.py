###################################################################################################
#Problem statement : Accept a number and print its factorial using a for loop.
# Expected Input:
# Enter a number: 5
# Expected Output:
# Factorial of 5 is: 120
###################################################################################################
def Factorial(NO):
    if(NO<=0):
        return 
    iFact = 1
    for i in range(1,NO+1):
        iFact = iFact * i
    return iFact

def main():
   iRet = 0
   print("Enter the number")
   no = int(input())
   iRet = Factorial(no)
   print("Factorial of ",no,"is :",iRet)
   
if __name__ == "__main__":
    main()