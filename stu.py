import math
import itertools

# defining gridworld():
g_space = [
    [0, 0, 0, 1],
    [0, 0, 0, -1],
    [0, 0, 0, 0]]
noise = .2
gamma = .9
action_list = {"U" : (-1, 0), "D" : (1, 0), "R" : (0, 1), "L" : (0, -1)}


# checking if the state is terminal state
def terminal_state(state):
    (i, j) = state
    if i == 0 and j == 3:
        return True
    elif i == 1 and j == 3:
        return True
    return False


# value_space = [[0 for i in range(4)] for j in range(3)]   #the main value space
value_space = [
    [0, 0, 0, 1],
    [0, 0, 0, -1],
    [0, 0, 0, 0]]

# val = sum of (possibility * [reward for state + gamma*reward for next state])
main_p = 1 - noise   # setting the probability
noise_p = noise / 2  # setting the probability
row, col = 3, 4

def next_state(state, action):   #To get the next state for a particular action
    (i, j) = state
    next_i = i + action_list[action][0]
    next_j = j + action_list[action][1]
    if next_i < 0 or next_i >= row or next_j < 0 or next_j >= col :
        next_i, next_j = i, j
    return next_i, next_j


def value(state):
    (i, j) = state
    return value_space[i][j]


def possible_future_states(state):
    """
    Returns a set of possible future states from current state
    """
    i, j = state
    possible_states = {(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i, j)}
    if i==0:
        possible_states.remove((i-1, j))
    if i==3-1:
        possible_states.remove((i+1, j))
    if j==0:
        possible_states.remove((i, j-1))
    if j==4-1:
        possible_states.remove((i, j+1))

    tmp_states = possible_states.copy()
    for x, y in tmp_states:
        if (x, y) == (1, 1):
            possible_states.remove((x, y))

    return possible_states


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
            p[state] += p[s]
            p[s] = 0
    return p


def get_value(action, state):
    """
    Returns the value of a state
    """
    val = 0
    p = transition_probability(state, action)
    for s in p:
        if(p[s]):
            val += p[s] * gamma * value_space[s[0]][s[1]]
    return val

best_actions = [['U']*4 for i in range(3)]

for i in range(10):

    for iters in range(50):
        for i in range(3):
            for j in range(4):
                state = (i, j)
                if terminal_state(state) or state == (1, 1):
                    pass
                else:
                    state_v = get_value(best_actions[i][j], (i, j))
                    value_space[i][j] = state_v

    for i in range(3):
        for j in range(4):
            state = (i, j)
            if terminal_state(state) or state == (1, 1):
                pass
            else:
                action = None
                max_val = -float('inf')
                for a in action_list:
                    state_v = get_value(a, (i, j))
                    if state_v > max_val:
                        max_val = state_v
                        action = a
                best_actions[i][j] = action


final_data = {}    #combining value and action

for (i, j) in itertools.product(range(3), range(4)):
    final_data[i,j] = [value_space[i][j], best_actions[i][j]]

print(f"The final value and actions for particular cell: {final_data}")


#-----------------------visualizing the data-------------------------------


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


data = np.array(value_space)
text = np.array(best_actions)
  
# combining text with values
formatted_text = (np.asarray(["{0}\n{1:.2f}".format(
    text, data) for text, data in zip(text.flatten(), data.flatten())])).reshape(3, 4)
 
# drawing heatmap
fig, ax = plt.subplots()
colormap = sns.color_palette("Purples") 
ax = sns.heatmap(data, annot=formatted_text, fmt="", cmap=colormap)

plt.show()