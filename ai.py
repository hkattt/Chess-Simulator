# AI CLASS

import pygame as pg
import copy

# importing files
from pieces import *

class AI():
    def __init__(self, colour, depth, game):
        self.colour = colour
        self.game = game
        if self.colour == "W":
            self.turn = True
        else:
            self.turn = False
        self.depth = depth
        self.values = {"P" : 10, "B" : 30, "Kn" : 30, "R" : 50, "Q" : 90, "K" : 1000}

    def move(self):
        if self.colour == "W":
            pieces = self.game.white_pieces
            enemy_pieces = self.game.black_pieces
        else:
            pieces = self.game.black_pieces
            enemy_pieces = self.game.white_pieces

        best_move = float('-inf')
        final_move = None

        for piece in pieces:
            piece.move_list()
            piece.fix_check()
            for move in piece.viable:
                board_copy = self.new_board(piece, move)
                for row in board_copy:
                    print(row)
                return
                value = self.minimax(self.depth - 1, board_copy, False)

    def minimax(self, depth, board, isMaximizing):
        if depth == 0:
            return -self.board_evaluation(board)

        self.generate_temp(board)
        
        if isMaximizing:
            best = -9999
            """
            for piece in self.temp_all_sprites:
                piece.move_list()
                return""""


    def new_board(self, piece, move):
        board_copy = copy.deepcopy(self.game.board)
        board_copy[piece.y][piece.x] = "."
        board_copy[move[1]][move[0]] = piece.colour + piece.symbol
        return board_copy

    def board_evaluation(self, board):
        value = 0
        for row in board:
            for piece in row:
                value += self.values[piece[1:]]
        return value

    def generate_temp(self, board):
        pass



