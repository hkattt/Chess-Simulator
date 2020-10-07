from PIL import Image

class Piece():
    def __init__(self, square_x, square_y, colour, symbol):
        self.square_y = square_y # (pixel width(0,40))
        self.square_x = square_x
        self.colour = colour # (B or W)
        self.symbol = symbol # (K, Q, Kn, R, B, P)


pieces = [] #list of pieces

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

# loads in the image 
image = Image.open("C:/Users/hugok/Desktop/School Work/Gungahlin College/Robotics/Term 3/Hugo-Kat-Pygame-Chess/test_img.png") #make sure using forward slashes.
image_rgb = image.convert("RGB")


for i in range (60, 540, 60): #Checking through each individually
    for j in range(60, 540, 60): #Checking through each individually
        exit = False
        for x in range(i - 60, i, 5):
            for y in range(j - 60, j, 5):
                       
                pixel_red, pixel_green, pixel_blue = image_rgb.getpixel((x, y)) # RGB value at (x, y) on the image
                
                # iterates over all of the possible piece colours
                for piece_index in range(1, 13):

                    if pixel_red <= RED_UPPERS[piece_index] and pixel_red >= RED_LOWERS[piece_index]:
                        if pixel_green <= GREEN_UPPERS[piece_index] and pixel_green >= GREEN_LOWERS[piece_index]:
                            if pixel_blue <= BLUE_UPPERS[piece_index] and pixel_blue >= BLUE_LOWERS[piece_index]:
                        
                                failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                                failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                                # seems to work without this section; however, kept it here incase I missed something
                                """
                                if failsafe_check_backward_red and failsafe_check_forward_red > red_uppers[piece_index]: 
                                    consistencies[piece_index] = False
                                if failsafe_check_backward_red and failsafe_check_forward_red < red_lowers[piece_index]:
                                    consistencies[piece_index] = False
                                if failsafe_check_backward_green and failsafe_check_forward_green > green_uppers[piece_index]:
                                    consistencies[piece_index] = False
                                if failsafe_check_backward_green and failsafe_check_forward_red < green_lowers[piece_index]:
                                    consistencies[piece_index] = False
                                if failsafe_check_backward_blue and failsafe_check_forward_blue > blue_uppers[piece_index]: 
                                    consistencies[piece_index] = False
                                if failsafe_check_backward_blue and failsafe_check_forward_red < blue_lowers[piece_index]:
                                    consistencies[piece_index] = False
                                """
                                
                                if failsafe_check_backward_red and failsafe_check_forward_red <= RED_UPPERS[piece_index]:
                                    if failsafe_check_backward_green and failsafe_check_forward_green <= GREEN_UPPERS[piece_index]:
                                        if failsafe_check_backward_blue and failsafe_check_forward_blue <= BLUE_UPPERS[piece_index]:
                                            if failsafe_check_backward_red and failsafe_check_forward_red >= RED_LOWERS[piece_index]:
                                                if failsafe_check_backward_green and failsafe_check_forward_green >= GREEN_LOWERS[piece_index]:
                                                    if failsafe_check_backward_blue and failsafe_check_forward_blue >= BLUE_LOWERS[piece_index]:
                                                        CONSISTENCIES[piece_index] = True

                                # passed the failsafe
                                if CONSISTENCIES[piece_index]:
                                    # creates a piece corresponding to the current piece index
                                    if piece_index == 1:
                                        pieces.append(Piece(i, j, "W", "P"))
                                    elif piece_index == 2:
                                        pieces.append(Piece(i, j, "B", "P"))
                                    elif piece_index == 3:
                                        pieces.append(Piece(i, j, "W", "R"))
                                    elif piece_index == 4:
                                        pieces.append(Piece(i, j, "B", "R"))
                                    elif piece_index == 5:
                                        pieces.append(Piece(i, j, "W", "B"))
                                    elif piece_index == 6:
                                        pieces.append(Piece(i, j, "B", "B"))
                                    elif piece_index == 7:
                                        pieces.append(Piece(i, j, "W", "Kn"))
                                    elif piece_index == 8:
                                        pieces.append(Piece(i, j, "B", "Kn"))
                                    elif piece_index == 9:
                                        pieces.append(Piece(i, j, "W", "K"))
                                    elif piece_index == 10:
                                        pieces.append(Piece(i, j, "B", "K"))
                                    elif piece_index == 11:
                                        pieces.append(Piece(i, j, "W", "Q"))
                                    elif piece_index == 12:
                                        pieces.append(Piece(i, j, "B", "Q"))
                                    exit = True
                                    break
                                # failed the failsafe
                                if CONSISTENCIES[piece_index] == False:
                                    print("stinky")
            if exit:
                break

board = [[".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]]

# adding pieces to the board array
for x in range(0, 8):
    for y in range(0, 8):
        for piece in pieces:
            if (piece.square_x // 60) - 1 == x and (piece.square_y // 60) - 1 == y:
                board[y][x] = piece.colour + piece.symbol

for row in board:
    print(row)