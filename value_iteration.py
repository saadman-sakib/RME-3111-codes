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
    i, j = state
    possible_states = {(i-1, j), (i+1, j), (i, j-1), (i, j+1)}
    if i==0:
        possible_states.remove((i-1, j))
    if i==N-1:
        possible_states.remove((i+1, j))
    if j==0:
        possible_states.remove((i, j-1))
    if j==M-1:
        possible_states.remove((i, j+1))

    tmp_states = possible_states.copy()
    for i, j in tmp_states:
        if GRID[i][j] == None:
            possible_states.remove((i, j))

    return possible_states


def normalize(p):
    s = sum(p.values())
    for k in p:
        p[k] /= s
    return p


def transition_probability(state, action):
        # 20% noise
        i, j = state
        if action == 'U':
            p =  {(i-1, j): 0.8, (i, j+1): 0.1, (i, j-1): 0.1}
        elif action == 'D':
            p =  {(i+1, j): 0.8, (i, j+1): 0.1, (i, j-1): 0.1}
        elif action == 'L':
            p =  {(i, j-1): 0.8, (i-1, j): 0.1, (i+1, j): 0.1}
        elif action == 'R':
            p =  {(i, j+1): 0.8, (i-1, j): 0.1, (i+1, j): 0.1}

        pfs = possible_future_states(state)
        for s in p:
            if s not in pfs:
                p[s] = 0
        p = normalize(p)
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


if __name__ == '__main__':
    import pprint
    import matplotlib.pyplot as plt
    import numpy as np

    delta = float('inf')
    while abs(delta) > .0000001:
        delta = 0
        for s in STATES:
            new_val = value_update(s)
            delta = max( delta,  abs(new_val - GRID[s[0]][s[1]]) )
            GRID[s[0]][s[1]] = new_val
    pprint.pprint(GRID)
    a = np.asarray(GRID, dtype=np.float32)

    fig, ax = plt.subplots()
    im = ax.imshow(a, cmap = 'RdYlGn', interpolation = 'nearest')

    for i in range(N):
        for j in range(M):
            if GRID[i][j] != None:
                txt_display = "%.2f" % GRID[i][j]
            else:
                txt_display = " "
            text = ax.text(j, i, txt_display,
                        ha="center", va="center", color="black")
    plt.show()