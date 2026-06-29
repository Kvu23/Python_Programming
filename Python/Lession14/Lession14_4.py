# program to understand the if-else statement
Age = int(input("Enter Person's age: "))
print("You entered:", Age)

if Age < 0:
    print("Invalid age. Age cannot be negative.")
elif Age >= 18:
    print("The person can vote.")
elif Age < 18:
    print("The person is not yet eligible to vote.")
