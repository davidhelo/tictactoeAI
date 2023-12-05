
from django.shortcuts import render
from . import tictactoeGame
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def optimalMove(request):
    '''
    Response next player optimal action and board received
    Gets in the request a "board":[]
    return {"NextPlayer": nextPlayer, "optimalAction": optimalAction, "board": board}
    if board is empty, it returns a random cell to add variation to start and save time
    '''
    if request.method == "POST":
        message = "post request"
        board = request.data['board']
        if len(tictactoeGame.actions(board)) == 9:
            optimalAction = (random.randint(0, 2), random.randint(0, 2))
        else:
            optimalAction = tictactoeGame.minimax(board)
        nextPlayer = tictactoeGame.player(board)
        newBoard = board.copy()
        if optimalAction is not None:
            newBoard = tictactoeGame.result(board, optimalAction)
        winner = tictactoeGame.winner(newBoard)
        terminalBoard = tictactoeGame.terminal(newBoard)
        print({"Next player": nextPlayer, "Optimal action": optimalAction, "Board": board,"terminalBoard": terminalBoard, "winner": winner})
        return Response({"NextPlayer": nextPlayer, "optimalAction": optimalAction, "board": board, "terminalBoard": terminalBoard, "winner": winner})



