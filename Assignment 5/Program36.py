###################################################################################################
#Problem statement :  Celsius to Fahrenheit Converter
# Accept temperature in Celsius and convert it to Fahrenheit using the formula:
# F = (C × 9/5) + 32
# Expected Input:
# Enter temperature in Celsius: 25
# Expected Output:
# Temperature in Fahrenheit: 77.0°F
###################################################################################################

def ConvertFahrenheit(no):
    Ans = 0
    Ans =(no *9/5) +32
    return Ans 
        

def main():
    fRet = 0.0
    print("Enter the temperature in Celsius : ")
    No = int(input())

    fRet = ConvertFahrenheit(No)

    print("Temperature in Faherenheit :",fRet,"F")    

if __name__ == "__main__":
    main()