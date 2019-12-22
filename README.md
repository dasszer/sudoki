# SUDOKI
Sudoki is a python program that solves any sudoku problems. Simply give it the sudoku to solve and it will use a backtracking method to find the correct solved sudoku.

# How to use
Add the following board layout to the end of the code filled in with the correct numbers (0 if empty):
```
board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
```
And then add the following lines:
```
pp = pprint.PrettyPrinter(width=41, compact=True)
solve(board)
pp.pprint(board)
```