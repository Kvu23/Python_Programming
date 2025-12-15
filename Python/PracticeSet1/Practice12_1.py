#get multiple input with single line of code using split method

name, age = input("Enter your name and age separated by space: ").split(",")
print("User name is: ",name) 
print("User age is: ",age)

print("what is your name and age? ")    # end="" is used to avoid new line
name, age = input("Enter name and Age: ").split(",")  # input() function always returns a string

print("User name is: ",name) 
print("User age is: ",age)

