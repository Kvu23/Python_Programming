# this programs demonstrates core logic of number guessing game in python using random library
import interface
import game_logic

def play_number_guessing():
    attempt_count = 0
    # display greetings
    interface.displaygreetings()
    #get the number here
    number = interface.get_computer_choice()

    #start main loop
    while True:
        #get the user guess here
        user_guess = interface.get_user_guess()

        #increment attempt count
        attempt_count = attempt_count + 1

        #check number guess here perform logic
        result = game_logic.guess_number(user_guess,number)
        if result == True:
            print(f"You guess correct number {number} in {attempt_count}")
        else:
            print(f"You guess incorrect, try again")
            continue

        #ask for playing game again or not
        print(f'do you want to play again? [y/n]')
        userchoices = input()

        #compare user choice
        if userchoices.lower() == 'y':
            #reset user attempt again here
            attempt_count = 0
            #get the new number here
            number = interface.get_computer_choice()
            continue
        else:
            break

if __name__ == "__main__":
    play_number_guessing()