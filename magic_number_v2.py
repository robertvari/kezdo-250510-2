import os, random

def main():
    pass

def intor():
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