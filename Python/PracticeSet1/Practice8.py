#WAP for odd and even programs

number = int(input("input number: "))

if(number % 2 == 0):
    print("even number")
else:
    print("Odd number")
    
#greatest of 3 numbers

number1 = int(input("input number: "))
number2 = int(input("input number: "))
number3 = int(input("input number: "))

if(number1 > number2 and number1 > number3):
    print(number1, "is greatest number")
elif(number2 > number3):
    print(number2, "is greatest number")
else:
    print(number3, "is greatest number")
    
#WAP to check number is divisible by 7 or not

number = int(input("enter number: "))

if(number % 7 == 0):
    print(number,"is divisible by 7")
else:
    print(number,"is not divisible by 7")

