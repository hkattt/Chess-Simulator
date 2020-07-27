# MAIN GAME FILE

# Importing required modules
import pygame as pg
import random
import time

# Imports other game files
from settings import *
from pieces import *
from board import *

pg.init() 
pg.mixer.init()

class Game():
    def __init__(self): 
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) # Game window
        pg.display.set_caption("Chess") # Game windows caption
        self.clock = pg.time.Clock()
        self.running = True
        self.colour_index = [WHITE, BLACK]

    def load_board(self):
        pass

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.black_pieces = pg.sprite.Group()
        self.white_pieces = pg.sprite.Group()
        self.run()

    def run(self):
        if self.running:
            self.playing = True
            while self.playing:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.paint()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            # Checks if the user wants to quit the game
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        if self.playing:
                            self.playing = False
                        self.running = False

    def board_colours(self):
        index = 0
        for column in range(8):
            for row in range(8):
                pg.draw.rect(self.screen, self.colour_index[index], (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0)
                index = (index - 1) * -1
            index = (index -1) * -1

    def paint(self):
        self.board_colours()
        pg.display.update()

game = Game()
while game.running:
    game.new()