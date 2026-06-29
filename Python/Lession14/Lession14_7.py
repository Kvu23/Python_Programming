# This program performs basic arithmetic operations based on user input.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("You entered: ", number1, " and ", number2)

operations = input("Enter the operation (+, -, *, /): ")

match operations:
    case '+':
        result = number1 + number2
        print("Addition of two numbers is: ", result)
    case '-':
        result = number1 - number2
        print("Subtraction of two numbers is: ", result)
    case '*':
        result = number1 * number2
        print("Multiplication of two numbers is: ", result)
    case '/':
        if number2 != 0:
            result = number1 / number2
            print("Division of two numbers is: ", result)
        else:
            print("Error: Division by zero is not allowed.")
            result = None
    case _:
        print("Invalid operation")
        result = None
