import math

class MiniMax:
    def __init__(self, player):
        pass

    def is_terminal(self, state):
        pass

    def terminal_value(self, state):
        pass

    def next_states(self, state):
        pass

    def min_value_state(self, state):
        if (self.is_terminal(state)):
            return self.terminal_value(state)
        optimal_value = math.inf
        for move in self.next_states(state):
            value = self.max_value_state(move)
            if (value <= optimal_value): optimal_value = value

        return optimal_value
    
    def max_value_state(self, state):
        if (self.is_terminal(state)):
            return self.terminal_value(state)
        optimal_value = -math.inf
        for move in self.next_states(state):
            value = self.min_value_state(move)
            if (value >= optimal_value): optimal_value = value

        return optimal_value


class AlphaBeta:
    def __init__(self, player):
        pass

    def is_terminal(self, state):
        pass

    def terminal_value(self, state):
        pass

    def next_states(self, state):
        pass

    def min_value_state(self, state, alpha, beta):
        if (self.is_terminal(state)):
            return {"value": self.terminal_value(state, alpha, beta), "move": None}
        optimal_value = math.inf
        for move in self.next_states(state):
            value = self.max_value_state(move)
            optimal_value = max(value, optimal_value)
            if value <= alpha: return optimal_value
            beta = min(beta, value)

        return optimal_value
    
    def max_value_state(self, state, alpha, beta):
        if (self.is_terminal(state)):
            return {"value": self.terminal_value(state, alpha, beta), "move": None}
        optimal_value = -math.inf
        for move in self.next_states(state):
            value = self.min_value_state(move)
            optimal_value = min(value, optimal_value)
            if value >= beta: return optimal_value
            alpha = max(alpha, value)

        return optimal_value