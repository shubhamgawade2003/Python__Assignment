###################################################################################################
#Problem statement :Write a program which accept number from user and check whether that number is 
#                     positive or negative or zero.
#
#Input : 11 Output : Positive Number
#Input : -8 Output : Negative Number
#Input : 0 Output : Zero  
#
#################################################################################################
def Display(iNo):
    if(iNo==0):
        print("Zero")
    elif(iNo>0):
        print("Positive number")
    else:
        print("Negative Number")       

def  main():
    print("Enter the number")
    iValue=int(input())
    Display(iValue) 
    
if __name__ =="__main__" :
    main()