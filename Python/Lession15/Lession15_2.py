# this program is all about understanding lambda functions in python
number = float(input("Enter a number: "))
number1 = float(input("Enter another number: "))
square = lambda x: x * x
print("Square of given input is:", square(number))  # Output: 25

cube = lambda x: x * x * x
print("Cube of given input is:", cube(number))  # Output: 27

add = lambda x, y: x + y
print("Sum of given inputs is:", add(number, number1))  # Output: 7

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]