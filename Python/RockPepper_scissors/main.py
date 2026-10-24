#main driver logic to determine winner
import game_logic
import interface

def play_game():
    #while True:
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

        #break
#main driver program to run game
if __name__ == "__main__":
    play_game()