"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    """
    count number of X's and O's on the board
    if the number of X's and O's are equal, X goes, otherwise O goes
    x goes first count is equal 
    """

    x_count = 0
    o_count = 0

    for row in board:
        for n in row:
            if n == X:
                x_count += 1
                continue
            if n == O:
                o_count += 1

    if x_count == o_count:
        return X
    else:    
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    # check all squares, if currently empty, its a posible action
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value is EMPTY:
              possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # check if action if valid
    i, j = action
    if board[i][j] == EMPTY:
        # if valid update deep copy of board and return a deep copy
        board_copy = copy.deepcopy(board)
        current_player = player(board)
        board_copy[i][j] = current_player
        return board_copy

    # otherwise raise an exception
    raise RuntimeError('Not valid action')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check for three in a row starting from specific to cover all possible winning situations 
    # without checking every square

    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # check diaginals 
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check if there is a winner
    if winner(board) is None:
        return False

    # check for any available actions
    if actions(board):
        return False
    
    return True




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # call winner to determine if there is a winner and who it is 
    is_winner = winner(board)

    if is_winner is X:
        return 1
    if is_winner is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # check if board is terminal
    if terminal(board):
        return None
    
    # get current player (X or O)
    current_player = player(board)

    # get list of possible actions
    possible_actions = actions(board)

    # check if one of the possible actions is a winner
    for action in possible_actions:

        # create board with action and analize
        test_board = result(board,action)

        # check if action wins for current player
        if winner(test_board) is current_player:
            return action
        
        # check if action wins for other player
        if winner(test_board) is not None:
            return action
        
    return action
