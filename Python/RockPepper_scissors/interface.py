# function for menu to display
import random

def dispalyMenu():
    print("Welcome to Rock Paper Scissors!")
    print("Please enter your choice between 0 -2: ")
    print("0. Rock")
    print("1. Paper")
    print("2. Scissors")

def get_user_choice():
    while True:
        #print("Please enter your choice between 0 -2: ")
        try:
            user_choice = int(input())
            print("user entered choice: ", user_choice)
            if user_choice not in [0,1,2]:
                print("Please choose between 0 to 2")
                continue
            else:
                return user_choice
        except ValueError:
            print("Please choose between 0 to 2")

def get_computer_choice():
    while True:
        computer_choice = random.randint(0,2)
        print("Computer choice: ", computer_choice)
        if computer_choice not in [0, 1, 2]:
            print("Please choose between 0 to 2")
            continue
        else:
            return computer_choice
