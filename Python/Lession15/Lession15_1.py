#example of function and arguments
def greet(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old.")

greet("Kaushik chauhan", 36)  # Output: Hello Kaushik chauhan, you are 36 years old. if argumrnts are passed, those values will be used. it is called positional arguments.

def greetings(name = "guest", age = 0):
    print("Hello " + name + ", you are " + str(age) + " years old.")

greetings()  # Output: Hello guest, you are 0 years old. if no arguments are passed, default values will be used. this is called default arguments.

def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet_user("Kaushik chauhan", 36)  # Output: Hello Kaushik chauhan, you are 36 years old." + name + ", you are " + str(age) + " years old.")

greet_user(age=36, name="Kaushik chauhan") #this is called keyword arguments. here we are passing the arguments in different order but still it will work because we are using the keywords to specify the arguments.

#simple functions to understand the concept of function and arguments and return values
def add(a, b):
    c = a + b
    # print(f"The sum of {a} and {b} is {c}")
    return c

result = add(5, 10)  # Output: The sum of 5 and 10 is 15
print("result of additions is ",   result)  
