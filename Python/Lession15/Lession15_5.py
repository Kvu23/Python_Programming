# program to understand functions and variable scopes

z = 10 # global variable

def sum(a, b):
    z = a + b # local variable
    print("Sum is:", z)
    
sum(2,7)
print("Global variable z is:",z)

def myfunc():
    global z # to use the global variable z
    z = 5 # changing the value of global variable z
    print("Value of global variable z inside myfunc is:",z)
    
myfunc()
print("Value of global variable z outside myfunc after modifications is:",z)

