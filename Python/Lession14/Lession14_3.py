# This program prompts the user to enter a number and then checks whether the number is positive, negative, or zero. It uses conditional statements (if, elif, else) to determine the category of the number and prints the appropriate message.

number = int(input("Enter a number: "))
print("You entered:", number)

if number == 0:
    print("The number is zero.")
elif number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")
    

