###################################################################################################
#Problem statement : Accept a list of numbers and use filter() to keep only even numbers.
# Expected Input:
# Enter list: 1 2 3 4 5 6
# Expected Output:
# Even numbers: [2, 4, 6]
###################################################################################################

Even =lambda A : A % 2==0

def main():
    Data= []
    print("Enter size of list")
    size = int(input())

    print("Enter the number")
    for i in range(size):
        no =int(input())
        Data.append(no)

    print("Input List is :",Data)    

    iRet = list(filter(Even,Data))
    print("Even numbers",iRet)


if __name__ == "__main__":
    main()