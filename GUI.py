import pprint
import pygame
pygame.font.init()

# GUI.py : gui interface that solves a sudoku board by a backtracking method

# class grid : a class for the board layout
class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.win = win
        self.model = None
        self.selected = None
        self.cubes = # do the class cube beforehand
        self.update_model()

    def update_model(self):
        self.model =

    def place(self, val):

    def sketch(self, val):

    def draw(self):

    def select(self, row, col):

    def clear(self):

    def click(self, pos):

    def is_finished(self, pos):

    def solve(self):

    def solve_gui(self):