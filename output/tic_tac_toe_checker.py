"""Kata - Tic-Tac-Toe Checker

completed at: 2019-04-26 19:46:40
by: Jakub Červinka

If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is `0` if a spot is empty, `1` if it is an "X", or `2` if it is an "O", like so:

```
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
```

We want our function to return:

* `-1` if the board is not yet finished AND no one has won yet (there are empty spots),
* `1` if "X" won,
* `2` if "O" won,
* `0` if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""

import numpy as np

def check_win(player, board):       
    rows = [all(board[r,:] == player) for r in range(3)]
    cols = [all(board[:, c] == player) for c in range(3)]        
    diags = [all(np.diag(board) == player),
             all(np.diag(np.fliplr(board) == player))]
                 
    return any(rows + cols + diags)

def isSolved(board):
    board = np.array(board)
    
    if check_win(1, board): return 1
    if check_win(2, board): return 2
    return 0 if not(0 in board) else -1

