# Tic Tac Toe AI
 ## Description
 This app is an implementation in Python of Adversarial Search, Minimax algorithm to play tic tac toe game.
 The minimax function is in the [tictactoeGame.py](https://github.com/davidhelo/tictactoeAI/blob/main/optimalmove/tictactoeGame.py) file.
 Find more information about Adversarial Search and Minimax algorithms in this lecture from Harvard course cs50ai [here](https://cs50.harvard.edu/ai/2023/notes/0/#adversarial-search)
 or [here](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/).

 ## Web App
 The web app was developed in React JS and Python Django Framework. It was pre-build to be served as a static HTML file and then injects the javascript to the index template.
 You'll find the source code for the web app in a different repository, [here](https://github.com/davidhelo/TictactoeAIWebApp).

 ### Optimal move API
 This API get a POST request to "/optimalmove/" with a "board" parameter in its body with information about the board.
 It return a JSON object:
 '''
 {
    'Next player': 'O', 
    'Optimal action': (2, 1), 
    'Board': [['O', 'X', None], ['X', 'X', 'O'], [None, None, None]], 
    'terminalBoard': False, 
    'winner': None
 }
 '''
Where: 
    - "board" is the board received,
    - "terminal board" return true if there is a winner or the board if full,
    - "winner" return O X or None (meaning if terminal is True and winner None the game is a tie),
    - "optimal action" is the calculated next optimal action.
    - "next player" is the next player in the received board.

 