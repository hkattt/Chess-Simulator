# AI CLASS

import pygame as pg
import copy

class AI():
    def __init__(self, colour, game):
        self.colour = colour
        self.game = game
        if self.colour == "W":
            self.turn = True
        else:
            self.turn = False

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
            for move in piece.viable:
                board_copy = self.new_board(piece, move)
                

    def new_board(self, piece, move):
        board_copy = copy.deepcopy(self.game.board)
        board_copy[piece.y][piece.x] = "."
        board_copy[move[1]][move[0]] = piece.colour + piece.symbol
        return board_copy






