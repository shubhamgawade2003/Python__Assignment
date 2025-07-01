###################################################################################################
#Problem statement :  Find Largest Among Three Numbers
# Accept three numbers from the user and print the largest using nested if-else statements.
# Expected Input:
# Enter three numbers: 5 9 3
# Expected Output:
# Largest number is 9.
###################################################################################################

def CheckLargest(no1,no2,no3):
    if(no1 == no2 ==no3):
        print("Numbers are equal")
        return
    if(no1>no2 and no1 >no3):
        print("Largest number is ",no1)
    elif(no2>no1 and no2>no3):
        print("Largest number is ",no2) 
    else:
        print("Largest number is ",no3)   

def main():
    print("Enter the first number :")
    No1 = int(input())

    print("Enter the Second number :")
    No2 = int(input())
    
    print("Enter the Third number :")
    No3 = int(input())

    CheckLargest(No1,No2,No3)   

if __name__ == "__main__":
    main()