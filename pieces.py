# PIECE CLASSES

# importing required modules
import pygame as pg

class Piece():
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

class King(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.load_image()

    def load_image(self):
        if self.colour == "B":
            self.image = pg.image.load("blackKing.png")
        else:
            self.image = pg.image.load("whiteKing.png")

class Queen(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.load_image()
    
    def load_image(self):
        if self.colour == "B":
            self.image = pg.image.load("blackQueen.png")
        else:
            self.image = pg.image.load("whiteQueen.png")

class Rook(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.load_image()

    def load_image(self):
        if self.colour == "B":
            self.image = pg.image.load("blackRook.png")
        else:
            self.image = pg.image.load("whiteRook.png")

class Bishop(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.load_image()
    
    def load_image(self):
        if self.colour == "B":
            self.image = pg.image.load("blackBishop.png")
        else:
            self.image = pg.image.load("whiteBishop.png")

class Knight(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.load_image()
    
    def load_image(self):
        if self.colour == "B":
            self.image = pg.image.load("blackKnight.png")
        else:
            self.image = pg.image.load("whiteKnight.png")

class Pawn(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.load_image()

    def load_image(self):
        if self.colour == "B":
            self.image = pg.image.load("blackPawn.png")
        else:
            self.image = pg.image.load("whitePawn.png")