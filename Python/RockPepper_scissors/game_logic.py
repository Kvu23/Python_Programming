# write game logic here to determine winner

def detect_winner(player_choice,computer_choice):
    #check for tie first
    result = (player_choice - computer_choice) % 3
    if result == 0:
        return 0
    elif result == 1:
        return 1
    elif result == 2:
        return 2
    return None