from django.shortcuts import redirect
from tictactoegame.views import tictactoeGameView
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from index main")