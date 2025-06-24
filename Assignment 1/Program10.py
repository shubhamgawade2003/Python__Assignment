###################################################################################################
#Problem statement : Write a program which accept name from user and display length of its name.
#Input : Marvellous Output : 10
#                   
#################################################################################################
def Count(Str):
    iCount=len(Str)
    return iCount

def  main():
    print("Enter the String")
    Str =input()
    Ret=Count(Str) 
    print(Ret)
    
if __name__ =="__main__" :
    main()