GRID = [
    [0, 0, 0, 1.0],
    [0, None, 0, -1.0],
    [0, 0, 0, 0]
]

STATES = set()
TERMINAL_STATES = {(0, 3), (1, 3)}
Q = {}

N, M = len(GRID), len(GRID[0])

GAMMA = 0.9
ALPHA = .5
NOISE = .5
THRESHOLD = .00001


def is_terminal(state):
    if state in  TERMINAL_STATES:
        return True
    return False


def actions(state):
    possible_actions = {'U', 'D', 'L', 'R'}
    return possible_actions

def initialize():
    for i in range(N):
        for j in range(M):
            if (GRID[i][j]!=None) and ((i, j) not in TERMINAL_STATES):
                STATES.add((i, j))
            
            if (GRID[i][j]!=None):
                for a in actions((i, j)):
                    Q[((i, j), a)] = GRID[i][j]


def possible_future_states(state):
    i, j = state
    possible_states = {(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i, j)}
    # removing states with obstacles
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
            p[state] +=   p[s]
            p[s] = 0
    return p

    
def reward(state):
    i, j = state
    if (i, j) in TERMINAL_STATES:
        return GRID[i][j]
    else:
        return 0


def expected_future_Q(state, action):
    if is_terminal(state):
        return reward(state)
    p = transition_probability(state, action)
    exp_reward = 0
    for s in p:
        if p[s]:
            exp_reward += p[s]*max(Q[(s, a)] for a in actions(s))
    return exp_reward


def q_update(state, action):
    exp_q_val = expected_future_Q(state, action)
    new_val = Q[(state, action)] + ALPHA * (reward(state) + GAMMA*exp_q_val - Q[(state, action)])
    return new_val


def policy_extraction(state):
    value = -float('inf')
    action = None
    for a in actions(state):
        q_val = Q[(state, a)]
        if q_val > value:
            value = q_val
            action = a
    GRID[state[0]][state[1]] = value
    return action


if __name__ == '__main__':
    import pprint
    import matplotlib.pyplot as plt
    import numpy as np

    initialize()

    delta = float('inf')
    while abs(delta) > THRESHOLD:
        delta = 0
        for s in STATES:
            for a in actions(s):
                new_val = q_update(s, a)
                delta = max( delta,  abs(new_val - Q[(s, a)]) )
                Q[(s, a)] = new_val

    pprint.pprint(Q)

    policies = {}
    for s in STATES:
        policy = policy_extraction(s)
        policies[s] = policy

    a = np.asarray(GRID, dtype=np.float32)
    fig, ax = plt.subplots()
    im = ax.imshow(a, cmap = 'RdYlGn', interpolation = 'nearest')

    for i in range(N):
        for j in range(M):
            if GRID[i][j] != None and (i, j) not in TERMINAL_STATES:
                txt_display = "%.2f" % Q[((i, j), policies[(i, j)])] + "\n" + policies[(i, j)]
            elif (i, j) in TERMINAL_STATES:
                txt_display = "%.2f" % GRID[i][j]
            else:
                txt_display = " "
            text = ax.text(j, i, txt_display,
                        ha="center", va="center", color="black")
    plt.show()


