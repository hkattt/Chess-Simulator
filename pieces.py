# PIECE CLASSES

# importing required modules
import pygame as pg

# importing required files
from settings import *

class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y
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
        self.first = True # used to determine whether a pawn can jump two pieces
        self.checking = False
        # initiates the sprite class
        pg.sprite.Sprite.__init__(self, self.groups)

    def friendly_occupied(self):
        """ Returns a list containing the coordinates of all the tiles that are
            occupied by friendly pieces """
        occupied = [] # list containing all the occupied squares
        if self.colour == "W": # white piece
            for piece in self.game.white_pieces:
                occupied.append((piece.x, piece.y))
        else: # black piece
            for piece in self.game.black_pieces:
                occupied.append((piece.x, piece.y))
        return occupied

    def occupied(self):
        """ Returns a list containing the coordinates of all the tiles that are
            currently occupied """
        occupied = [] # list containing all the occupied squares
        for piece in self.game.all_sprites:
            occupied.append((piece.x, piece.y))
        return occupied

    def fix_check(self):
        """ Removes moves that do not block / prevent a check """
        original_x, original_y = self.x, self.y # keeps track of the pieces original position
        new_viable = []
        # iterates over all the moves
        for move in self.viable:
            self.x, self.y = move[0], move[1] # updates the pieces position to the current move
            # checks if this move prevents / blocks the check
            # if it does, it is added to the new viable list
            if self.king.in_check() != True: 
                new_viable.append(move)
            # iterates over all the pieces
            for piece in self.game.all_sprites:
                # if the current piece is checking and is in the same position as the current move
                # the move is viable (i.e. if the current move can take the piece putting its king in check)
                if piece.checking:
                    if piece.x == self.x and piece.y == self.y:
                        new_viable.append(move)
        # sets the pieces position back to the original position
        self.x, self.y = original_x, original_y
        self.viable = new_viable

    def is_checking(self):
        """ Checks if the piece is putting the opposition king into check """
        for king in self.game.kings:
            # king on the opposite team
            if king.colour != self.colour:
                # kings current position is one of the viable moves
                if (king.x, king.y) in self.viable:
                    return True
        return False

    def friendly_king(self):
        """ Returns the friendly king object
            This serves the purpose of giving each piece access to its king """
        for king in self.game.kings:
            if king.colour == self.colour:
                return king

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
        # adds the king into the kings group
        self.game.kings.add(self)
        self.checked = False
        self.king = self
        
    def move_list(self):
        """ Generates a list contraining all of the king's viable moves """
        self.viable = []
        occupied = self.friendly_occupied()
        # generates potential moves
        self.viable += [(self.x + 1, self.y), (self.x, self.y + 1), (self.x - 1, self.y), (self.x, self.y - 1), 
            (self.x + 1, self.y + 1), (self.x - 1, self.y - 1), (self.x + 1, self.y - 1), (self.x - 1, self.y + 1)]
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in occupied]
        # removes moves that are off the board
        self.viable[:] = [move for move in self.viable if move[0] <= 7 if move[0] >= 0 if move[1] <= 7 if move[1] >= 0]

    def in_check(self):
        all_moves = []
        if self.colour == "W":
            for piece in self.game.black_pieces:
                piece.move_list()
                all_moves += piece.viable
        else:
            for piece in self.game.white_pieces:
                piece.move_list()
                all_moves += piece.viable
        if (self.x, self.y) in all_moves:
            self.checked = True
            return True
        self.checked = False
        return False
        
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
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the queen's viable moves """
        self.viable = []
        occupied, friendly_occupied = self.occupied(), self.friendly_occupied()
        rook_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # rooks possible moving directions (i.e. right, left, up, down)
        move_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)] # possible moving directions (i.e. up right, down right, up left, down left)
        moves = []
        # rook logic
        # iterates over each direction
        for direction in rook_directions:
            for i in range(1, 8):
                if 0 <= self.x < 8 and 0 <= self.y < 8:
                    # adding viable moves
                    moves += [(self.x + i * direction[0], self.y + i * direction[1])]
                # stops adding moves once a piece is found (can't move through pieces)
                # this is done by breaking the loop (i.e. stopping the current direction)
                if (self.x + i * direction[0], self.y + i * direction[1]) in occupied:
                    break
        # bishop logic
        # iterates over each direction
        for direction in move_directions:
            for i in range(1, 8):
                if 0 <= self.x < 8 and 0 <= self.y < 8:
                    # adding viable moves
                    moves += [(self.x + i * direction[0], self.y + i * direction[1])]
                # stops adding moves once a piece is found (can't move through pieces)
                # this is done by breaking the loop (i.e. stooping the current direcion)
                if (self.x + i * direction[0], self.y + i * direction[1]) in occupied:
                    break
        # adding the moves
        self.viable += moves
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in friendly_occupied]
        # removes moves that are off the board
        self.viable[:] = [move for move in self.viable if move[0] <= 7 if move[0] >= 0 if move[1] <= 7 if move[1] >= 0]
    
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
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the rook's viable moves """
        self.viable = []
        occupied, friendly_occupied = self.occupied(), self.friendly_occupied()
        move_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # possible moving directions (i.e. right, left, up, down)
        moves = []
        # iterates over each direction
        for direction in move_directions:
            for i in range(1, 8):
                if 0 <= self.x < 8 and 0 <= self.y < 8:
                    # adding viable moves
                    moves += [(self.x + i * direction[0], self.y + i * direction[1])]
                # stops adding moves once a piece is found (can't move through pieces)
                # this is done by breaking the loop (i.e. stopping the current direction)
                if (self.x + i * direction[0], self.y + i * direction[1]) in occupied:
                    break
        # adding the moves
        self.viable += moves
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in friendly_occupied]
        # removes moves that are off the board
        self.viable[:] = [move for move in self.viable if move[0] <= 7 if move[0] >= 0 if move[1] <= 7 if move[1] >= 0]

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
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the bishop's viable moves. 
            This function uses logic from the following source:
             https://codereview.stackexchange.com/questions/94465/enumerating-moves-for-a-chess-piece 11/8 """
        self.viable = []
        occupied, friendly_occupied = self.occupied(), self.friendly_occupied()
        move_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)] # possible moving directions (i.e. up right, down right, up left, down left)
        moves = []
        # iterates over each direction
        for direction in move_directions:
            for i in range(1, 8):
                if 0 <= self.x < 8 and 0 <= self.y < 8:
                    # adding viable moves
                    moves += [(self.x + i * direction[0], self.y + i * direction[1])]
                # stops adding moves once a piece is found (can't move through pieces)
                # this is done by breaking the loop (i.e. stooping the current direcion)
                if (self.x + i * direction[0], self.y + i * direction[1]) in occupied:
                    break
        # adding the moves
        self.viable += moves
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in friendly_occupied]
        # removes moves that are off the board
        self.viable[:] = [move for move in self.viable if move[0] <= 7 if move[0] >= 0 if move[1] <= 7 if move[1] >= 0]
        
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
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the knight's viable moves """
        self.viable = []
        occupied = self.friendly_occupied()
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
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the pawn's viable moves """
        self.viable = []
        occupied, friendly_occupied = self.occupied(), self.friendly_occupied()
        # white pawn
        if self.colour == "W":
            self.viable += [(self.x, self.y - 1)]
            # removes moves that have an occupied tile (stops pawn from moving forward when an enemy piece is on the way)
            self.viable[:] = [move for move in self.viable if move not in occupied]
            # first move (pawns can jump two tiles)
            if self.first:
                self.viable += [(self.x, self.y - 2)]

            # checks if the pawn can take any black pieces
            for piece in self.game.black_pieces:
                # top right
                if piece.x == self.x + 1 and piece.y == self.y - 1:
                    self.viable += [(piece.x, piece.y)]
                # top left
                elif piece.x == self.x - 1 and piece.y == self.y - 1:
                    self.viable += [(piece.x, piece.y)]

        # black pawn
        else:
            self.viable += [(self.x, self.y + 1)]
            # removes moves that have an occupied tile (stops pawn from moving forward when an enemy piece is on the way)
            self.viable[:] = [move for move in self.viable if move not in occupied]
            # first move (pawns can jump two tiles)
            if self.first:
                self.viable += [(self.x, self.y + 2)]

            # checks if the pawn can take any black pieces
            for piece in self.game.white_pieces:
                # bottom right
                if piece.x == self.x + 1 and piece.y == self.y + 1:
                    self.viable += [(piece.x, piece.y)]
                # bottom left
                elif piece.x == self.x - 1 and piece.y == self.y + 1:
                    self.viable += [(piece.x, piece.y)]
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in friendly_occupied]
        # removes moves that are off the board
        self.viable[:] = [move for move in self.viable if move[0] <= 7 if move[0] >= 0 if move[1] <= 7 if move[1] >= 0]

    def load_image(self):
        """ Loads in the sprite image for the pawn piece """
        if self.colour == "B":
            self.image = pg.image.load("blackPawn.png")
        else:
            self.image = pg.image.load("whitePawn.png")