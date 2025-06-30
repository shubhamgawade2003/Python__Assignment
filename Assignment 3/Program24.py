###################################################################################################
#Problem statement :Write a program which accept N numbers from user and store it into List.
#                   Accept one another number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3
###################################################################################################
def Frequency(Input,No):
    iCount = 0
    for i in Input :
        if(i == No):
            iCount += 1
    return iCount  
        
       
def main():
    Data = []
    print("Enter the total number")
    Size =int(input())
    print("Enter the number")
    
    for i in range (Size):
       no = int(input())
       Data.append(no)
    print("Input Data",Data)   

    print("Enter number to Search")
    Value = int (input()) 

    iRet =Frequency(Data,Value)
    print(iRet)
    
if __name__ =="__main__":
    main()