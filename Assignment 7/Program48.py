###################################################################################################
#Problem statement : Accept a list of numbers and use reduce() (from functools) to find the product 
#                    of all numbers.
# Expected Input:
# Enter list: 2 3 4
# Expected Output:
# Product: 24
###################################################################################################
from functools import reduce

Product =lambda A ,B : A * B

def main():
    Data= []
    print("Enter size of list")
    size = int(input())

    print("Enter the number")
    for i in range(size):
        no =int(input())
        Data.append(no)

    print("Input List is :",Data)    

    iRet = reduce(Product,Data)
    print("Product:",iRet)

if __name__ == "__main__":
    main()