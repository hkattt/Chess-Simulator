
# importing files
from settings import *

# importing required modules
from PIL import Image

class Chess_Piece():
    def __init__(self, square_x, square_y, colour, symbol):
        self.square_y = square_y # (pixel width(0,40))
        self.square_x = square_x
        self.colour = colour # (B or W)
        self.symbol = symbol # (K, Q, Kn, R, B, P)

def board_from_img(image):
    """ Creates a board matrix from an image """
    pieces = [] #list of pieces

    # empty board matrix
    board = [[".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]]

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
                                    
                                    if failsafe_check_backward_red and failsafe_check_forward_red > RED_UPPERS[piece_index]: 
                                        CONSISTENCIES[piece_index] = False
                                    if failsafe_check_backward_red and failsafe_check_forward_red < RED_LOWERS[piece_index]:
                                        CONSISTENCIES[piece_index] = False
                                    if failsafe_check_backward_green and failsafe_check_forward_green > GREEN_UPPERS[piece_index]:
                                        CONSISTENCIES[piece_index] = False
                                    if failsafe_check_backward_green and failsafe_check_forward_red < GREEN_LOWERS[piece_index]:
                                        CONSISTENCIES[piece_index] = False
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue > BLUE_UPPERS[piece_index]: 
                                        CONSISTENCIES[piece_index] = False
                                    if failsafe_check_backward_blue and failsafe_check_forward_red < BLUE_LOWERS[piece_index]:
                                        CONSISTENCIES[piece_index] = False
                                    
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
                                            pieces.append(Chess_Piece(i, j, "W", "P"))
                                        elif piece_index == 2:
                                            pieces.append(Chess_Piece(i, j, "B", "P"))
                                        elif piece_index == 3:
                                            pieces.append(Chess_Piece(i, j, "W", "R"))
                                        elif piece_index == 4:
                                            pieces.append(Chess_Piece(i, j, "B", "R"))
                                        elif piece_index == 5:
                                            pieces.append(Chess_Piece(i, j, "W", "B"))
                                        elif piece_index == 6:
                                            pieces.append(Chess_Piece(i, j, "B", "B"))
                                        elif piece_index == 7:
                                            pieces.append(Chess_Piece(i, j, "W", "Kn"))
                                        elif piece_index == 8:
                                            pieces.append(Chess_Piece(i, j, "B", "Kn"))
                                        elif piece_index == 9:
                                            pieces.append(Chess_Piece(i, j, "W", "K"))
                                        elif piece_index == 10:
                                            pieces.append(Chess_Piece(i, j, "B", "K"))
                                        elif piece_index == 11:
                                            pieces.append(Chess_Piece(i, j, "W", "Q"))
                                        elif piece_index == 12:
                                            pieces.append(Chess_Piece(i, j, "B", "Q"))
                                        exit = True
                                        break
                                    # failed the failsafe
                                    if CONSISTENCIES[piece_index] == False:
                                        pass
                if exit:
                    break

    # adding pieces to the board matrix
    for x in range(0, 8):
        for y in range(0, 8):
            for piece in pieces:
                if (piece.square_x // 60) - 1 == x and (piece.square_y // 60) - 1 == y:
                    board[y][x] = piece.colour + piece.symbol
    return board

IMAGES = {1 : Image.open("C:/Users/hugok/Desktop/School Work/Gungahlin College/Robotics/Term 3/Hugo-Kat-Pygame-Chess/1.png"), 
        2 : Image.open("C:/Users/hugok/Desktop/School Work/Gungahlin College/Robotics/Term 3/Hugo-Kat-Pygame-Chess/2.png"), 
        3 : Image.open("C:/Users/hugok/Desktop/School Work/Gungahlin College/Robotics/Term 3/Hugo-Kat-Pygame-Chess/3.png"), 
        4 : Image.open("C:/Users/hugok/Desktop/School Work/Gungahlin College/Robotics/Term 3/Hugo-Kat-Pygame-Chess/4.png"), 
        5 : Image.open("C:/Users/hugok/Desktop/School Work/Gungahlin College/Robotics/Term 3/Hugo-Kat-Pygame-Chess/5.png"), 
        6 : Image.open("C:/Users/hugok/Desktop/School Work/Gungahlin College/Robotics/Term 3/Hugo-Kat-Pygame-Chess/test_img.png")}

image = IMAGES[5]
board = board_from_img(image)
print("")
for row in board:
    print(row)
print("")