###################################################################################################
#Problem statement : Vowel or Consonant Check
# Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not,
# print it's a consonant.
# Expected Input:
# Enter a character: e
# Expected Output:
# 'e' is a vowel.
###################################################################################################

def CheckChar(Ch):
    
    if(Ch=='A'or Ch=='E'or Ch=='I'or Ch=='O'or Ch=='U'or Ch=='a'or Ch=='e'or Ch=='i'or Ch=='o'or Ch=='u'):
        return True
    else :
        return False

def main():
    
    bRet = False
    
    print("Enter the charactor :")
    charValue = (input())

    if(charValue<'A'or charValue>'Z'and charValue<'a'or charValue>'z'):
        print("Invalid input")
        return

    bRet = CheckChar(charValue)
    
    if(bRet ==True):
        print(charValue +" is a Vowel")
    else :
        print((charValue + " is s consonant"))    

if __name__ == "__main__":
    main()