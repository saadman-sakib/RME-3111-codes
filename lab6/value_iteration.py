GRID = [
    [0, 0, 0, 1.0],
    [0, None, 0, -1.0],
    [0, 0, 0, 0]
]
GAMMA = 0.9
N, M = len(GRID), len(GRID[0])

STATES = set()
TERMINAL_STATES = {(0, 3), (1, 3)}

for i in range(N):
    for j in range(M):
        if (GRID[i][j]!=None) and ((i, j) not in TERMINAL_STATES):
            STATES.add((i, j))


def is_terminal(state):
    i, j = state
    if (i, j) in  TERMINAL_STATES:
        return True
    return False


def reward(state):
    i, j = state
    return GRID[i][j]


def actions(state):
    possible_actions = {'U', 'D', 'L', 'R'}
    return possible_actions


def possible_future_states(state):
    """
    Returns a set of possible future states from current state
    """
    i, j = state
    possible_states = {(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i, j)}
    if i==0:
        possible_states.remove((i-1, j))
    if i==N-1:
        possible_states.remove((i+1, j))
    if j==0:
        possible_states.remove((i, j-1))
    if j==M-1:
        possible_states.remove((i, j+1))

    tmp_states = possible_states.copy()
    for x, y in tmp_states:
        if GRID[x][y] == None:
            possible_states.remove((x, y))

    return possible_states


def normalize(p):
    s = sum(p.values())
    for k in p:
        p[k] /= s
    return p


def transition_probability(state, action):
    """
    Returns a dictionary of possible future states and their probabilities
    """
    PD = 0.8
    PN = .1
    i, j = state
    if action == 'U':
        p =  {(i-1, j): PD, (i, j+1): PN, (i, j-1): PN, (i, j): 0}
    elif action == 'D':
        p =  {(i+1, j): PD, (i, j+1): PN, (i, j-1): PN, (i, j): 0}
    elif action == 'L':
        p =  {(i, j-1): PD, (i-1, j): PN, (i+1, j): PN, (i, j): 0}
    elif action == 'R':
        p =  {(i, j+1): PD, (i-1, j): PN, (i+1, j): PN, (i, j): 0}

    pfs = possible_future_states(state)
    for s in p:
        if s not in pfs:
            tmp = p[s]
            p[s] = 0
            p[state] +=  tmp
    return p


def value_update(state):
    value = -float('inf')
    for a in actions(state):
        p = transition_probability(state, a)
        exp_val = 0
        for s in p:
            if p[s]:
                exp_val += p[s]*GRID[s[0]][s[1]]*GAMMA
        value = max(exp_val, value)
    
    return value

def policy_extraction(state):
    value = -float('inf')
    action = None
    for a in actions(state):
        p = transition_probability(state, a)
        exp_val = 0
        for s in p:
            if p[s]:
                exp_val += p[s]*GRID[s[0]][s[1]]*GAMMA
        
        if exp_val > value:
            value = exp_val
            action = a    
    return action


if __name__ == '__main__':
    import pprint
    import matplotlib.pyplot as plt
    import numpy as np

    delta = float('inf')
    while abs(delta) > .0000001:
    # for i in range(100):
        delta = 0
        for s in STATES:
            new_val = value_update(s)
            delta = max( delta,  abs(new_val - GRID[s[0]][s[1]]) )
            GRID[s[0]][s[1]] = new_val
    # pprint.pprint(GRID)
    a = np.asarray(GRID, dtype=np.float32)

    policies = {}
    for s in STATES:
        policy = policy_extraction(s)
        policies[s] = policy

    fig, ax = plt.subplots()
    im = ax.imshow(a, cmap = 'RdYlGn', interpolation = 'nearest')

    for i in range(N):
        for j in range(M):
            if GRID[i][j] != None and (i, j) not in TERMINAL_STATES:
                txt_display = "%.2f" % GRID[i][j] + "\n" + policies[(i, j)]
            elif (i, j) in TERMINAL_STATES:
                txt_display = "%.2f" % GRID[i][j]
            else:
                txt_display = " "
            text = ax.text(j, i, txt_display,
                        ha="center", va="center", color="black")
    plt.show()


