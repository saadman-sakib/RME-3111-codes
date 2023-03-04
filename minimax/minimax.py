import math
import copy


class AI:
    def __init__(self, player):
        self.player = player
        self.opponent = 'O' if player == 'X' else 'X'

    def is_winner(self, state, player):
        won = False
        won = ((state[0][0] == state[1][1] == state[2][2] == player) or won)
        won = ((state[0][2] == state[1][1] == state[2][0] == player) or won)
        for i in range(3):
            won = ((state[i][0] == state[i][1] ==
                   state[i][2] == player) or won)
            won = ((state[0][i] == state[1][i] ==
                   state[2][i] == player) or won)
        return won

    def is_terminal(self, state):
        yes = False
        yes = ((None not in state[0]) and
               (None not in state[1]) and
               (None not in state[2])) or \
            yes
        yes = self.is_winner(state, self.player) or \
            self.is_winner(state, self.opponent) or \
            yes
        return yes

    def terminal_value(self, state):
        if (self.is_winner(state, self.player)):
            return 1
        elif (self.is_winner(state, self.opponent)):
            return -1
        else:
            return 0

    def get_board_after_move(self, state, move, player):
        new_state = copy.deepcopy(state)
        i, j = move[0], move[1]
        new_state[i][j] = player
        return new_state

    def allowable_moves(self, state):
        moves = []
        for i in range(3):
            for j in range(3):
                if (state[i][j] == None):
                    moves.append((i, j))
        return moves

    def min_value_state(self, state, alpha, beta):
        if (self.is_terminal(state)):
            return {"value": self.terminal_value(state), "move": None}
        optimal_value = math.inf
        optimal_move = None
        for move in self.allowable_moves(state):
            move_state = self.get_board_after_move(state, move, self.opponent)
            value = self.max_value_state(move_state, alpha, beta)["value"]
            if (value <= optimal_value):
                optimal_move = move
                optimal_value = value
                beta = min(beta, value)
            if value < alpha:
                break
            

        return {"value": optimal_value, "move": optimal_move}

    def max_value_state(self, state, alpha, beta):
        if (self.is_terminal(state)):
            return {"value": self.terminal_value(state), "move": None}
        optimal_value = -math.inf
        optimal_move = None
        for move in self.allowable_moves(state):
            move_state = self.get_board_after_move(state, move, self.player)
            value = self.min_value_state(move_state, alpha, beta)["value"]
            if (value >= optimal_value):
                optimal_move = move
                optimal_value = value
                alpha = max(value, alpha)
            if value > beta:
                break

        return {"value": optimal_value, "move": optimal_move}

    def make_move(self, board):
        return self.max_value_state(board, -math.inf, math.inf)["move"]
