# PLAYER CLASS

# importing required modules
import pygame as pg
import math

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
        self.previous = False
        self.selected_piece= None

    def move(self):
        """ Player moves their pieces using the mouse """
        position = pg.mouse.get_pos() # position of the mouse cursor
        # returns a tuple of bool values (corresponding to each mouse button)
        # the first value [0] is the left mouse button
        pressed = pg.mouse.get_pressed() 

        # mouse button is pressed
        if pressed[0]:
            self.mousedown = True
            # checks if a piece was clicked
            self.clicked(position) 
        # mouse button is not pressed
        else:
            self.mousedown = False

        # moves the selected piece
        if self.selected_piece != None:
            self.selected_piece.rect.center = position

        # checks for state change (i.e. when the button is released)
        if self.mouse_up(self.mousedown):
            self.snap_to_grid()
            self.selected_piece = None
            self.turn = False

    def clicked(self, mousePos):
        """ Determines which piece got clicked """
        # the user can only pick up (click) their pieces (B or W)
        if self.colour == "W":
            for piece in self.game.white_pieces:
                # a piece is clicked if the mouse cursor is hovering over it (and the button got pressed)
                if piece.rect.collidepoint(mousePos):
                    self.selected_piece = piece
        
        else:
            for piece in self.game.black_pieces:
                # a piece is clicked if the mouse cursor is hovering over it (and the button got pressed)
                if piece.rect.collidepoint(mousePos):
                    self.selected_piece = piece

    def mouse_up(self, current):
        """ Looks for a statechange in the mouse press """
        # if the previous state is not the same as the current state
        # a state change has occurred.
        if self.previous != current:
            self.previous = current # update the previous state to be the current state
            # only returns true when the button has been released
            if current == False: 
                return True
        return False

    def snap_to_grid(self):
        """ Positions a newly moved piece in the centre of its tile """
        smallest = float('inf') # place holder (used to find the closest tile)
        # iterates over each tile
        for column in range(8):
            for row in range(8):
                # calculates the x, y coordinates of the centre the current tile
                tile_x, tile_y = (column * TILE_SIZE) + (TILE_SIZE / 2), (row * TILE_SIZE) + (TILE_SIZE / 2)
                # calculates the distance between the piece being moved and the current tile
                dist = math.sqrt(math.pow(self.selected_piece.rect.center[0] - tile_x, 2) + math.pow(self.selected_piece.rect.center[1] - tile_y, 2))
                # if the distance is smaller than the current smallest (or closest) the current distance is the smallest
                if dist < smallest:
                    smallest = dist
                    x, y = tile_x, tile_y
        # updates the pieces position to the centre of the closest tile
        self.selected_piece.rect.center = (x, y)

        






    