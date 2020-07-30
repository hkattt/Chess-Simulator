# PLAYER CLASS

# importing required modules
import pygame as pg

# importing required files
from settings import *

class Player():
    def __init__(self, colour, game):
        self.colour = colour
        self.game = game
        if colour == "W":
            self.turn = True
        else:
            self.turn = False
        self.mousedown = False
        self.mousereleased = True

    def move(self):
        position = pg.mouse.get_pos()
        pressed = pg.mouse.get_pressed()

        if pressed[0]:
            self.mousedown = True
            self.mouse_over(position)
        else:
            self.mousedown = False
            self.mousereleased = True

    def mouse_over(self, mousePos):
        if self.colour == "W":
            for piece in self.game.white_pieces:
                if piece.x <= mousePos[0] and piece.x + TILE_SIZE >= mousePos[0]:
                    if piece.y <= mousePos[1] and piece.y + TILE_SIZE >= mousePos[1]:
                        print(piece)






    