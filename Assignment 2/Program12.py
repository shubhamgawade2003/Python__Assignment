###################################################################################################
#Problem statement : Write a program which accept one number and display below pattern.
# Input : 5
# Output : * * * * *
#          * * * * *
#          * * * * *
#          * * * * *
#          * * * * *
#                   
###################################################################################################
def Pattern(Value):
    for i in range(0,Value):
        for j in range (0,Value):
            print("*",end="\t")
        print(end="\n")


def main():
    print("Enter the number")
    No =int(input())

    Pattern(No)
    

if __name__ =="__main__":
    main()