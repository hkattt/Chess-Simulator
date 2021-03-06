# PIECE CLASSES

# importing required modules
import pygame as pg

# importing required files
from settings import *

class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, colour, groups, kings):
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y
        self.colour = colour
        # the group variable contains four groups
        #   1. all_sprites (i.e. all pieces)
        #   2. black pieces
        #   3. white pieces
        #   4. kings
        self.groups = groups
        # pieces sprite groups
        self.all_sprites = self.groups[0]
        if self.colour == "B":
            self.friendly_pieces = self.groups[1]
            self.enemy_pieces = self.groups[2]
        else:
            self.friendly_pieces = self.groups[2]
            self.enemy_pieces = self.groups[1]
        self.kings = kings
        self.viable = []
        self.first = True # used to determine whether a pawn can jump two pieces
        # initiates the sprite class
        pg.sprite.Sprite.__init__(self, (self.all_sprites, self.friendly_pieces))

    def occupied(self, group):
        """ Returns a list containing the coordinates of all the tiles that are
            currently occupied """
        occupied = [] # list containing all the occupied squares
        for piece in group:
            occupied.append((piece.x, piece.y))
        return occupied

    def fix_check(self):
        """ Removes moves that do not block / prevent a check """
        original_x, original_y = self.x, self.y # keeps track of the pieces original position
        new_viable = []
        # iterates over all the moves
        for move in self.viable:
            self.x, self.y = move[0], move[1] # updates the pieces position to the current move
            # if the current move does not result in the king being placed in check it is viable
            if self.king.in_check() != True:
                new_viable.append(move)
            # iterates over all of the enemy pieces
            for piece in self.enemy_pieces:
                # checks if the cooridnates of the current piece are the same as the current move
                # i.e. is the move taking the current piece
                if piece.x == move[0] and piece.y == move[1] and piece != self:
                    piece.kill() # temporarily removes the current piece from its groups
                    # if the current move results in a check it is removed from the viable list
                    # otherwise it is added if it is not already in the list
                    if self.king.in_check():
                        if move in new_viable:
                            new_viable.remove(move)
                    else:
                        if move not in new_viable:
                            new_viable.append(move)
                    # adding the piece back into its groups
                    piece.add(piece.all_sprites)
                    piece.add(piece.friendly_pieces)
                    # initiates the sprite class
                    pg.sprite.Sprite.__init__(piece, (piece.all_sprites, piece.friendly_pieces))
                    break
        # sets the pieces position back to the original position
        self.x, self.y = original_x, original_y
        self.viable = new_viable

    def friendly_king(self):
        """ Returns the friendly king object
            This serves the purpose of giving each piece access to its king """
        for king in self.kings:
            if king.colour == self.colour:
                return king
class King(Piece):
    def __init__(self, x, y, colour, groups, kings):
        super().__init__(x, y, colour, groups, kings)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))
        self.symbol = "K"
        # adds the king into the kings group
        self.kings.add(self)
        self.checked = False
        self.king = self
        
    def move_list(self):
        """ Generates a list contraining all of the king's viable moves """
        self.viable = []
        occupied = self.occupied(self.friendly_pieces)
        # generates potential moves
        self.viable += [(self.x + 1, self.y), (self.x, self.y + 1), (self.x - 1, self.y), (self.x, self.y - 1), 
            (self.x + 1, self.y + 1), (self.x - 1, self.y - 1), (self.x + 1, self.y - 1), (self.x - 1, self.y + 1)]
        # removes moves that have an occupied tile
        self.viable[:] = [move for move in self.viable if move not in occupied]
        # removes moves that are off the board
        self.viable[:] = [move for move in self.viable if move[0] <= 7 if move[0] >= 0 if move[1] <= 7 if move[1] >= 0]

    def in_check(self):
        """ Checks to see if the king is in check """
        all_moves = [] # list containing all possible moves
        # iterates over all of the enemy pieces and adds their possible
        # moves to all_moves
        for piece in self.enemy_pieces:
            piece.move_list()
            all_moves += piece.viable
        # if the kings' current position is the same as a potential move
        # then he is in check
        if (self.x, self.y) in all_moves:
            self.checked = True # this flag only exists for the check tiles drawing function (not having it makes it destroy the original viable list
            return True
        self.checked = False
        return False

    def check_mate(self):
        """ Checks if the king has been placed in check mate """
        moves = [] # list containing all possible moves
        # iterates over all friendly pieces and adds their potential
        # moves to all_moves
        for piece in self.friendly_pieces:
            piece.move_list()
            piece.fix_check()
            moves += piece.viable
        # if there are no mores in all_moves (i.e. length of the list = 0) the king
        # has been check mated
        if len(moves) == 0:
            return True
        return False
        
    def load_image(self):
        """ Loads in the sprite image for the king piece """
        if self.colour == "B":
            self.image = pg.image.load("images/blackKing.png")
        else:
            self.image = pg.image.load("images/whiteKing.png")
class Queen(Piece):
    def __init__(self, x, y, colour, groups, kings):
        super().__init__(x, y, colour, groups, kings)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))
        self.symbol = "Q"
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the queen's viable moves """
        self.viable = []
        occupied, friendly_occupied = self.occupied(self.all_sprites), self.occupied(self.friendly_pieces)
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
            self.image = pg.image.load("images/blackQueen.png")
        else:
            self.image = pg.image.load("images/whiteQueen.png")
class Rook(Piece):
    def __init__(self, x, y, colour, groups, kings):
        super().__init__(x, y, colour, groups, kings)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))
        self.symbol = "R"
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the rook's viable moves """
        self.viable = []
        occupied, friendly_occupied = self.occupied(self.all_sprites), self.occupied(self.friendly_pieces)
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
            self.image = pg.image.load("images/blackRook.png")
        else:
            self.image = pg.image.load("images/whiteRook.png")
class Bishop(Piece):
    def __init__(self, x, y, colour, groups, kings):
        super().__init__(x, y, colour, groups, kings)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))
        self.symbol = "B"
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the bishop's viable moves. 
            This function uses logic from the following source:
             https://codereview.stackexchange.com/questions/94465/enumerating-moves-for-a-chess-piece 11/8 """
        self.viable = []
        occupied, friendly_occupied = self.occupied(self.all_sprites), self.occupied(self.friendly_pieces)
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
            self.image = pg.image.load("images/blackBishop.png")
        else:
            self.image = pg.image.load("images/whiteBishop.png")
class Knight(Piece):
    def __init__(self, x, y, colour, groups, kings):
        super().__init__(x, y, colour, groups, kings)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))
        self.symbol = "Kn"
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the knight's viable moves """
        self.viable = []
        occupied = self.occupied(self.friendly_pieces)
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
            self.image = pg.image.load("images/blackKnight.png")
        else:
            self.image = pg.image.load("images/whiteKnight.png")
class Pawn(Piece):
    def __init__(self, x, y, colour, groups, kings):
        super().__init__(x, y, colour, groups, kings)
        self.load_image()
        # scales the image to the desired size
        self.image = pg.transform.scale(self.image, (64, 64))
        # an images rect is used to draw the image onto the game window
        self.rect = self.image.get_rect()
        # positions the piece in the centre of the tile
        self.rect.center = ((self.x * TILE_SIZE) + (TILE_SIZE / 2), (self.y * TILE_SIZE) + (TILE_SIZE / 2))
        self.symbol = "P"
        # access to the friendly king
        self.king = self.friendly_king()

    def move_list(self):
        """ Generates a list containing all of the pawn's viable moves """
        self.viable = []
        occupied, friendly_occupied = self.occupied(self.all_sprites), self.occupied(self.friendly_pieces)
        # white pawn
        if self.colour == "W":
            self.viable += [(self.x, self.y - 1)]
            # removes moves that have an occupied tile (stops pawn from moving forward when an enemy piece is on the way)
            self.viable[:] = [move for move in self.viable if move not in occupied]
            # first move (pawns can jump two tiles)
            if self.first and (self.x, self.y - 1) not in occupied and (self.x, self.y - 2) not in occupied:
                self.viable += [(self.x, self.y - 2)]

            # checks if the pawn can take any black pieces
            for piece in self.enemy_pieces:
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
            if self.first and (self.x, self.y + 1) not in occupied and (self.x, self.y + 2) not in occupied:
                self.viable += [(self.x, self.y + 2)]

            # checks if the pawn can take any black pieces
            for piece in self.enemy_pieces:
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
            self.image = pg.image.load("images/blackPawn.png")
        else:
            self.image = pg.image.load("images/whitePawn.png")