# example of fstrings in python

name = 'kaushik chauhan'
Language = 'python'

# using fstrings to print the values of variables
print(f'Hello, my name is {name} and I am learning {Language}.')
print('Hello, my name is {} and I am learning {}.'.format(name, Language))

# prints all the methods available for string objects
print(dir(str))  