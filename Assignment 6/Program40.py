###################################################################################################
#Problem statement : Accept a number from the user and print its multiplication table up to 10.
# Expected Input:
# Enter a number: 7
# Expected Output
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
###################################################################################################
def Table(NO):

    for i in range(1,11):
        print(NO,"x",i,"=",NO*i)


def main():
   print("Enter the number")
   no = int(input())
   Table(no)
   
if __name__ == "__main__":
    main()