###################################################################################################
#Problem statement : Write a program which accept one number and display below pattern.
#Input : 5
#Output : 1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#
###################################################################################################
def Pattern(Value):
    
    for i in range(0,Value):
        for j in range(1,Value+1):
            print(j,end="\t")
        print(end ="\n")

    
        
def main():
    print("Enter the number")
    No =int(input())

    Pattern(No)
    
    

if __name__ =="__main__":
    main()