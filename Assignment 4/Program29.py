###################################################################################################
#Problem statement :Write a program which contains filter(), map() and reduce() in it. Python
#                   application which contains one list of numbers. List contains the numbers which
#                   are accepted from user. Filter should filter out all such numbers which are even.
#                   Map function will calculate its square.Reduce will return addition of all that 
#                   numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204
###################################################################################################

from functools import reduce

CheckEven=lambda No:((No%2)==0)

Square =lambda No:No**2

Addition = lambda A,B: A+B



def main():
    Data = []
    print("Enter the total number")
    Size =int(input())
    print("Enter the number")
    
    for i in range (Size):
       no = int(input())
       Data.append(no)
    print("Input Data",Data)   

    FData = list (filter(CheckEven,Data))
    print("Filter output : ",FData)

    MData = list(map(Square,FData))
    print("Map output : ",MData)

    RData = reduce(Addition ,MData)
    print(" reduce output : ",RData)


if __name__=="__main__":
    main()