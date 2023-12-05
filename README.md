# Tic Tac Toe AI
 ## Description
 ### Adversarial Search: minimax algorithm
 This app is an implementation in Python of an adversarial search algorithm, concretely, the minimax algorithm to play tic tac toe game.

 The minimax function is in the [tictactoeGame.py](https://github.com/davidhelo/tictactoeAI/blob/main/optimalmove/tictactoeGame.py) file. 

 This function consist in searching all possible paths up to the last outcome and assign each a score that is compare to other paths scores to maximize the possibility to win. 
 
 This is done with two functions `maxValue` that takes the maximum value returned by `minValue` which at the same time takes the minimum value returned from `maxValue` function.
 These two functions call each other recursively until there is a terminal board (which mean there is a winner or a tie), at that point a score is assign: 1 if maximizer wins, -1 if minimizer wins or 0 if it is a tie, weighted by the depth of the path. 

 Find more information about Adversarial Search and Minimax algorithms in this lecture from Harvard course cs50ai [here](https://cs50.harvard.edu/ai/2023/notes/0/#adversarial-search),
 or more information [here](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/).

 ## Web App
 The web app was developed in React JS and Python Django Framework. It was pre-build to be served as a static HTML file and then injects the javascript to the index template.
 You'll find the source code for the web app in a different repository, [here](https://github.com/davidhelo/TictactoeAIWebApp).

 ### Optimal move API
 This app consumes an API implemented in Django. The API receives a POST request to "/optimalmove/" with a "board" parameter in its body that represents the board in the format: 
 ```
 {
   "board": [
      [ cell, cell, cell ],
      [ cell, cell, cell ],
      [ cell, cell, cell ],
   ]
 }
 ```
 Where `cell` represents each the cells in the tictactoe board, and can have a value of 'X', 'O' or None.

 This API will use the minimax algorithm to calculate the optimal move and return it in JSON format:
 ```
 {
    'Next player': 'O', 
    'Optimal action': (2, 1), 
    'Board': [['O', 'X', None], ['X', 'X', 'O'], [None, None, None]], 
    'terminalBoard': False, 
    'winner': None
 }
 ```
Where: 
- `"board"` is the board received,
- `"terminal board"` return true if there is a winner or the board if full,
- `"winner"` return O X or None (meaning if terminal is True and winner None the game is a tie),
- `"optimal action"` is the calculated next optimal action,
- `"next player"` is the next player in the received board.

 