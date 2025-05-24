import os, random

def main():
    intro()

def intro():
    clear_screen()
    print("-"*50, "MAGIC NUMBER", "-"*50)
    print("I have number between 1 and 10. Can you guess it?")
    print("You have 3 tries to guess.")

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

    min_number = 1
    max_number = 10
    magic_number = random.randint(min_number, max_number)

    player_guess = get_player_guess()

    while magic_number != player_guess:
        tries -=1
        if tries == 0: break
        
        clear_screen()
        print(f"Wrong guess. You have {tries} tries left. Try again.")
        player_guess = get_player_guess()
    
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