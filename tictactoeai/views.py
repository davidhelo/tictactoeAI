from django.shortcuts import redirect
from tictactoegame.views import tictactoeGameView


def index(request):
    return redirect(tictactoeGameView)