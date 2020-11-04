# MAIN GAME FILE

# importing required modules
import pygame as pg
import random
import time

# imports other game files
from player import *
from ai import *
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
        self.font = pg.font.Font("freesansbold.ttf", 32)

    def new(self):
        """ Creates a new game """
        # creates players
        self.white = Player("W", self)
        #self.black = Player("B", self)

        # creates sprite groups
        self.all_sprites = pg.sprite.Group()
        self.black_pieces = pg.sprite.Group()
        self.white_pieces = pg.sprite.Group()
        self.kings = pg.sprite.Group()
        self.groups = (self.all_sprites, self.black_pieces, self.white_pieces)

        self.ai = AI("B", 2, self)
        self.teams = [self.white, self.ai]

        self.generate_pieces()

        # determines the RGB values for all of the pieces
        STARTING_BOARD = Image.open("C:/Users/hugok/Desktop/School Work/Gungahlin College/Robotics/Term 3/Hugo-Kat-Pygame-Chess/START.png")
        set_colours(STARTING_BOARD, 480)

        self.run()

    def run(self):
        """ Main game loop """
        i = 0
        if self.running:
            self.playing = True
            while self.playing:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.paint()
                if self.white.turn:
                    #self.white.move()
                    self.white.move_from_img(i)
                    time.sleep(5)
                    i += 1
                    i %= 3
                elif self.ai.turn:
                    self.ai.move()

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
        """ Draws the board tiles. 
            This function uses logic from the follows source:
            https://github.com/chattarajoy/Shatranj/blob/master/helperfunctions.py 27/7 """
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
        if self.white.selected_piece != None: # checks if the player is carrying a piece
            # draws all the viable moves (i.e. draws circles onto the board)
            for move in self.white.selected_piece.viable:
                pg.draw.rect(self.screen, BLACK, (move[0] * TILE_SIZE, move[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0)
                pg.draw.rect(self.screen, DARK_GREY, (move[0] * TILE_SIZE, move[1] * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1), 0)

    def check_colours(self):
        """ Draws the checked tiles onto the board """
        # iterates over the kings:
        for king in self.kings:
            if king.checked: # king is checked
                pg.draw.rect(self.screen, BLACK, (king.x * TILE_SIZE, king.y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0)
                pg.draw.rect(self.screen, LIGHT_RED, (king.x * TILE_SIZE, king.y * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1), 0)
                
    def paint(self):
        """ Draws onto the window """
        self.board_colours() # draws the board colours
        self.viable_colours() # draws the viable move colours
        self.check_colours() # draws the check colours

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, sprite)
        # the current selected piece (one being moved) is drawn last
        # this gives off the illusion that it is above the other pieces
        #if self.black.selected_piece != None: # black player is moving a piece
        #    self.screen.blit(self.black.selected_piece.image, self.black.selected_piece)
        if self.white.selected_piece != None: # white player is moving a piece
            self.screen.blit(self.white.selected_piece.image, self.white.selected_piece)

        pg.display.update() # updates the window

    def end_screen(self):
        """ Screen after a player has been checkmated """
        for king in self.kings:
            if king.checked:
                self.paint() # updates the screen
                text = self.font.render("CHECK MATE", True, LIGHT_RED) # font
                text_rect = text.get_rect() # fonts rect
                text_rect.center = WIDTH // 2, HEIGHT // 2 # fonts position
                running = True
                while running:
                    for event in pg.event.get():
                        # checks if the user wants to quit the game
                        if event.type == pg.QUIT:
                            running = False
                        if event.type == pg.KEYDOWN:
                            # checks if the user pressed the escape key
                            if event.key == pg.K_ESCAPE:
                                running = False
                    self.screen.blit(text, text_rect)
                    pg.display.update()
    
    def generate_pieces(self):
        """ Generates pieces from the current game board """
        # kings are created before all of the other pieces
        King(4, 0, "B", self.groups, self.kings)
        King(4, 7, "W", self.groups, self.kings)
        # iterates over the board array
        # the board array holds the starting positions of all the pieces

        for row, tiles in enumerate(self.board):
            for column, tile in enumerate(tiles):
                # creates object based on each tiles string (string corresponding to each tile)
                if tile != ".":
                    # tile colour
                    if tile[0] == "B":
                        colour = "B"
                    else:
                        colour = "W"
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


game = Game()
while game.running:
    game.new()
    game.end_screen()