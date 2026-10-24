# write game logic here to determine winner

def detect_winner(player_choice,computer_choice):
    #check for tie first
    if computer_choice == player_choice:
        return 0
    elif (player_choice - computer_choice) % 3 == 1:
        return 1
    elif (player_choice - computer_choice) % 3 == 2:
        return 2