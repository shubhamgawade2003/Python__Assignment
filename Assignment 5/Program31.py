###################################################################################################
#Problem statement : Arithmetic Operations on Two Numbers
# Write a program to accept two integers from the user and display their:
#• Sum
#• Difference
#• Product
#• Division
# Expected Input:
# Enter first number: 10
# Enter second number: 2
# Expected Output:
# Sum: 12
# Difference: 8
# Product: 20
# Division: 5.0
###################################################################################################
def Sum(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def Difference(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def Product(No1,No2):
    Ans = 0
    Ans = No1 * No2
    return Ans

def Division(No1,No2):
    Ans = 0
    Ans = No1 / No2
    return Ans

def main():
    iRet = 0
    
    print("Enter the first number :")
    Value1 = int (input())

    print("Enter the Second number :")
    Value2 = int (input())

    iRet = Sum(Value1,Value2)
    print("Sum :",iRet)

    iRet = Difference(Value1,Value2)
    print("Difference :",iRet)

    iRet = Product(Value1,Value2)
    print("Product :",iRet)

    iRet = Division(Value1,Value2)
    print("Division :",iRet)

if __name__ == "__main__":
    main()