#sample programs for print statements and variables input programs

print("hello world from python from vs code")
user_name = input('Enter your name: ')
print('hello', user_name)


#Same variable if we assign different values then data type will be changed
my_variable = 'kaushik chauhan'
print(my_variable)
my_variable = 69
print(my_variable)
my_variable = True
print(my_variable)
my_variable = None
# print(type(my_variable))
print('Data type of my_variable is:', type(my_variable))

'''Addition of two numbers program
below programs takes two numbers as input from user
and adds them and displays the result'''

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

result = (num1) + (num2)
print('The addition of two numbers', num1, 'and ',num2, 'is: ', result)



