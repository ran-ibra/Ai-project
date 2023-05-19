import numpy as np
import random
import pygame
import sys
import math,time
import matplotlib.pyplot as plt

from miniMaxAlgorithm import *
from Board import *
from Winning import *
from Compare import *


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

minimax_execution_times = []
alpha_beta_execution_times = []

minimax_node_evaluations = []
alpha_beta_node_evaluations = []

board = formBord()
showgame(board)
game_over = False

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board , SQUARESIZE , height, RADIUS, screen)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

turn = random.choice([AI,PLAYER])

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)


        pygame.display.update()

        if turn == PLAYER:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            if turn == PLAYER:
                start_time = time.time()
                col, minimax_score = minimax(board, 5, True)
                end_time = time.time()
                execution_time = end_time - start_time
                minimax_execution_times.append(execution_time)
                minimax_node_evaluations.append(score_position(board, PLAYER_PIECE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    putting_peice(board, row, col, PLAYER_PIECE)

                    if winning_move(board, PLAYER_PIECE):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
                        compare(minimax_execution_times,alpha_beta_execution_times,minimax_node_evaluations,alpha_beta_node_evaluations)


                    #
                    turn += 1
                    turn = turn % 2
                    showgame(board)
                    draw_board(board, SQUARESIZE, height, RADIUS, screen)

    if turn == AI and not game_over:

        start_time = time.time()
        col, minimax_score = miniMaxalgo(board, 5, -math.inf, math.inf, True)
        end_time = time.time()
        execution_time = end_time - start_time
        alpha_beta_execution_times.append(execution_time)
        alpha_beta_node_evaluations.append(score_position(board, AI_PIECE))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            putting_peice(board, row, col, AI_PIECE)

            if winning_move(board, AI_PIECE):
                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True
                compare(minimax_execution_times,alpha_beta_execution_times,minimax_node_evaluations,alpha_beta_node_evaluations)

            showgame(board)
            #draw_board(board)
            draw_board(board , SQUARESIZE , height, RADIUS, screen)

            turn += 1
            turn = turn % 2

    if game_over:
        pygame.time.wait(3000)