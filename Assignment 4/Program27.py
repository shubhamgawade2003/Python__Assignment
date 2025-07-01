###################################################################################################
#Problem statement :Write a program which contains one lambda function which accepts two parameters
#                   and return its multiplication.
#Input : 4 3 Output : 12
#Input : 6 3 Output : 18
###################################################################################################

Power = lambda X,Y :  X*Y

def main():
    print("Enter the first input")
    X =int(input())
    
    print("Enter the Second input")
    Y =int(input())
    
    ret =Power(X,Y)
    print("Multiplication of given number is :",ret)

if __name__=="__main__":
    main()