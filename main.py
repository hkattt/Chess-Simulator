# MAIN GAME FILE

# importing required modules
import pygame as pg
import random
import time

# imports other game files
from pieces import *
from player import *
from board import *

pg.init() 
pg.mixer.init()
class Game():
    def __init__(self): 
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) # game window
        pg.display.set_caption("Chess") # game windows title
        self.clock = pg.time.Clock() # controls FPS
        self.running = True 
        self.board = board # board containing the position of each piece

    def new(self):
        """ Creates a new game """
        # creates players
        self.white = Player("W", self)
        self.black = Player("B", self)
        self.teams = [self.white, self.black]

        # creates sprite groups
        self.all_sprites = pg.sprite.Group()
        self.black_pieces = pg.sprite.Group()
        self.white_pieces = pg.sprite.Group()

        # iterates over the board array
        # the board array holds the starting positions of all the pieces
        for row, tiles in enumerate(self.board):
            for column, tile in enumerate(tiles):
                # creates object based on each tiles string (string corresponding to each tile)
                if tile != ".":
                    if tile == "K":
                        King(column, row, self)
                    elif tile == "Q":
                        Queen(column, row, self)
                    elif tile == "R":
                        Rook(column, row, self)
                    elif tile == "B":
                        Bishop(column, row, self)
                    elif tile == "Kn":
                        Knight(column, row, self)
                    elif tile == "P":
                        Pawn(column, row, self)
        self.run()

    def run(self):
        """ Main game loop """
        if self.running:
            self.playing = True
            while self.playing:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.paint()
                if self.white.turn:
                    self.white.move()
                elif self.black.turn:
                    self.black.move()

    def update(self):
        """ Updates window """
        self.all_sprites.update()

    def events(self):
        """ Game loop events """
        for event in pg.event.get():
            # checks if the user wants to quit the game
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                # checks if the user pressed the escape key
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False

    def board_colours(self):
        """ Draws the board tiles """
        index = 0 
        colour_index = [WHITE, LIGHT_BROWN] 
        # iterates over every tile on the chess board
        for column in range(8):
            for row in range(8):
                # draws a new tile in each position, changing the colour each time
                pg.draw.rect(self.screen, BLACK, (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0)
                pg.draw.rect(self.screen, colour_index[index], (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1), 0)
                index = (index - 1) * -1 # flips the colour
            index = (index -1) * -1 # ensures each row starts with a different colour

    def viable_colours(self):
        """ Draws the viable tiles onto the board """
        # iterates over both of the teams (W & B)
        for team in self.teams:
            if team.turn: # checks which teams turn it is
                if team.selected_piece != None: # checks if the player is carrying a piece
                    # draws all the viable moves (i.e. draws circles onto the board)
                    for move in team.selected_piece.viable:
                        pg.draw.rect(self.screen, BLACK, (move[0] * TILE_SIZE, move[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0)
                        pg.draw.rect(self.screen, DARK_GREY, (move[0] * TILE_SIZE, move[1] * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1), 0)

    def paint(self):
        """ Draws onto the window """
        self.board_colours()
        self.viable_colours()

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, sprite)

        pg.display.update() # updates the window

game = Game()
while game.running:
    game.new()