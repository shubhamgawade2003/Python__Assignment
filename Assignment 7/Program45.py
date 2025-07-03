###################################################################################################
#Problem statement :Write two lambda functions:
# • One to calculate square of a number
# • Another to calculate cube of a number
# Expected Input:
# Enter a number: 3
# Expected Output:
# Square: 9
# Cube: 27
###################################################################################################

Square =lambda A : A**2
Cube =lambda A : A**3

def main():
    iRet = 0
    print("Enter the number")
    no = int(input())

    iRet = Square(no)
    print("Square:",iRet)

    iRet = Cube(no)
    print("Cube:",iRet)


if __name__ == "__main__":
    main()