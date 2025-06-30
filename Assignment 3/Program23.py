###################################################################################################
#Problem statement :Write a program which accept N numbers from user and store it into List. 
#                   Return Minimum number from that List.
#Input : Number of elements : 4
#Input Elements : 13 5 45 7
#Output : 5
###################################################################################################
def Minimum(Input):
    j = Input[0]
    for i in Input :
        if(j>i):
            j = i
    return j  
        
       
def main():
    Data = []
    print("Enter the total number")
    Size =int(input())
    print("Enter the number")
    
    for i in range (Size):
       no = int(input())
       Data.append(no)
    print("Input Data",Data)   

    iRet =Minimum(Data)
    print(iRet)
    
if __name__ =="__main__":
    main()