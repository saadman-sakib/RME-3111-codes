import math

class ExpMax:
    def __init__(self):
        self.graph = {
            "A": {"B", "C", "D"},
            "B": {"E", "F"},
            "C": {"G", "H"},
            "D": {"I", "J"},
        }

        self.terminal = {
            "E": 3,
            "F": 12,
            "G": 8,
            "H": 2,
            "I": 4,
            "J": 6,
        }

        self.prob = {
            "E": .5,
            "F": .5,
            "G": .5,
            "H": .5,
            "I": .5,
            "J": .5,
        }

    def is_terminal(self, state):
        return state in self.terminal

    def terminal_value(self, state):
        return self.terminal[state]

    def next_states(self, state):
        return self.graph[state]

    def p(self, state):
        return self.prob[state]
    
    def exp_value_state(self, state):
        if (self.is_terminal(state)):
            return self.terminal_value(state)
        optimal_value = 0
        for move in self.next_states(state):
            optimal_value += self.p(move)*self.max_value_state(move)

        return optimal_value
    
    def max_value_state(self, state):
        if (self.is_terminal(state)):
            return self.terminal_value(state)
        optimal_value = -math.inf
        for move in self.next_states(state):
            value = self.exp_value_state(move)
            if (value >= optimal_value): optimal_value = value

        return optimal_value


ai = ExpMax()

print(ai.max_value_state("A"))