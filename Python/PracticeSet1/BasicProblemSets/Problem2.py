# This program takes two numbers as input and performs basic arithmetic operations (addition, subtraction, multiplication, and division) on them.
print("Enter 2 numbers:")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

Add = num1 + num2
Sub = num1 - num2
Mul = num1 * num2

if num2 != 0:
    Div = num1 / num2
else:
    Div = "undefined (cannot divide by zero)"
    
print("Addition: ", Add)
print("Subtraction: ", Sub)
print("Multiplication: ", Mul)
print("Division: ", Div)
