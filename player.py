# PLAYER CLASS

# importing required modules
import pygame as pg

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

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mousedown = True
            else:
                self.mousedown = False
                self.mousereleased = True

    


    