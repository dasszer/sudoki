import pprint

# sudoki.py : solves a sudoku board by a backtracking method

def solve(board):
    """
    Solves a sudoku board using backtracking
    :param board: 2d list of ints
    :return: solution
    """
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


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

def valid(board, pos, num):
    """
    Returns true if the attempted move is valid
    :param board: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """

    # Check in row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check in col
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # Check in box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

