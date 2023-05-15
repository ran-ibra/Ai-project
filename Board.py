import numpy as np

from miniMaxAlgorithm import *
from Winning import *


PLAYER = 0
AI = 1
EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4

def formBord():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def putting_peice(board, row, col, piece):
    board[row][col] = piece

    
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def showgame(board):
    print(np.flip(board, 0))
