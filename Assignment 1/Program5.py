###################################################################################################
#Problem statement : Write a program which display 10 to 1 on screen.
#Output : 10 9 8 7 6 5 4 3 2 1
#                   
#################################################################################################
def Display(iNo):
    for i in range(iNo,0,-1):
        print(i,end="\t")

def  main():
    Display(10) 
    
if __name__ =="__main__" :
    main()