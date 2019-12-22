import pprint

# sudoki.py : solves a sudoku board by a backtracking method

def find_empty(board):
    """
    finds an empty space in the board
    :param board: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None