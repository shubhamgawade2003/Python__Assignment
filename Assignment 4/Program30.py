###################################################################################################
#Problem statement :Write a program which contains filter(), map() and reduce() in it. Python
#                   application which contains one list of numbers. List contains the numbers which
#                   are accepted from user. Filtershould filter out all prime numbers. Map function
#                   will multiply each number by 2. Reduce will return Maximum number from that 
#                   numbers.(You can also use normal functions instead of lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62
###################################################################################################

from functools import reduce

def ChkPrime(no):
    if no < 2:
        return False
    for i in range(2, int(no / 2) + 1):
        if no % i == 0:
            return False
    return True

def Double(no):
    return no * 2

def Maximum( A, B):
    return A if A > B else B

def main():
    Data = []

    print("Enter the total number of elements:")
    Size = int(input())

    print("Enter  numbers:")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data:", Data)

    FData = list(filter(ChkPrime, Data))
    print("After filter (prime numbers):", FData)

    MData = list(map(Double, FData))
    print("After map (doubled values):", MData)
 
    RData = reduce(Maximum, MData)
    print("After reduce (maximum value):", RData)
    
if __name__ == "__main__":
    main()
