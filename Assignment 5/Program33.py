###################################################################################################
#Problem statement : Voting Eligibility Checker
# Accept age from the user and check whether the person is eligible to vote. (Age should be
# 18 or above.)
# Expected Input:
# Enter age: 19
# Expected Output:
# Eligible to vote.
###################################################################################################

def VoteRight(AgeValue):
    bflag = False
    if(AgeValue>=18):
        bflag = True
    return bflag
    

def main():
    bRet = False
    print("Enter the Age :")
    Age = int(input())

    bRet = VoteRight(Age)
    if (bRet == True):
        print("Your are eligible to Vote")
    else:
        print("Your are not eligible Vote")    

if __name__ == "__main__":
    main()