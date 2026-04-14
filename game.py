from dataclasses import dataclass

class Game():
    def __init__(self):
        self.display_menu()
    def start_game(self):
        first_player = 1       
        second_player = 2
        print("The game has started")

    def display_menu(self):
        print("---MENU---")
        print("1. Start Game")
        while True:
            choice = input("Select Option: ")
            if choice == '1':
                self.start_game()
                break
            else:
                print("Please select valid option!")


if __name__ == '__main__':    
    play = Game() 
  