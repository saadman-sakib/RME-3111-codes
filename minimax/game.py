from minimax import AI
import random

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1 if random.randint(0,1) == 0 else self.player2
    
    def game_move(self, row, col):
        if self.board[row][col] == None:
            self.board[row][col] = self.current_player
            self.current_player = self.player2 if self.current_player is self.player1 else self.player1
        else:
            print("Invalid Move")
    
    def print_board(self):
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print()
    
    def is_winner(self, player):
        state = self.board
        won = False
        won = ((state[0][0]==state[1][1]==state[2][2]==player) or won)
        won = ((state[0][2]==state[1][1]==state[2][0]==player) or won)
        for i in range(3):
            won = ((state[i][0]==state[i][1]==state[i][2]==player) or won)
            won = ((state[0][i]==state[1][i]==state[2][i]==player) or won)
        return won
    
    def is_game_over(self):
        state = self.board
        yes = False
        yes = ((None not in state[0]) and \
               (None not in state[1]) and \
               (None not in state[2])) or \
                yes
        yes = self.is_winner(self.player1) or \
              self.is_winner(self.player2) or \
              yes 
        return yes

