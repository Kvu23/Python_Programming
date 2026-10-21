import interface
import operations

#this is the main Driver programs
def run_calculator():
    while True:
        #1 display menu
        interface.displaymenu()

        #get the choice
        choice = interface.get_user_choice()
        if choice == 5:
            print("\nThank you for choosing Sample calculator application")
            break

        if choice not in [1,2,3,4]:
            print("Please choose from 1,2,3,4")
            continue

        number1,number2 = interface.get_numbers()

        if choice == 1:
            result = operations.addition(number1,number2)
            print(f"\nResult : {number1} + {number2} = {result}")
        elif choice == 2:
            result = operations.substraction(number1, number2)
            print(f"\nResult : {number1} - {number2} = {result}")
        elif choice == 3:
            result = operations.multiplication(number1, number2)
            print(f"\nResult : {number1} * {number2} = {result}")
        elif choice == 4:
            result = operations.division(number1, number2)
            print(f"\nResult : {number1} / {number2} = {result}")

#main programs run
if __name__ == "__main__":
    run_calculator()
