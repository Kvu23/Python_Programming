#main driver logic to determine winner
import game_logic
import interface

def play_game():
    while True:
        #display menu first
        interface.dispalyMenu()

        #get user choice first
        user_choice = interface.get_user_choice()

        #get computer choice
        computer_choice = interface.get_computer_choice()

        #determine winner
        if game_logic.detect_winner(user_choice,computer_choice) == 0:
            print("\n its a Tie\n")
        elif game_logic.detect_winner(user_choice,computer_choice) == 1:
            print("\n You win, computer lose!\n")
        elif game_logic.detect_winner(user_choice,computer_choice) == 2:
            print("\n You lose, computer win!\n")

        print("do you want to play again : y/Y or n/N")
        choice = input()
        if choice == "y" or choice == "Y":
            continue
        else:
            print("\n Thank you for playing rock pepper scissors, see you till next time\n")
            break
#main driver program to run game
if __name__ == "__main__":
    play_game()