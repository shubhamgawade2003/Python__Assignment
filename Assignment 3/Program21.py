###################################################################################################
#Problem statement :Write a program which accept N numbers from user and store it into List.
#                   Return addition of all elements from that List.
#Input : Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output : 130
###################################################################################################
def Addition(Input):
    iAdd = 0
    
    for i in Input :
        iAdd = iAdd + i
    return iAdd
      
def main():
    Data = []
    print("Enter the total number")
    Size =int(input())
    print("Enter the number")
    
    for i in range (Size):
       no = int(input())
       Data.append(no)
    print("Input Data",Data)   

    iRet =Addition(Data)
    print(iRet)
    
if __name__ =="__main__":
    main()