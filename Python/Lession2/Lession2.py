#print arithmetic operations of 2 numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Arithmetic operators
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num2 / num1}")
print(f"Floor Division: {num1 // num2}")
print(f"Modulus: {num2 % num1}")
print(f"Exponentiation: {num2 ** num1}")

# Relational operators
print(f"Equal: {num1 == num2}")
print(f"Not Equal: {num1 != num2}")
print(f"Greater than or equal: {num1 >= num2}")
print(f"Greater than: {num1 > num2}")
print(f"Less than or equal: {num1 <= num2}")
print(f"Less than: {num1 < num2}")

#Assignment operators
num = 100
num **= 5
print(f'num: {num}')
num = 100
num //= 5
print(f'num: {num}')
num = 100
num %= 5
print(f'num: {num}')
num = 100
num /= 5
print(f'num: {num}')
num = 100
num *= 5
print(f'num: {num}')
num = 100
num -= 5
print(f'num: {num}')
num = 100
num += 5
print(f'num: {num}')
num = 100
num *= 5
print(f'num: {num}')

#Logical not operators
print(f'not False: {not False}')
print(f'not True: {not True}')
print(f'not (num2 > num1): {not (num2 > num1)}')
print(not (num1 > num2))

# and operator
val1 = True
val2 = True
print('and operator answer is: ', val1 and val2)
val2 = False
print('and operator answer is: ', val1 and val2)
val1 = False
val2 = True
print('and operator answer is: ', val1 and val2)
val1 = False
val2 = False
print('and operator answer is: ', val1 and val2)

#or operator
val1 = True
val2 = False
print("or operator answer: ", val1 or val2)
val2 = True
print("or operator answer: ", val1 or val2)
val1 = False
print("or operator answer: ", val1 or val2)
val2 = False
print("or operator answer: ", val1 or val2)
















