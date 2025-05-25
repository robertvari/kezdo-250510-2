import os, random, time

MIN_NUMBER = 1
MAX_NUMBER = 100
CREDITS = 10


def main():
    intro()
    input("Press Enter to continue...")
    game_loop()

def intro():
    clear_screen()
    print("-"*50, "MAGIC NUMBER", "-"*50)
    print(f"I have a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?")
    print("You have 3 tries to guess.")
    print(f"You start with {CREDITS} credits. If you can guess my number you win 1 credit.")
    print("But if you lost all your credits the game ends.\n")

def exit_game():
    clear_screen()
    print("Thank you for playing my game :)))")

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_player_guess():
    result = input("What is your guess? ")

    valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    while result not in valid_numbers:
        clear_screen()
        print("Wrong number.")
        result = input("What is your guess? ")
    
    return int(result)

def game_loop():
    clear_screen()

    tries = 3
    print(f"You have {tries} tries.")

    magic_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    magic_number = 5  # for testing the game

    player_guess = get_player_guess()

    while magic_number != player_guess:
        tries -=1
        if tries == 0: break
        
        clear_screen()
        print(f"Wrong guess. You have {tries} tries left. Try again.")
        player_guess = get_player_guess()
    
    end_game_conditions(magic_number, player_guess)

def end_game_conditions(magic_number, player_guess):
    clear_screen()
    if magic_number == player_guess:
        print("You win! :))")
    else:
        print("You lost this round")

    player_response = input("Do you want to play again? (y/n)")
    if player_response == "y":
        game_loop()
    else:
        exit_game()


main()