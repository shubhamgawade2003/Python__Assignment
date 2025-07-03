###################################################################################################
#Problem statement : Write a function that accepts a string and checks whether it is a palindrome.
# Expected Input:
# Enter a string: radar
# Expected Output:
# radar is a palindrome.
###################################################################################################

def CheckPalindrome(str1):
    str2 = ''
    for i in range(len(str1), 0, -1):
        str2 += str1[i - 1]  
    return str1 == str2

def main():
    bRet = False
    print("Enter the string")
    String = input()

    bRet = CheckPalindrome(String)

    if (bRet == True):
        print(String + " is a palindrome.")
    else:
        print(String + " is not a palindrome.")

if __name__ == "__main__":
    main()
