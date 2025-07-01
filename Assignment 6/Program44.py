###################################################################################################
#Problem statement :Accept 5 numbers from the user. Find and print the largest number.
# Expected Input:
# Enter 5 numbers: 23 89 12 56 45
# Expected Output:
# Maximum number is: 89
###################################################################################################
def MaximumNum(numbers):
    max_num = numbers[0] 
    for i in range(1, 5):
        if (numbers[i] > max_num):
            max_num = numbers[i]
    return max_num
                       
def main():
   Data =[]
   iRet = 0
   print("Enter the  5 numbers")

   for i in range(5):
        no = int(input())
        Data.append(no)

   iRet= MaximumNum(Data)
   print("Maximum no is",iRet)
      
if __name__ == "__main__":
    main()