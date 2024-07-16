from pyfiglet import Figlet
import os
import sys

def main():
    while True:    
        play_game = start_game()
        if play_game == False:
            clear_screen()
            f = Figlet(font="bubble", justify="center", width=80)
            print(f.renderText("Thanks for Playing"))
            sys.exit()
        clear_screen()
        maze = get_maze()

def clear_screen():
    return os.system("cls" if os.name=="nt" else "clear")

def get_maze():
    #return maze from one of the options in a file
    ...

def print_maze():
    ...

def move_character(move):
    #moves character in maze
    ...

def check_win():
    #check if character is in winning location
    ...

def start_game():
    while True:
        clear_screen()
        f = Figlet(font="epic", justify="center", width=80)
        print(f.renderText("Welcome to Mazed"))
        print("\n\n") 
        try:
            answer = input("What do you want to do?\n\n(1) Start Game\n\n(2) Quit\n\n")
            if answer == "1":
                return True
            elif answer == "2":
                return False
            else:
                continue
        except ValueError:
            pass

if __name__ == "__main__":
    main()