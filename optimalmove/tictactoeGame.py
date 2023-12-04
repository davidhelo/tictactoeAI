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
    countX = sum(x.count(X) for x in board)
    countO = sum(o.count(O) for o in board)
    return X if countX <= countO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possibleActions.add((i, j))

    return possibleActions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultBoard = copy.deepcopy(board)
    if action not in actions(board):
        raise Exception("Invalid action")
    resultBoard[action[0]][action[1]] = player(board)
    return resultBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    waysToWin = [
        # sets to win horizontally
        {(0,0),(0,1),(0,2)},
        {(1,0),(1,1),(1,2)},
        {(2,0),(2,1),(2,2)},
        # sets to win vertically
        {(0,0),(1,0),(2,0)},
        {(0,1),(1,1),(2,1)},
        {(0,2),(1,2),(2,2)},
        # set to win diagonally
        {(0,0),(1,1),(2,2)},
        {(0,2),(1,1),(2,0)}
    ]

    def getPositions(player):
        cells = set()
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == player:
                    cells.add((i, j))
        return cells
    
    Xcells = getPositions(X)
    Ocells = getPositions(O)

    for win in waysToWin:
        if win.issubset(Xcells):
            return X
        if win.issubset(Ocells):
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    countEmpty = sum(e.count(EMPTY) for e in board)
    if winner(board) is not None or countEmpty == 0:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # assuming terminal(board) == True when utility() is called
    currentWinner = winner(board)
    if currentWinner == X:
        return 1
    
    if currentWinner == O:
        return -1
    
    if currentWinner == None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    def getScore(depth, utilityValue):
        '''
        calculate score with depth compensation to pick faster win
        '''
        score = 0
        if utilityValue == 1:
            score = utilityValue * (10 - depth)
        elif utilityValue == -1:
            score = utilityValue * (10 - depth) 
        return score

    def maxValue(board, depth):
        if terminal(board):
            ut = utility(board)
            return getScore(depth, ut)
        v = float('-inf')
        for action in actions(board):
            v = max(v, minValue(result(board, action), depth+1))
        return v
    
    def minValue(board, depth):
        if terminal(board):
            ut = utility(board)
            return getScore(depth, ut)
        v = float('inf')
        for action in actions(board):
            v = min(v, maxValue(result(board, action), depth+1))
        return v

    currentPlayer = player(board)
    alphaValue = float('-inf')
    betaValue = float('inf')

    # if maximizing player
    if currentPlayer == X:
        optimalValue = float('-inf')
        optimalAction = None
        for action in actions(board):
            actionValue = minValue(result(board, action), 1)
            if optimalValue <= actionValue:
                optimalAction = action
            optimalValue = max(optimalValue, actionValue)
            alphaValue = max(alphaValue, optimalValue)
            if betaValue <= alphaValue:
                break
        return optimalAction
    
    # if minimizing player
    if currentPlayer == O:
        optimalValue = float('inf')
        optimalAction = None
        for action in actions(board):
            actionValue = maxValue(result(board, action), 1)
            if optimalValue > actionValue:
                optimalAction = action
            optimalValue = min(optimalValue, actionValue)
            betaValue = min(betaValue, optimalValue)
            if betaValue <= alphaValue:
                break
        return optimalAction
    