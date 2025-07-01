###################################################################################################
#Problem statement :Write a program which contains one lambda function which accepts one parameter 
#                   and return power of two.
#Input : 4 Output : 16
#Input : 8 Output : 64
###################################################################################################

Power = lambda A :  A**2

def main():
    print("Enter the input")
    X =int(input())
    ret =Power(X)
    print(ret)

if __name__=="__main__":
    main()