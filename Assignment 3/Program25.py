###################################################################################################
#Problem statement :Write a program which accept N numbers from user and store it into List. 
#                   Return addition of all prime numbers from that List. Main python file accepts
#                   N numbers from user and pass each number to ChkPrime() function which is part 
#                   of our user defined module named as MarvellousNum. Name of the function from 
#                   main python file should be ListPrime().
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#Output : 54 (13 + 5 + 7 +2 + 5)
###################################################################################################

#MarvellousNum.py
def ChkPrime(no):
    if no < 2:
        return False
    for i in range(2, int(no / 2) + 1):
        if no % i == 0:
            return False
    return True

#main.py
#import MarvellousNum 
def ListPrime():
    Data = []
    print("Enter the number of elements:")
    Size = int(input())

    print(f"Enter {Size} numbers:")
    for i in range(Size):
        num = int(input())
        Data.append(num)

    sumPrimes = 0
    for number in Data:
        if ChkPrime(number):
            sumPrimes += number

    print("Addition of prime numbers is:", sumPrimes)

def main():
    ListPrime()

if __name__ == "__main__":
    main()
