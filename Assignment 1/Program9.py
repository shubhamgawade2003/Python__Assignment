###################################################################################################
#Problem statement : Write a program which display first 10 even numbers on screen.
#Output : 2 4 6 8 10 12 14 16 18 20
#                   
#################################################################################################
def Display():
    num = 2
    for i in range(10) :
        print(num,end="\t")
        num =num+2

def  main():
    Display() 
    
if __name__ =="__main__" :
    main()