# This program takes a number as input and calculates its square, cube, double, and triple.

print("Enter the number: ")
num = float(input())

square = num ** 2
cube = num ** 3

print(f'The square of {num} is: {square}')
print(f'The cube of {num} is: {cube}')

double_num = num * 2
print(f'The double of {num} is: {double_num}')

triple_num = num * 3
print(f'The triple of {num} is: {triple_num}')


