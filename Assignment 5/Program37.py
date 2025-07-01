###################################################################################################
#Problem statement : Area and Perimeter of Rectangle
# Accept the length and width of a rectangle. Calculate and display the area and perimeter.
# Expected Input:
# Enter length: 5
# Enter width: 3
# Expected Output:
# Area: 15
# Perimeter: 16
###################################################################################################

def Perimerter(Lvalue,Wvalue):
    Ans = 0
    Ans = (2*Lvalue)+(2*Wvalue)
    return Ans 
def Area(Lvalue,Wvalue):
    Ans = 0
    Ans = Lvalue * Wvalue
    return Ans         

def main():
    iARet = 0
    iPRet =0
    print("Enter the Length : ")
    Length = int(input())

    print("Enter the Width : ")
    Width = int(input())

    iPRet = Perimerter(Length,Width)
    iARet = Area(Length,Width)

    print("Area :",iARet)
    print("Perimeter :",iPRet)

if __name__ == "__main__":
    main()