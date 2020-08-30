# AI CLASS

import pygame as pg

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



