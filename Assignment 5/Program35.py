###################################################################################################
#Problem statement :   Even or Odd Number Check
# Write a program to check whether the entered number is even or odd.
# Expected Input:
# Enter a number: 17
# Expected Output:
# 17 is an odd number.
###################################################################################################

def CheckEven(no):
    bFlag = False
    if(no %2 == 0):
      bFlag = True
    return bFlag  
        

def main():
    bRet = False
    print("Enter the  number :")
    No = int(input())

    bRet = CheckEven(No)
    if (bRet == True):
        print(No,"is Even number")
    else:
        print(No,"is Odd number")     

if __name__ == "__main__":
    main()