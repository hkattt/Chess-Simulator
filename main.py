# MAIN GAME FILE

# Importing required modules
import pygame
import random
import time

# Imports other game files
from settings import *
from pieces import *
from board import *

pygame.init() 
pygame.mixer.init()

class Game():
    def __init__(self): 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Game window
        pygame.display.set_caption("Chess") # Game windows caption
        self.clock = pygame.time.Clock()
        self.running = True

    def load_board(self):
        pass

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.black_pieces = pygame.sprite.Group()
        self.white_pieces = pygame.sprite.Group()
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
        for event in pygame.event.get():
            # Checks if the user wants to quit the game
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.playing:
                            self.playing = False
                        self.running = False

    def paint(self):
        pass
