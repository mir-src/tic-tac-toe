from typing import Optional, List

# Constants
PLAYER_X  = "X"
PLAYER_O = "O" 
WINNING_COMBINATIONS = [
    (0,1,2), (3,4,5), (6,7,8), # rows
    (0,3,6), (1,4,7), (2,5,8), # columns
    (0,4,8), (2,4,6)           # diagonals
]

class TicTacToe():
    def __init__(self):
        self.board: List[str] = [str(i) for i in range(1,10)]
        self.current_player: str = PLAYER_X
        self.winner: Optional[str] = None 
        self.moves_count: int = 0

    def display_board(self) -> None:
        print("\n")
        for i in range(0,9,3):
            row = self.board[i:i+3]
            print(" " + " | ".join(row))
            if i < 6:
                print("---+---+---")
        print("\n")

    def get_player_move(self) -> int:
        while True:
            try:
                move = int(input(f"Player {self.current_player}, choose a cell (1-9): "))

                if move < 1 or move > 9:
                    print("Please enter anumber between 1 and 9.")
                    continue
                index = move - 1
                if self.board[index] in (PLAYER_O,PLAYER_X):
                    print("That cell is already take. Choose another one.")
                    continue
                return index
            except ValueError: 
                print("Invalid input. Please enter a number.")

    def make_move(self, index: int) -> None:
        self.board[index] = self.current_player
        self.moves_count += 1

    def check_winner(self) -> Optional[str]:
        for a,b,c in WINNING_COMBINATIONS:
            if self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]

        if self.moves_count == 9:
            return "Draw" 

        return None

    def switch_player(self) -> None:
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X

    def play(self) -> None:
        print("Welcome to my Tic-Tac-Toe game!")
        while self.winner is None: 
            self.display_board()
            move_index = self.get_player_move()
            self.make_move(move_index)
            self.winner = self.check_winner()
            if self.winner is None:
                self.switch_player()

        self.display_board()
        if self.winner == 'Draw':
            print("It's a draw!")
        else:
            print(f"Player {self.winner} wins! Congratulations!")

def display_menu() -> None:
    while True:
        print("\n--- MENU ---")
        print("1. Start Game")
        print("2. Quit")
        choice = input("Select option: ")
        if choice == '1':
            game = TicTacToe()
            game.play()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    display_menu()






                








  