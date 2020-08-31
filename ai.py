# AI CLASS

import pygame as pg
import copy

from pieces import *

class AI():
    def __init__(self, colour, depth, game):
        self.colour = colour
        self.game = game
        if self.colour == "W":
            self.turn = True
            self.friendly_pieces = self.game.white_pieces
        else:
            self.friendly_pieces = self.game.black_pieces
        self.depth = depth
        self.values = {"P" : 10, "B" : 30, "Kn" : 30, "R" : 50, "Q" : 90, "K" : 1000}

    def move(self):
        best_move = float('-inf')
        final_move = None

        for piece in self.friendly_pieces:
            piece.move_list()
            piece.fix_check()
            for move in piece.viable:
                board_copy = self.new_board(piece, move)
                for row in board_copy:
                    print(row)
                print("")
                value = self.minimax(self.depth - 1, board_copy, False)
                return

    def minimax(self, depth, board, isMaximizing):
        if depth == 0:
            return -self.board_evaluation(board)

        self.generate_temp(board)

        for row in board:
            print(row)
        print("")
        
        if isMaximizing:
            best = -9999
            for piece in self.temp_whites:
                piece.move_list()
                piece.fix_check()
                for move in piece.viable:
                    board_copy = self.new_board(piece, move)
                    return
                    self.minimax(self.depth - 1, board_copy, False)

        else:
            best = 9999
            for piece in self.temp_blacks:
                piece.move_list()
                piece.fix_check()
                for move in piece.viable:
                    board_copy = self.new_board(piece, move)
                    for row in board_copy:
                        print(row)
                    return
                    self.minimax(self.depth - 1, board_copy, True)


    def new_board(self, piece, move):
        board_copy = copy.deepcopy(self.game.board)
        board_copy[piece.y][piece.x] = "."
        board_copy[move[1]][move[0]] = piece.colour + piece.symbol
        return board_copy

    def board_evaluation(self, board):
        value = 0
        for row in board:
            for piece in row:
                if piece != ".":
                    if piece[0] == self.colour:
                        value += self.values[piece[1:]]
                    else:
                        value += self.values[piece[1:]] * -1
        return value

    def generate_temp(self, board):
        self.temp_all = pg.sprite.Group()
        self.temp_whites = pg.sprite.Group()
        self.temp_blacks = pg.sprite.Group()
        self.kings = pg.sprite.Group()
        self.groups = (self.temp_all, self.temp_blacks, self.temp_whites)


        # kings are created before all of the other pieces
        King(4, 0, "B", self.groups, self.kings)
        King(4, 7, "W", self.groups, self.kings)
        # iterates over the board array
        # the board array holds the starting positions of all the pieces
        for row, tiles in enumerate(board):
            for column, tile in enumerate(tiles):
                # creates object based on each tiles string (string corresponding to each tile)
                if tile != ".":
                    # tile colour
                    if tile[0] == "B":
                        colour = "B"
                    else:
                        colour = "W"
                    if tile[1:] == "Q":
                        Queen(column, row, colour, self.groups, self.kings)
                    elif tile[1:] == "R":
                        Rook(column, row, colour, self.groups, self.kings)
                    elif tile[1:] == "B":
                        Bishop(column, row, colour, self.groups, self.kings)
                    elif tile[1:] == "Kn":
                        Knight(column, row, colour, self.groups, self.kings)
                    elif tile[1:] == "P":
                        Pawn(column, row, colour, self.groups, self.kings)


