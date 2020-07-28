# MAIN GAME FILE

# importing required modules
import pygame as pg
import random
import time

# imports other game files
from settings import *
from pieces import *
from board import *

pg.init() 
pg.mixer.init()

class Game():
    def __init__(self): 
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) # game window
        pg.display.set_caption("Chess") # game windows title
        self.clock = pg.time.Clock() # controls FPS
        self.running = True

    def load_board(self):
        pass

    def new(self):
        """ Creates a new game """
        self.all_sprites = pg.sprite.Group()
        self.black_pieces = pg.sprite.Group()
        self.white_pieces = pg.sprite.Group()
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
        colour_index = [WHITE, BLACK] 
        # iterates over every tile on the chess board
        for column in range(8):
            for row in range(8):
                # draws a new tile in each position, changing the colour each time
                pg.draw.rect(self.screen, colour_index[index], (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0)
                index = (index - 1) * -1 # flips the colour
            index = (index -1) * -1 # ensures each row starts with a different colour

    def paint(self):
        """ Draws onto the window """
        self.board_colours()
        pg.display.update() # updates the window

game = Game()
while game.running:
    game.new()