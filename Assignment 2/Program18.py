###################################################################################################
#Problem statement :Write a program which accept one number and display below pattern.
#Output : 1
#         1 2
#         1 2 3
#         1 2 3 4
#         1 2 3 4 5
#
###################################################################################################
def Pattern(Value):
    
    for i in range(1,Value+1):
        for j in range(1,Value+1):
            if(j<=i):
                print(j,end="\t")
            else:
                break
        print(end ="\n")

    
        
def main():
    print("Enter the number")
    No =int(input())

    Pattern(No)
    
    

if __name__ =="__main__":
    main()