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
#-------------------------------------------#

# ------- pawn_white ------- Piece_1 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_1 = 5
pixel_green_upper_bound_1 = 5
pixel_blue_upper_bound_1 = 144

# ------- Lower_Bounds -------#

pixel_red_lower_bound_1 = 0
pixel_green_lower_bound_1 = 0
pixel_blue_lower_bound_1 = 134

# ------- Consistency -------#

consistency_1 = False

# ------- pawn_black ------- Piece_2 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_2 = 132 
pixel_green_upper_bound_2 = 255
pixel_blue_upper_bound_2 = 217

# ------- Lower_Bounds -------#

pixel_red_lower_bound_2 = 122
pixel_green_lower_bound_2 = 250
pixel_blue_lower_bound_2 = 107

# ------- Consistency -------#

consistency_2 = False

# ------- rook_white ------- Piece_3 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_3 = 5
pixel_green_upper_bound_3 = 255
pixel_blue_upper_bound_3 = 255

# ------- Lower_Bounds -------#

pixel_red_lower_bound_3 = 0
pixel_green_lower_bound_3 = 250
pixel_blue_lower_bound_3 = 250

# ------- Consistency -------#

consistency_3 = False

# ------- rook_black ------- Piece_4 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_4 = 255
pixel_green_upper_bound_4 = 255
pixel_blue_upper_bound_4 = 5

# ------- Lower_Bounds -------#

pixel_red_lower_bound_4 = 250
pixel_green_lower_bound_4 = 250
pixel_blue_lower_bound_4 = 0

# ------- Consistency -------#

consistency_4 = False

# ------- bishop_white ------- Piece_5 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_5 = 215
pixel_green_upper_bound_5 = 110
pixel_blue_upper_bound_5 = 35

# ------- Lower_Bounds -------#

pixel_red_lower_bound_5 = 205
pixel_green_lower_bound_5 = 100
pixel_blue_lower_bound_5 = 25

# ------- Consistency -------#

consistency_5 = False

# ------- bishop_black ------- Piece_6 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_6 = 133 
pixel_green_upper_bound_6 = 5
pixel_blue_upper_bound_6 = 133

# ------- Lower_Bounds -------#

pixel_red_lower_bound_6 = 123
pixel_green_lower_bound_6 = 0
pixel_blue_lower_bound_6 = 123

# ------- Consistency -------#

consistency_6 = False

# ------- knight_white ------- Piece_7 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_7 = 255
pixel_green_upper_bound_7 = 5
pixel_blue_upper_bound_7 = 5

# ------- Lower_Bounds -------#

pixel_red_lower_bound_7 = 250
pixel_green_lower_bound_7 = 0
pixel_blue_lower_bound_7 = 0

# ------- Consistency -------#

consistency_7 = False

# ------- knight_black ------- Piece_8 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_8 = 255
pixel_green_upper_bound_8 = 197
pixel_blue_upper_bound_8 = 208

# ------- Lower_Bounds -------#

pixel_red_lower_bound_8 = 250
pixel_green_lower_bound_8 = 187
pixel_blue_lower_bound_8 = 198

# ------- Consistency -------#

consistency_8 = False

# ------- king_white ------- Piece_9 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_9 = 133
pixel_green_upper_bound_9 = 5
pixel_blue_upper_bound_9 = 5

# ------- Lower_Bounds -------#

pixel_red_lower_bound_9 = 123
pixel_green_lower_bound_9 = 0
pixel_blue_lower_bound_9 = 0

# ------- Consistency -------#

consistency_9 = False

# ------- king_black ------- Piece_10 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_10 = 255 
pixel_green_upper_bound_10 = 160
pixel_blue_upper_bound_10 = 5

# ------- Lower_Bounds -------#

pixel_red_lower_bound_10 = 250
pixel_green_lower_bound_10 = 150
pixel_blue_lower_bound_10 = 0

# ------- Consistency -------#

consistency_10 = False

# ------- queen_white ------- Piece_11 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_11 = 197
pixel_green_upper_bound_11 = 197
pixel_blue_upper_bound_11 = 197

# ------- Lower_Bounds -------#

pixel_red_lower_bound_11 = 187
pixel_green_lower_bound_11 = 187
pixel_blue_lower_bound_11 = 187

# ------- Consistency -------#

consistency_11 = False

# ------- queen_black ------- Piece_12 -------#

# ------- Upper_Bounds -------#

pixel_red_upper_bound_12 = 5
pixel_green_upper_bound_12 = 133
pixel_blue_upper_bound_12 = 5

# ------- Lower_Bounds -------#

pixel_red_lower_bound_12 = 0
pixel_green_lower_bound_12 = 123
pixel_blue_lower_bound_12 = 0

# ------- Consistency -------#

consistency_12 = False

# several dictionaries are used to easily access the variables.

RED_UPPERS = {
            1 : pixel_red_upper_bound_1, 2 : pixel_red_upper_bound_2, 3 : pixel_red_upper_bound_3, 4 : pixel_red_upper_bound_4, 5 : pixel_red_upper_bound_5, 
            6 : pixel_red_upper_bound_6, 7 : pixel_red_upper_bound_7, 8 : pixel_red_upper_bound_8, 9 : pixel_red_upper_bound_9, 10 : pixel_red_upper_bound_10,
            11 : pixel_red_upper_bound_11, 12 : pixel_red_upper_bound_12
            }


RED_LOWERS = {
            1 : pixel_red_lower_bound_1, 2 : pixel_red_lower_bound_2, 3 : pixel_red_lower_bound_3, 4 : pixel_red_lower_bound_4, 5 : pixel_red_lower_bound_5, 
            6 : pixel_red_lower_bound_6, 7 : pixel_red_lower_bound_7, 8 : pixel_red_lower_bound_8, 9 : pixel_red_lower_bound_9, 10 : pixel_red_lower_bound_10,
            11 : pixel_red_lower_bound_11, 12 : pixel_red_lower_bound_12
            }

GREEN_UPPERS = {
            1 : pixel_green_upper_bound_1, 2 : pixel_green_upper_bound_2, 3 : pixel_green_upper_bound_3, 4 : pixel_green_upper_bound_4, 5 : pixel_green_upper_bound_5, 
            6 : pixel_green_upper_bound_6, 7 : pixel_green_upper_bound_7, 8 : pixel_green_upper_bound_8, 9 : pixel_green_upper_bound_9, 10 : pixel_green_upper_bound_10,
            11 : pixel_green_upper_bound_11, 12 : pixel_green_upper_bound_12
            }
GREEN_LOWERS = {
            1 : pixel_green_lower_bound_1, 2 : pixel_green_lower_bound_2, 3 : pixel_green_lower_bound_3, 4 : pixel_green_lower_bound_4, 5 : pixel_green_lower_bound_5, 
            6 : pixel_green_lower_bound_6, 7 : pixel_green_lower_bound_7, 8 : pixel_green_lower_bound_8, 9 : pixel_green_lower_bound_9, 10 : pixel_green_lower_bound_10,
            11 : pixel_green_lower_bound_11, 12 : pixel_green_lower_bound_12
            }

BLUE_UPPERS = {
            1 : pixel_blue_upper_bound_1, 2 : pixel_blue_upper_bound_2, 3 : pixel_blue_upper_bound_3, 4 : pixel_blue_upper_bound_4, 5 : pixel_blue_upper_bound_5, 
            6 : pixel_blue_upper_bound_6, 7 : pixel_blue_upper_bound_7, 8 : pixel_blue_upper_bound_8, 9 : pixel_blue_upper_bound_9, 10 : pixel_blue_upper_bound_10,
            11 : pixel_blue_upper_bound_11, 12 : pixel_blue_upper_bound_12
            }

BLUE_LOWERS = {
            1 : pixel_blue_lower_bound_1, 2 : pixel_blue_lower_bound_2, 3 : pixel_blue_lower_bound_3, 4 : pixel_blue_lower_bound_4, 5 : pixel_blue_lower_bound_5, 
            6 : pixel_blue_lower_bound_6, 7 : pixel_blue_lower_bound_7, 8 : pixel_blue_lower_bound_8, 9 : pixel_blue_lower_bound_9, 10 : pixel_blue_lower_bound_10,
            11 : pixel_blue_lower_bound_11, 12 : pixel_blue_lower_bound_12
            }

CONSISTENCIES = {
                1 : consistency_1, 2 : consistency_2, 3 : consistency_3, 4 : consistency_4, 5 : consistency_5, 6 : consistency_6, 7 : consistency_7, 8 : consistency_8,
                9 : consistency_9, 10 : consistency_10, 11 : consistency_11, 12 : consistency_12
                }