###################################################################################################
#Problem statement : Print Triangle Pattern using Nested Loops
# Expected Output:
#                  *
#                  * *
#                  * * *
#                  * * * *
###################################################################################################
def Pattern():
    
    for i in range(1,5):
        for j in range(1,i+1):
                print("*",end="\t")               
        print(end ="\n")

def main():
   Pattern()
      
if __name__ == "__main__":
    main()