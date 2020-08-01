# PIECE CLASSES

# importing required modules
import pygame as pg

# importing required files
from settings import *

class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        # copy of the game class, allowing the pieces to access information about 
        # other pieces on the board
        self.game = game
        # calculates which side of the board the piece is on (B or W)
        # using this the colour of the piece can be determined
        if self.y > TILE_SIZE * 2:
            self.colour = "W"
        else:
            self.colour = "B"
        # pieces sprite groups
        if self.colour == "B":
            self.groups = game.all_sprites, game.black_pieces
        else:
            self.groups = game.all_sprites, game.white_pieces
        # initiates the sprite class
        pg.sprite.Sprite.__init__(self, self.groups)
        # used to determine whether a piece has been picked up

class King(Piece):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = (self.x + (TILE_SIZE / 2), self.y + (TILE_SIZE / 2))

    def load_image(self):
        """ Loads in the sprite image for the king piece """
        if self.colour == "B":
            self.image = pg.image.load("blackKing.png")
        else:
            self.image = pg.image.load("whiteKing.png")
class Queen(Piece):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = (self.x + (TILE_SIZE / 2), self.y + (TILE_SIZE / 2))
    
    def load_image(self):
        """ Loads in the sprite image for the queen piece """
        if self.colour == "B":
            self.image = pg.image.load("blackQueen.png")
        else:
            self.image = pg.image.load("whiteQueen.png")
class Rook(Piece):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = (self.x + (TILE_SIZE / 2), self.y + (TILE_SIZE / 2))

    def load_image(self):
        """ Loads in the sprite image for the rook piece """
        if self.colour == "B":
            self.image = pg.image.load("blackRook.png")
        else:
            self.image = pg.image.load("whiteRook.png")
class Bishop(Piece):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = (self.x + (TILE_SIZE / 2), self.y + (TILE_SIZE / 2))
    
    def load_image(self):
        """ Loads in the sprite image for the bishop piece """
        if self.colour == "B":
            self.image = pg.image.load("blackBishop.png")
        else:
            self.image = pg.image.load("whiteBishop.png")
class Knight(Piece):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = (self.x + (TILE_SIZE / 2), self.y + (TILE_SIZE / 2))
    
    def load_image(self):
        """ Loads in the sprite image for the knight piece """
        if self.colour == "B":
            self.image = pg.image.load("blackKnight.png")
        else:
            self.image = pg.image.load("whiteKnight.png")
class Pawn(Piece):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = (self.x + (TILE_SIZE / 2), self.y + (TILE_SIZE / 2))

    def load_image(self):
        """ Loads in the sprite image for the pawn piece """
        if self.colour == "B":
            self.image = pg.image.load("blackPawn.png")
        else:
            self.image = pg.image.load("whitePawn.png")