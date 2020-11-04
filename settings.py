# SETTINGS FILE

# game window size
WIDTH = 512
HEIGHT = 512

TILE_SIZE = 64
GRID_WIDTH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE

# colours and FPS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_GREY = (125, 135, 150)
DARK_GREY = (190, 190, 190)
LIGHT_BROWN = (181, 151, 120)
LIGHT_RED = (222, 23, 56)
FPS = 30

# chess vision variables / dictionaries

# ------- pawn_white ------- Piece_1 -------#

# ------- Consistency -------#

consistency_1 = False

# ------- pawn_black ------- Piece_2 -------#

# ------- Consistency -------#

consistency_2 = False

# ------- rook_white ------- Piece_3 -------#

# ------- Consistency -------#

consistency_3 = False

# ------- rook_black ------- Piece_4 -------#

# ------- Consistency -------#

consistency_4 = False

# ------- bishop_white ------- Piece_5 -------#

# ------- Consistency -------#

consistency_5 = False

# ------- bishop_black ------- Piece_6 -------#

# ------- Consistency -------#

consistency_6 = False

# ------- knight_white ------- Piece_7 -------#

# ------- Consistency -------#

consistency_7 = False

# ------- knight_black ------- Piece_8 -------#

# ------- Consistency -------#

consistency_8 = False

# ------- king_white ------- Piece_9 -------#

# ------- Consistency -------#

consistency_9 = False

# ------- king_black ------- Piece_10 -------#

# ------- Consistency -------#

consistency_10 = False

# ------- queen_white ------- Piece_11 -------#

# ------- Consistency -------#

consistency_11 = False

# ------- queen_black ------- Piece_12 -------#

# ------- Consistency -------#

consistency_12 = False

# several dictionaries are used to easily access the variables.
# the colour code dictionaries  wll be updates once the colour 
# calibration code is run (i.e. set_colours())

RED_UPPERS = {}

RED_LOWERS = {}

GREEN_UPPERS = {}

GREEN_LOWERS = {}

BLUE_UPPERS = {}

BLUE_LOWERS = {}

CONSISTENCIES = {
                1 : consistency_1, 2 : consistency_2, 3 : consistency_3, 4 : consistency_4, 5 : consistency_5, 6 : consistency_6, 7 : consistency_7, 8 : consistency_8,
                9 : consistency_9, 10 : consistency_10, 11 : consistency_11, 12 : consistency_12
                }