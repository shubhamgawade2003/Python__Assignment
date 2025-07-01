###################################################################################################
#Problem statement : Print Sum of Even Numbers Between 1 and 100. Use a loop to find and print the
#                    sum of all even numbers from 1 to 100.
# Expected Output:
# Sum of even numbers between 1 to 100 is: 2550
###################################################################################################
def SumEven():
    Sum= 0
    for i in range(2,101,2):
        Sum = Sum + i
    return Sum

def main():
   iRet = 0
   iRet = SumEven()
   print("Sum of even numbers between 1 to 100 :",iRet)
   
if __name__ == "__main__":
    main()