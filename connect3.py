import operator
import copy
import sys


current_state = []


# Read the current state
def initial_state(current):
    file = open(sys.argv[1], 'r')
    tiles = file.read().split()
    #print(tiles)
    for i in range(4):
        row = []
        index = 0
        for j in range(5):
            row.append(tiles[i][index])
            index += 1
        current.append(row)
    return current

initial_state(current_state)
# print(current_state)


# Decide which player to make the next move
def player_move(state):
    count_x = 0
    count_o = 0
    for row in state:
        for tile in row:
            if tile == 'X':
                count_x += 1
            elif tile == 'O':
                count_o += 1
    if count_x == count_o:
        return 1
    else:
        return 2

# print(player_move(current_state))


# Define the set of legal moves by checking which column is not full yet
def legal_moves(state):
    valid_col = []
    for index in range(5):
        if state[0][index] == '.':
            valid_col.append(index)
    return valid_col

# print(legal_moves(current_state))


# Result after the next player chooses a column and moves
def result(state, col):
    state_copy = copy.deepcopy(state)
    next_move = ''
    if player_move(state) == 1:
        next_move = 'X'
    else:
        next_move = 'O'
    for row in state_copy[::-1]:
        if row[col] != '.':
            continue
        else:
            row[col] = next_move
            break
    return state_copy


# Check if position (x,y) is the start a vertical connected-3
def vertical_check(state,x,y):
    if x > 1:
        return False
    check_value = state[x][y]
    if check_value == '.':
        return False
    if state[x+1][y] != check_value:
        return False
    else:
        if state[x+2][y] != check_value:
            return False
        else:
            return check_value

# print(vertical_check(current_state,2,0))


# Check if position (x,y) is the start a horizontal connected-3
def horizontal_check(state,x,y):
    if y > 2:
        return False
    check_value = state[x][y]
    if check_value == '.':
        return False
    if state[x][y+1] != check_value:
        return False
    else:
        if state[x][y+2] != check_value:
            return False
        else:
            return check_value

# print(horizontal_check(current_state,3,1))


# Check if position (x,y) is the start a diagonal connected-3 with positive slope
def diagonal_check_up(state,x,y):
    if x < 2 or y > 2:
        return False
    check_value = state[x][y]
    if check_value == '.':
        return False
    if state[x-1][y+1] != check_value:
        return False
    else:
        if state[x-2][y+2] != check_value:
            return False
        else:
            return check_value

# print(diagonal_check_up(current_state,3,1))


# Check if position (x,y) is the start a diagonal connected-3 with negative slope
def diagonal_check_down(state,x,y):
    if x > 1 or y > 2:
        return False
    check_value = state[x][y]
    if check_value == '.':
        return False
    if state[x+1][y+1] != check_value:
        return False
    else:
        if state[x+2][y+2] != check_value:
            return False
        else:
            return check_value


# Test if one of the two players has won and indicate who won
def terminal_test(state):
    winner = ''
    for index_row in range(4):
        for index_col in range(5):
            if vertical_check(state, index_row, index_col):
                winner = vertical_check(state, index_row, index_col)
                break
            if horizontal_check(state,index_row, index_col):
                winner = horizontal_check(state, index_row, index_col)
                break
            if diagonal_check_up(state, index_row, index_col):
                winner = diagonal_check_up(state, index_row, index_col)
                break
            if diagonal_check_down(state, index_row, index_col):
                winner = diagonal_check_down(state, index_row, index_col)
                break
    if winner == '':
        result = 0
        for row in state:
            for tile in row:
                if tile == '.':
                    result = -2
                    break
        if result == 0:
            return -10
        else:
            return False
    else:
        if winner == 'X':
            return 1
        if winner == 'O':
            return -1

# print(terminal_test(current_state))


def max_value(state):
    if terminal_test(state):
        if terminal_test(state) == -10:
            return 0
        else:
            return terminal_test(state)
    value = -9999
    successors = []
    valid_moves = legal_moves(state)
    for col_move in valid_moves:
        successors.append(result(state, col_move))
    for state in successors:
        value = max(value, min_value(state))
    return value


# print(max_value(current_state))
def min_value(state):
    if terminal_test(state):
        if terminal_test(state) == -10:
            return 0
        else:
            return terminal_test(state)
    value = 9999
    successors = []
    valid_moves = legal_moves(state)
    for col_move in valid_moves:
        successors.append(result(state, col_move))
    for state in successors:
        value = min(value, max_value(state))
    return value


# Calculate mini-max of state A to determine the maximum strategy for the respective player
def minimax_utility(state):
    if terminal_test(state):
        utility = terminal_test(state)
        return utility
    next_player = player_move(state)
    if next_player == 1:
        player_letter = 'X'
    else:
        player_letter = 'O'
    valid_moves = legal_moves(state)
    best_move = -1
    best_utility = -10
    if next_player == 1:
        actions = {}
        for move in valid_moves:
            # print(result(state,move))
            actions[move] = min_value(result(state, move))
        best_move = max(actions.items(), key=operator.itemgetter(1))[0]
        best_utility = actions[best_move]
    if next_player == 2:
        actions = {}
        for move in valid_moves:
            actions[move] = max_value(result(state, move))
        best_move = min(actions.items(), key=operator.itemgetter(1))[0]
        best_utility = actions[best_move]
    return player_letter, best_move, best_utility


player, move, utility = minimax_utility(current_state)
print("%d %s%d" % (utility, player, move))