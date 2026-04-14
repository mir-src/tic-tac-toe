from dataclasses import dataclass

class Game():
    def __init__(self):
        self.display_menu()
    def start_game(self):
        players = ['1','2']
        positions = {
            '1': ['1','free'],
            '2': ['2','free'],
            '3': ['3','free'],
            '4': ['4','free'],
            '5': ['5','free'],
            '6': ['6','free'],
            '7': ['7','free'],
            '8': ['8','free'],
            '9': ['9','free'],
        }
        print("The game has started")
        turn = 1
        win = False
        while True:
            self.display_board(positions)
            if turn == 1:
                choice = input("It's time for player 1 to make a move (1-9): ")
                if positions[choice][1] == 'free': 
                    positions[choice][0] = 'O'
                    positions[choice][1] = 'busy'

                if win:
                    print("Player 1 has won the game")
                    break
            else:
                self.display_board(positions)
                if turn == 1:
                    choice = input("It's time for player 1 to make a move (1-9): ")
                    if choice == '1':
                        positions['a'] = 'X'
                    elif choice == '2':
                        positions['b'] = 'X'
                    elif choice == '3':
                        positions['c'] = 'X'
                    elif choice == '4':
                        positions['d'] = 'X'
                    elif choice == '5':
                        positions['e'] = 'X'
                    elif choice == '6':
                        positions['f'] = 'X'
                    elif choice == '7':
                        positions['g'] = 'X'
                    elif choice == '8':
                        positions['h'] = 'X'
                    else:
                        positions['i'] = 'X'
                    turn = 2
                    if win:
                        print("Player 1 has won the game")
                        break
        self.display_menu()

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


    def display_board(self, pos: dict) -> str:
        print(f"""
        {pos['1'][0]} | {pos['2'][0]} | {pos['3'][0]}  
        {pos['4'][0]} | {pos['5'][0]} | {pos['6'][0]}  
        {pos['7'][0]} | {pos['8'][0]} | {pos['9'][0]}  
        """)

if __name__ == '__main__':    
    play = Game() 
  