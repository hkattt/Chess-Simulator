# AI CLASS

# importing required modules
import pygame as pg
import copy

# importing required files
from pieces import *
from move_tiles import *

class AI():
    def __init__(self, colour, depth, game):
        self.colour = colour
        self.game = game
        self.friendly_pieces, self.enemy_pieces = self.game.black_pieces, self.game.white_pieces
        self.depth = depth
        self.turn = False
        self.values = {"P" : 10, "B" : 30, "Kn" : 30, "R" : 50, "Q" : 90, "K" : 1000}
        self.tile_values = {"P" : PAWN_TILES, "B" : BISHOP_TILES, "Kn" : KNIGHT_TILES, "R" : ROOK_TILES, "Q" : QUEEN_TILES, "K" : KING_TILES}

    def move(self):
        selected_piece, move = self.minimax_seed(self.depth, self.game.board, True) # get the 'best' move from the minimax algorithm
        # updates the pieces position and rect (to the move)
        selected_piece.x, selected_piece.y = move[0], move[1] 
        selected_piece.rect.center = ((selected_piece.x * TILE_SIZE) + TILE_SIZE // 2),  ((selected_piece.y * TILE_SIZE) + TILE_SIZE // 2)
        self.take_piece(move[0], move[1]) # take a piece with the move
        self.update_board(selected_piece)
        selected_piece.original_x, selected_piece.original_y = selected_piece.x, selected_piece.y
        
        # checks if a king has been check mated
        for king in self.game.kings:
            if king.in_check():
                if king.check_mate():
                    self.game.playing = False
                    self.game.running = False
        self.turn, self.game.white.turn = False, True

    def minimax_seed(self, depth, board, isMaximizing):
        """ this function uses logic from the following sources:
            https://github.com/AnthonyASanchez/PythonChessAi
            https://github.com/devinalvaro/yachess/tree/master/src """
        best_move = float('-inf')
        final_move = None
        # MINIMAX ROOT 
        # iterates over all of the friendly pieces
        for piece in self.friendly_pieces:
            # generates the move list for the current piece
            piece.move_list()
            piece.fix_check()
            # iterates over all of the viable moves
            for move in piece.viable:
                # creates a copy of the current board with the current move played
                # i.e. makes a board with the current piece moved to the current move
                board_copy = self.new_board(self.game.board, piece, move)
                # runs minimax on the copied board
                value = max(best_move, self.minimax(self.depth - 1, board_copy, -10000, 10000, False))
                if value > best_move:
                    best_move = value
                    # saving the best move
                    final_move = (piece, move)
        return (final_move[0], final_move[1])

    def minimax(self, depth, board, alpha, beta, isMaximizing):
        """ this function uses logic from the following source:
            https://github.com/AnthonyASanchez/PythonChessAi """
        # if the depth is equal to 0, minimax retruns the 'value' of the board
        # the boards value is determined by adding up the net sum of all of the pieces

        if depth == 0:
            return self.board_evaluation(board)

        # creates temporary pieces
        self.generate_temp(board)

        # computers turn
        if isMaximizing:
            best = float('-inf')
            for piece in self.temp_blacks:
                piece.move_list()
                piece.fix_check()
                for move in piece.viable:
                    board_copy = self.new_board(board, piece, move)
                    best = max(best, self.minimax(depth - 1, board_copy, alpha, beta, False))
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        return best
            return best

        # users turn
        else:
            best = float('inf')
            for piece in self.temp_whites:
                piece.move_list()
                piece.fix_check()
                for move in piece.viable:
                    board_copy = self.new_board(board, piece, move)
                    best = min(best, self.minimax(depth - 1, board_copy, alpha, beta, True))
                    beta = min(beta, best)
                    if beta <= alpha:
                        return best
            return best

    def new_board(self, board, piece, move):
        board_copy = copy.deepcopy(board)
        board_copy[piece.y][piece.x] = "."
        board_copy[move[1]][move[0]] = piece.colour + piece.symbol
        return board_copy

    def update_board(self, piece):
        self.game.board[piece.y][piece.x] = piece.colour + piece.symbol
        self.game.board[piece.original_y][piece.original_x] = "."

    def board_evaluation(self, board):
        self.generate_temp(board)
        value = 0
        for piece in self.temp_all:
            if piece.colour == self.colour:
                value += (self.values[piece.symbol] + self.tile_values[piece.symbol][piece.y][piece.x])
            else:
                value += (self.values[piece.symbol] + self.tile_values[piece.symbol][piece.y][piece.x]) * -1

        for king in self.kings:
            if king.colour == self.colour:
                if king.in_check():
                    if king.check_mate():
                        value -= 100000
                    else:
                        value -= 50       
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
                    if tile[1:] == "K":
                        for king in self.kings:
                            if king.colour == colour:
                                king.x, king.y = column, row
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

    def take_piece(self, x, y):
        """ Takes a piece """
        # iterates over all the pieces
        # this does not allow the player to take their own pieces as it is not a 
        # viable move (i.e. it would not reach this point, the logic prevents it) 
        for piece in self.enemy_pieces:
            # checks if the current pieces coordinates is equal to the selected piece 
            # and is not the selected piece itself
            if piece.x == x and piece.y == y:
                piece.kill() # removes the piece from groups
