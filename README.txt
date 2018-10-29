For this project, I implemented an AI solver for Connect-3, which is a variant of Connect-4 on a 4x5 board, using the Mini-Max function to calculate the maximum utility recursively at each state. The program takes a state as a .txt file input and outputs the optimal move for the player-to-move at the given state with the expected utility for player X (ie. 1 if X wins, 0 if two players draw, and -1 if player O wins). If there are multiple moves with the same utility, it will output the first one. 
Example input: 

O.O..
OXOX.
XOXOX
XOXOX

Example output: 
1 X4
(which means: it's player X's turn, its best move is column 4 (right-most column), and the expected utility is 1 or player X is expected to win)
Note:
- Rows and columns are 0-indexed. 
- The larger the number of empty spaces, the longer it takes for the program to run because of its recursive nature. 
