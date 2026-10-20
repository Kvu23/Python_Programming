#display calculator menu first
def displaymenu():
    print("\nWelcome to simple Calculator program please choose an option")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

#get user choice
def get_user_choice():
    print("Please choose an option")
    while True:
        choice = int(input("Enter your choice: "))
        if choice >=1 and choice <=5:
            return choice
        else:
            print("invalid choice please choose between 1 and 5")
            continue

#Get the numbers from users
def get_numbers():
    while True:
        try:
            num1 = float(input("Enter a number1: "))
            num2 = float(input("Enter a number2: "))
            return num1, num2
        except ValueError:
            print("Please enter a valid numbers")