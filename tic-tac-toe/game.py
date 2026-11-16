import random


class TicTacToe :
    def __init__(self , difficulty):
        self.board = [" "] * 10
        self.player_turn = "X"
        self.ai = "O"
        self.human = "X"
        self.difficulty = difficulty

    
    def show_board(self) :
        print('\n')
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3] )
        print('------')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('------')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9] )
        print('\n')
    

    def swap_player_turn(self) :
         self.player_turn = self.ai if self.player_turn == self.human else self.human
    
    def is_board_filled(self) :
        return all(self.board[i] in ['X', 'O'] for i in range(1, 10))


    def fix_spot(self , cell , player) :
        self.board[cell] = player

    def has_player_won(self , player) :
        win_combinations = [
            [1,2,3] , [4,5,6] , [7,8,9] ,
            [1,4,7] , [2,5,8] , [3,6,9] ,
            [1,5,9] , [3,5,7]
        ]

        for combination in win_combinations :
            if  all(self.board[cell] == player for cell in combination) :
             return True
        return False
    
    def get_player_input(self):
        while True:
            try:
                cell = int(input("Enter a cell number (1-9): ")) 
                if cell not in range(1,10):
                    print("Invalid number. Choose 1-9.")
                elif self.board[cell] in ["X", "O"]:
                    print("Cell already taken.")
                else:
                    return cell
            except ValueError:
                print("Invalid input. Enter a number 1-9.")

    
    def minimax(self, is_maximizing):
        if self.has_player_won(self.ai):
            return 1
        elif self.has_player_won(self.human):
            return -1
        elif self.is_board_filled():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(1,10):
                if self.board[i] == " ":
                    self.board[i] = self.ai
                    score = self.minimax(False)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(1,10):
                if self.board[i] == " ":
                    self.board[i] = self.human
                    score = self.minimax(True)
                    self.board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def best_move(self ):
        best_score = -float('inf')
        move = None
        for i in range(1,10):
            if self.board[i] == " ":
                self.board[i] = self.ai
                score = self.minimax(False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        return move
    
    def ai_move(self) :
        if self.difficulty == "Easy" :
            available = [ i for i in range(1 ,10) if self.board[i] == " "]
            return random.choice(available)
        elif self.difficulty == "Medium" :
            if random.random() < 0.5 :
                available = [ i for i in range(1 ,10) if self.board[i] == " "]
                return random.choice(available)
            else :
                return self.best_move()
        else :
            return self.best_move()


    

    
    def start(self) :
        print("Welcome to TicTacToe! You are X, AI is O.")
        while True :
            self.show_board()
            if self.player_turn == self.human :
                cell = self.get_player_input()
            else :
                cell = self.ai_move()
                print(f"AI chooses cell {cell}")
            self.fix_spot(cell , self.player_turn)
            if self.has_player_won(self.player_turn):
                print(f"Player {self.player_turn} Won!")
                break
            elif self.is_board_filled() :
                    print("Draw")
                    break
            self.swap_player_turn()

if __name__ == "__main__" :
    while True :
      level = input("Enter a Level(Difficult  Medium - Easy)")
      if level in ["Difficult" , "Medium" ,"Easy"] :
         break
      else : 
          print("INVALID! Enter (Difficult  Medium - Easy)")
     
     
     
    game = TicTacToe(level)
    game.start()