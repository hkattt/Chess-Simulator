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
        if (self.y * TILE_SIZE) > TILE_SIZE * 2:
            self.colour = "W"
        else:
            self.colour = "B"
        # pieces sprite groups
        if self.colour == "B":
            self.groups = game.all_sprites, game.black_pieces
        else:
            self.groups = game.all_sprites, game.white_pieces
        self.viable = []
        # initiates the sprite class
        pg.sprite.Sprite.__init__(self, self.groups)

    def tiles_occupied(self):
        occupied = [] # list containing all the occupied squares
        if self.colour == "W": # white piece
            for piece in self.game.white_pieces:
                occupied.append((piece.x, piece.y))
        else: # black piece
            for piece in self.game.black_pieces:
                occupied.append((piece.x, piece.y))
        return occupied
class King(Piece):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))

    def move_list(self):
        """ Generates a list contraining all of the king's viable moves """
        self.viable = []
        occupied = self.tiles_occupied()
        # generates potential moves
        self.viable += [(self.x + 1, self.y), (self.x, self.y + 1), (self.x - 1, self.y), (self.x, self.y - 1), 
            (self.x + 1, self.y + 1), (self.x - 1, self.y - 1), (self.x + 1, self.y - 1), (self.x - 1, self.y + 1)]
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in occupied]
        # removes moves that are off the board
        self.viable[:] = [move for move in self.viable if move[0] <= 7 if move[0] >= 0 if move[1] <= 7 if move[1] >= 0]

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
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))

    def move_list(self):
        """ Generates a list containing all of the queen's viable moves """
        self.viable = []
        occupied = self.tiles_occupied()

        # rook logic
        r = [(self.x + i, self.y) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # right
        l = [(self.x - i, self.y) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # left
        d = [(self.x, self.y - i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # down
        u = [(self.x, self.y + i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # up 
        self.viable += r + l + d + u

        # bishop logic
        ur = [(self.x + i, self.y + i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # up right
        dr = [(self.x + i, self.y - i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # down right 
        ul = [(self.x - i, self.y + i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # up left
        dl = [(self.x - i, self.y - i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # down left
        self.viable += ur + dr + ul + dl

        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in occupied]
    
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
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))

    def move_list(self):
        """ Generates a list containing all of the rook's viable moves """
        self.viable = []
        occupied = self.tiles_occupied()
        r = [(self.x + i, self.y) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # right
        l = [(self.x - i, self.y) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # left
        d = [(self.x, self.y - i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # down
        u = [(self.x, self.y + i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # up 
        self.viable += r + l + d + u
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in occupied]

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
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))

    def move_list(self):
        """ Generates a list containing all of the bishop's viable moves. 
            This function uses logic from the following source:
             https://codereview.stackexchange.com/questions/94465/enumerating-moves-for-a-chess-piece 11/8 """
        self.viable = []
        occupied = self.tiles_occupied()
        ur = [(self.x + i, self.y + i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # up right
        dr = [(self.x + i, self.y - i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # down right 
        ul = [(self.x - i, self.y + i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # up left
        dl = [(self.x - i, self.y - i) for i in range(1, 8) if 0 <= self.x < 8 and 0 <= self.y < 8] # down left
        self.viable += ur + dr + ul + dl
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in occupied]
    
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
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))

    def move_list(self):
        """ Generates a list containing all of the knight's viable moves """
        self.viable = []
        occupied = self.tiles_occupied()
        # adds potential moves
        self.viable += [(self.x + 1, self.y + 2), (self.x + 2, self.y + 1), (self.x + 2, self.y - 1), (self.x + 1, self.y - 2),
                         (self.x - 1, self.y - 2), (self.x - 2, self.y - 1), (self.x - 2, self.y + 1), (self.x - 1, self.y + 2)]
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in occupied]
        # removes moves that are off the board
        self.viable[:] = [move for move in self.viable if move[0] <= 7 if move[0] >= 0 if move[1] <= 7 if move[1] >= 0]

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
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))
        self.first = True

    def move_list(self):
        """ Generates a list containing all of the pawn's viable moves """
        self.viable = []
        occupied = self.tiles_occupied()
        # white pawn
        if self.colour == "W":
            # first move (pawns can jump two tiles)
            if self.first:
                self.viable += [(self.x, self.y - 2)]
                self.first = False

            # checks if the pawn can take any black pieces
            for piece in self.game.black_pieces:
                # top right
                if piece.x == self.x + 1 and piece.y == self.y - 1:
                    self.viable += [(piece.x, piece.y)]
                # top left
                elif piece.x == self.x - 1 and piece.y == self.y - 1:
                    self.viable += [(piece.x, piece.y)]
            self.viable += [(self.x, self.y - 1)]

        # black pawn
        else:
            # first move (pawns can jump two tiles)
            if self.first:
                self.viable += [(self.x, self.y + 2)]
                self.first = False

            # checks if the pawn can take any black pieces
            for piece in self.game.white_pieces:
                # bottom right
                if piece.x == self.x + 1 and piece.y == self.y + 1:
                    self.viable += [(piece.x, piece.y)]
                # bottom left
                elif piece.x == self.x - 1 and piece.y == self.y + 1:
                    self.viable += [(piece.x, piece.y)]
            self.viable += [(self.x, self.y + 1)]
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in occupied]
        # removes moves that are off the board
        self.viable[:] = [move for move in self.viable if move[0] <= 7 if move[0] >= 0 if move[1] <= 7 if move[1] >= 0]

    def load_image(self):
        """ Loads in the sprite image for the pawn piece """
        if self.colour == "B":
            self.image = pg.image.load("blackPawn.png")
        else:
            self.image = pg.image.load("whitePawn.png")