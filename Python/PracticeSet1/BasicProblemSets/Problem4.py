# This program swaps two numbers entered by the user.
def swap_numbers(num1,num2):
    print("Swap with third variable :")
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2

def Swap_numbers(num1, num2):
    print("Swap without third variables :")
    return num2, num1

print("Enter 2 numbers: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swapping:")
print("First number: ", num1)
print("Second number: ", num2)

num1, num2 = swap_numbers(num1, num2)
num1, num2 = Swap_numbers(num1, num2)

print("After swapping:")
print("First number: ", num1)
print("Second number: ", num2)



