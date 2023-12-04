
from django.shortcuts import render
from . import tictactoeGame
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def optimalMove(request):
    '''
    Response next player optimal action and board received
    Gets in the request a "board":[]
    return {"NextPlayer": nextPlayer, "optimalAction": optimalAction, "board": board}
    '''
    if request.method == "POST":
        message = "post request"
        board = request.data['board']
        optimalAction = tictactoeGame.minimax(board)
        nextPlayer = tictactoeGame.player(board)
        newBoard = board.copy()
        if optimalAction is not None:
            newBoard = tictactoeGame.result(board, optimalAction)
        winner = tictactoeGame.winner(newBoard)
        terminalBoard = tictactoeGame.terminal(newBoard)
        print({"Next player": nextPlayer, "Optimal action": optimalAction, "Board": board,"terminalBoard": terminalBoard, "winner": winner})
        return Response({"NextPlayer": nextPlayer, "optimalAction": optimalAction, "board": board, "terminalBoard": terminalBoard, "winner": winner})



