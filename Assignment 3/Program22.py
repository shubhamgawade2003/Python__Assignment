###################################################################################################
#Problem statement :2.Write a program which accept N numbers from user and store it into List. 
# Return Maximum number from that List.
#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56
###################################################################################################
def Maximum(Input):
    j = Input[0]
    for i in Input :
        if(j<i):
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

    iRet =Maximum(Data)
    print(iRet)
    
if __name__ =="__main__":
    main()