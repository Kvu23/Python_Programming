# program to understand functions and variable scopes

z = 10 # global variable

def sum(a, b):
    '''this program will
    add two numbers and print the sum'''
    z = a + b # local variable
    print("Sum is:", z)
    
print(sum.__doc__)
sum(2,7)
print("Global variable z is:",z)

def myfunc():
    '''this function will change the value of global variable z'''
    
    global z # to use the global variable z
    z = 5 # changing the value of global variable z
    print("Value of global variable z inside myfunc is:",z)

print(myfunc.__doc__)
myfunc()
print("Value of global variable z outside myfunc after modifications is:",z)

