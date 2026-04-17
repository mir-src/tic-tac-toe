from dataclasses import dataclass

class Game():
    def __init__(self):
        self.display_menu()
    def start_game(self):
        players = ['1','2']
        pos = {
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
        who_won = -1
        f_play_cnt = 0 
        s_play_cnt = 0
        while True:
            self.display_board(pos)
            if turn == 1:
                f_play_cnt += 1 
                choice = input("It's time for player 1 to make a move (1-9): ")
                if pos[choice][1] == 'free': 
                    pos[choice][0] = 'O'
                    pos[choice][1] = 'busy'
                else:
                    continue
            else:
                s_play_cnt += 1
                choice = input("It's time for player 2 to make a move (1-9): ")
                if pos[choice][1] == 'free': 
                    pos[choice][0] = 'X'
                    pos[choice][1] = 'busy'
                else:
                    continue

            if (pos['1'][0] == pos['2'][0]) and (pos['2'][0] == pos['3'][0]): 
                win = True 
                if turn == 1:
                    who_won = 1
                else:
                    who_won = 2
            if (pos['4'][0] == pos['5'][0]) and (pos['5'][0] == pos['6'][0]): 
                win = True 
                if turn == 1:
                    who_won = 1
                else:
                    who_won = 2
            if (pos['7'][0] == pos['8'][0]) and (pos['8'][0] == pos['9'][0]): 
                win = True 
                if turn == 1:
                    who_won = 1
                else:
                    who_won = 2
            if (pos['1'][0] == pos['5'][0]) and (pos['5'][0] == pos['9'][0]): 
                win = True 
                if turn == 1:
                    who_won = 1
                else:
                    who_won = 2
            if (pos['3'][0] == pos['5'][0]) and (pos['5'][0] == pos['7'][0]): 
                win = True 
                if turn == 1:
                    who_won = 1
                else:
                    who_won = 2
            if (pos['1'][0] == pos['4'][0]) and (pos['4'][0] == pos['7'][0]): 
                win = True 
                if turn == 1:
                    who_won = 1
                else:
                    who_won = 2
            if (pos['2'][0] == pos['5'][0]) and (pos['5'][0] == pos['8'][0]): 
                win = True 
                if turn == 1:
                    who_won = 1
                else:
                    who_won = 2
            if (pos['3'][0] == pos['6'][0]) and (pos['6'][0] == pos['9'][0]): 
                win = True 
                if turn == 1:
                    who_won = 1
                else:
                    who_won = 2
            
            if turn == 1:
                turn = 2
            else:
                turn = 1

            if win and who_won == 1:
                print("Player 1 has won!")
                break
            elif win and who_won == 2:
                print("Player 2 has won!")
                break
            elif not win and (s_play_cnt + f_play_cnt >= 9): 
                print("No one has won!")
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
  