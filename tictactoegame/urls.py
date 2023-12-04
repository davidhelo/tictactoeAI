from django.contrib import admin
from django.urls import path
from .views import tictactoeGameView


urlpatterns = [
    path('', tictactoeGameView.as_view())
]