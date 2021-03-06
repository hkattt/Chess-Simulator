# MAIN GAME FILE

# importing required modules
import pygame as pg
import random
import time

# imports other game files
from player import *
from ai import *
from board import *
from display import *

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
        self.menu_image = pg.image.load("images/menu.jpg")
        self.menu_image = pg.transform.scale(self.menu_image, (512, 512))

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
        STARTING_BOARD = Image.open("C:/Users/Admin/Documents/Gungahlin College/Robotics/Chess-Simulator/images/START.png")
        set_colours(STARTING_BOARD, 480)

        self.run()

    def run(self):
        """ Main game loop """
        # playing against the AI
        if self.mode == "A":
            if self.running:
                self.playing = True
                while self.playing:
                    self.clock.tick(FPS)
                    self.events()
                    self.update()
                    self.paint()
                    if self.white.turn:
                        self.white.move()
                    elif self.ai.turn:
                        self.ai.move()
        # live demo
        elif self.mode == "D":
            i = 0
            if self.running:
                self.playing = True
                while self.playing:
                    self.clock.tick(FPS)
                    self.events()
                    self.update()
                    self.paint()
                    if self.white.turn:
                        self.white.move_from_img(i)
                        time.sleep(3)
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
            This function uses logic from the following source:
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

    def menu_screen(self):
        """ Main menu screen 
            NOTE: This was heavily inspired by the difficultly select system used in my previous pygame assignment """
        waiting = True
        if self.running:
            # creating buttons
            ai_button = Button(WHITE, WIDTH // 3.5, 160, 200, 40, "Play Against the AI", 16, self)
            demo_button = Button(WHITE, WIDTH // 3.5, 260, 200, 40, "Live Demonstration", 16, self)

            while waiting:
                # mouse position
                position = pg.mouse.get_pos()
                # background image
                self.screen.blit(self.menu_image, (0, 0))
                # title
                self.write("Chess Simulator", WHITE, 30,  WIDTH // 3.5, HEIGHT // 8)
                # buttons
                ai_button.draw(self.screen)
                demo_button.draw(self.screen)
                pg.display.update()

                for event in pg.event.get():
                    # checks if the player wants to quit
                    if event.type == pg.QUIT:
                        waiting = False
                        self.running = False
                    
                    # checks if the player wants to quit
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            waiting = False
                            self.running = False

                    if event.type == pg.MOUSEBUTTONDOWN:
                        # AI mode
                        if ai_button.mouse_over(position):
                            self.mode = "A"
                            waiting = False
                        # demo mode
                        elif demo_button.mouse_over(position):
                            self.mode = "D"
                            waiting = False

                    # checking if the user is hovering over a button
                    if event.type == pg.MOUSEMOTION:
                        # hovering over the AI button
                        if ai_button.mouse_over(position):
                            ai_button.colour = WHITE
                        else:
                            ai_button.colour = LIGHT_GREY
                        # hovering over the demo button
                        if demo_button.mouse_over(position):
                            demo_button.colour = WHITE
                        else:
                            demo_button.colour = LIGHT_GREY

    def write(self, text, colour, size, x, y):
        """ Draws text onto the screen """
        # setting the font size and type
        font = pg.font.Font("freesansbold.ttf", size)
        text_surface = font.render(text, True, colour)
        # creating the font rect
        text_rect = text_surface.get_rect()
        text_rect.center = x, y
        # drawing the text onto the screen
        self.screen.blit(text_surface, text_rect)

game = Game()
game.menu_screen()
while game.running:
    game.new()
    game.end_screen()