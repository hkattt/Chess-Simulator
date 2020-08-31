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
        if self.colour == "W":
            self.turn = True
        else:
            self.turn = False
        self.mousedown = False
        self.previous = False
        self.selected_piece = None

    def move(self):
        """ Player moves their pieces using the mouse """
        position = pg.mouse.get_pos() # position of the mouse cursor
        # returns a tuple of bool values (corresponding to each mouse button)
        # the first value [0] is the left mouse button
        pressed = pg.mouse.get_pressed() 

        # mouse button is pressed
        if pressed[0]:
            # checks if the player is already carrying a piece
            if self.selected_piece == None: 
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
        # does not do anything if the user did not click on a piece (i.e. clicked the board)
        if self.mouse_up(self.mousedown) and self.selected_piece != None:
            self.snap_to_grid()
            if self.viable_move():
                # checks if the kings are in check (this is mainly for aesthetic purposes)
                # if a king is in check, then it will check to see if a check mate occurred
                for king in self.game.kings:
                    if king.in_check():
                        if king.check_mate():
                            self.game.playing = False
                            self.game.running = False
                # after the move it is the other players turn
                self.turn = False
                # player is not carrying a piece
                self.selected_piece = None
                if self.colour == "W":
                    self.game.black.turn = True
                else:
                    self.game.white.turn = True

    def viable_move(self):
        """ Checks if the current move is viable """
        # checks if the current move is viable (legal move)
        if (self.selected_piece.x, self.selected_piece.y) in self.selected_piece.viable:
            self.selected_piece.first = False # for a pawn that completed its first move
            self.take_piece(self.selected_piece.x, self.selected_piece.y)
            self.update_board()
            # updates the selected pieces original position
            self.selected_piece.original_x, self.selected_piece.original_y = self.selected_piece.x, self.selected_piece.y
            return True
        # if the move was not legal the selected piece is dropped and moved to its original position
        self.selected_piece.x, self.selected_piece.y = self.selected_piece.original_x, self.selected_piece.original_y
        self.selected_piece.rect.center = ((self.selected_piece.x * TILE_SIZE) + (TILE_SIZE / 2), (self.selected_piece.y * TILE_SIZE) + (TILE_SIZE / 2))
        self.selected_piece = None
        return False

    def take_piece(self, x, y):
        """ Takes a piece """
        # iterates over all the pieces
        # this does not allow the player to take their own pieces as it is not a 
        # viable move (i.e. it would not reach this point, the logic prevents it) 
        for piece in self.game.all_sprites:
            # checks if the current pieces coordinates is equal to the selected piece 
            # and is not the selected piece itself
            if piece.x == x and piece.y == y and piece != self.selected_piece:
                piece.kill() # removes the piece from groups

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
        # generates move list
        if self.selected_piece != None:
            self.selected_piece.move_list()
            self.selected_piece.fix_check() # removes moves that do not block / prevent a check

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
        # board coordinates
        self.selected_piece.x, self.selected_piece.y = int((x - (TILE_SIZE / 2)) / TILE_SIZE), int((y - (TILE_SIZE / 2)) / TILE_SIZE)

    def update_board(self):
        """ Updates the board list """
        self.game.board[self.selected_piece.original_y][self.selected_piece.original_x] = "."
        self.game.board[self.selected_piece.y][self.selected_piece.x] = self.selected_piece.colour + self.selected_piece.symbol