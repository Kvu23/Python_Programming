# this file contain core game logic of number guessing game

def guess_number(user_guess, number):
    '''
    Guess the number game core logic starts here
    '''
    if user_guess == number:
        print(f"you guessed the number correctly")
        return True
    elif user_guess < number:
        print(f"Your guess is too low")
        return False
    elif user_guess > number:
        print(f"Your guess is too high")
        return False