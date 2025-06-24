###################################################################################################
#Problem statement : Write a program which accept number from user and print that number of 
#                    “*” on screen.
#Input : 5 Output : * * * * *
#                   
#################################################################################################
def Display(iNo):
    for i in range(0,iNo):
        print("*",end="\t")

def  main():
    print("Enter the number")
    iValue=int(input())
    Display(iValue) 
    
if __name__ =="__main__" :
    main()