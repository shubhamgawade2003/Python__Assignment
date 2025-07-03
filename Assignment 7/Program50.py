###################################################################################################
# Problem statement :  Write a function that accepts a list of integers and returns a list of prime
#                      numbers using filter().
# Expected Input:
# Enter list: 10 11 12 13 14 15 16 17
# Expected Output:
# Prime numbers: [11, 13, 17]
###################################################################################################

def CheckPrime(num):
    if num < 2:
        return 
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

def main():
    Data = []
    print("Enter size of list")
    size = int(input())

    print("Enter the numbers")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List is:", Data)

    PrimeNumbers = list(filter(CheckPrime, Data))
    print("Prime numbers:", PrimeNumbers)

if __name__ == "__main__":
    main()
