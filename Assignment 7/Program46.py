###################################################################################################
#Problem statement : Accept a list of integers from the user and use the map() function to double 
#                    each value.
# Expected Input:
# Enter list: [1 2 3 4 5]
# Expected Output:
# Doubled list: [2, 4, 6, 8, 10]
###################################################################################################

Double =lambda A : A*2

def main():
    Data= []
    print("Enter size of list")
    size = int(input())

    print("Enter the number")
    for i in range(size):
        no =int(input())
        Data.append(no)

    print("Input List is :",Data)    

    iRet = list(map(Double,Data))
    print("Doubled list is",iRet)


if __name__ == "__main__":
    main()