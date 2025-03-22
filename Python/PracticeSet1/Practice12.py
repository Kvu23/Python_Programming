#get multiple input with single line of code

name, age = input("Enter your name: "), input("Enter your age: ")
print(name)
print(age)

print("what is your name? ", end="")    # end="" is used to avoid new line
name = input()  # input() function always returns a string
print("what is your age? ", end="")   # end="" is used to avoid new line
age = int(input())
print(name)
print(age)


