from PIL import Image

class Piece():
    def __init__(self, square_x, square_y, colour, piece_type):
        self.square_y = square_y # (pixel width(0,40))
        self.square_x = square_x
        self.colour = colour # (B or W)
        self.piece_type = piece_type # (K, Q, Kn, R, B, P)


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

#-------------------------------------------#
 
for i in range (60, 540, 60): #Checking through each individually
    for j in range(60, 540, 60): #Checking through each individually
        exit = False
        for x in range(i - 60, i, 5):
            for y in range(j - 60, j, 5):   


#-------------------------------------------------------- pawn_white ---------------- piece_1 ----------------------------------------------------------#

                image = Image.open("C:/Users/Harry/Desktop/Code V3/py.png") #make sure using forward slashes.
                image_rgb = image.convert("RGB")
                pixel_red, pixel_green, pixel_blue = image_rgb.getpixel((x,y))
    
                if pixel_red <= pixel_red_upper_bound_1 and pixel_red >= pixel_red_lower_bound_1:
                    if pixel_green <= pixel_green_upper_bound_1 and pixel_green >= pixel_green_lower_bound_1:
                        if pixel_blue <= pixel_blue_upper_bound_1 and pixel_blue >= pixel_blue_lower_bound_1:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_1: 
                                consistency_1 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_1:
                                consistency_1 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_1:
                                consistency_1 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_1:
                                consistency_1 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_1: 
                                consistency_1 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_1:
                                consistency_1 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_1:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_1:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_1:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_1:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_1:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_1:
                                                   consistency_1 = True

                            if consistency_1 == True:
                                pieces.append(Piece(i, j, "w", "white_pawn"))
                                exit = True
                                break
                            
                            if consistency_1 == False:
                                print("stinky")

#-------------------------------------------------------- pawn_black ---------------- piece_2 ----------------------------------------------------------#

                if pixel_red <= pixel_red_upper_bound_2 and pixel_red >= pixel_red_lower_bound_2:
                    if pixel_green <= pixel_green_upper_bound_2 and pixel_green >= pixel_green_lower_bound_2:
                        if pixel_blue <= pixel_blue_upper_bound_2 and pixel_blue >= pixel_blue_lower_bound_2:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_2: 
                                consistency_2 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_2:
                                consistency_2 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_2:
                                consistency_2 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_2:
                                consistency_2 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_2: 
                                consistency_2 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_2:
                                consistency_2 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_2:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_2:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_2:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_2:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_2:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_2:
                                                   consistency_2 = True

                            if consistency_2 == True:
                                pieces.append(Piece(i, j, "b", "black_pawn"))
                                exit = True
                                break
                            
                            if consistency_2 == False:
                                print("stinky")

#-------------------------------------------------------- rook_white ---------------- piece_3 ----------------------------------------------------------#                                

                if pixel_red <= pixel_red_upper_bound_3 and pixel_red >= pixel_red_lower_bound_3:
                    if pixel_green <= pixel_green_upper_bound_3 and pixel_green >= pixel_green_lower_bound_3:
                        if pixel_blue <= pixel_blue_upper_bound_3 and pixel_blue >= pixel_blue_lower_bound_3:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_3: 
                                consistency_3 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_3:
                                consistency_3 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_3:
                                consistency_3 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_3:
                                consistency_3 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_3: 
                                consistency_3 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_3:
                                consistency_3 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_3:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_3:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_3:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_3:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_3:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_3:
                                                   consistency_3 = True

                            if consistency_3 == True:
                                pieces.append(Piece(i, j, "w", "white_rook"))
                                exit = True
                                break
                            
                            if consistency_3 == False:
                                print("stinky")

#-------------------------------------------------------- rook_black ---------------- piece_4 ----------------------------------------------------------#     

                if pixel_red <= pixel_red_upper_bound_4 and pixel_red >= pixel_red_lower_bound_4:
                    if pixel_green <= pixel_green_upper_bound_4 and pixel_green >= pixel_green_lower_bound_4:
                        if pixel_blue <= pixel_blue_upper_bound_4 and pixel_blue >= pixel_blue_lower_bound_4:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_4: 
                                consistency_4 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_4:
                                consistency_4 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_4:
                                consistency_4 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_4:
                                consistency_4 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_4: 
                                consistency_4 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_4:
                                consistency_4 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_4:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_4:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_4:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_4:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_4:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_4:
                                                   consistency_4 = True

                            if consistency_4 == True:
                                pieces.append(Piece(i, j, "b", "black_rook"))
                                exit = True
                                break
                            
                            if consistency_4 == False:
                                print("stinky")

#-------------------------------------------------------- bishop_white ---------------- piece_5 ----------------------------------------------------------#     

                if pixel_red <= pixel_red_upper_bound_5 and pixel_red >= pixel_red_lower_bound_5:
                    if pixel_green <= pixel_green_upper_bound_5 and pixel_green >= pixel_green_lower_bound_5:
                        if pixel_blue <= pixel_blue_upper_bound_5 and pixel_blue >= pixel_blue_lower_bound_5:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_5: 
                                consistency_5 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_5:
                                consistency_5 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_5:
                                consistency_5 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_5:
                                consistency_5 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_5: 
                                consistency_5 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_5:
                                consistency_5 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_5:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_5:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_5:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_5:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_5:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_5:
                                                   consistency_5 = True

                            if consistency_5 == True:
                                pieces.append(Piece(i, j, "w", "bishop_white"))
                                exit = True
                                break
                            
                            if consistency_5 == False:
                                print("stinky")

#-------------------------------------------------------- bishop_black ---------------- piece_6 ----------------------------------------------------------#     

                if pixel_red <= pixel_red_upper_bound_6 and pixel_red >= pixel_red_lower_bound_6:
                    if pixel_green <= pixel_green_upper_bound_6 and pixel_green >= pixel_green_lower_bound_6:
                        if pixel_blue <= pixel_blue_upper_bound_6 and pixel_blue >= pixel_blue_lower_bound_6:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_6: 
                                consistency_6 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_6:
                                consistency_6 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_6:
                                consistency_6 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_6:
                                consistency_6 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_6: 
                                consistency_6 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_6:
                                consistency_6 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_6:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_6:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_6:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_6:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_6:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_6:
                                                   consistency_6 = True

                            if consistency_6 == True:
                                pieces.append(Piece(i, j, "b", "bishop_black"))
                                exit = True
                                break
                            
                            if consistency_6 == False:
                                print("stinky")

#-------------------------------------------------------- knight_white ---------------- piece_7 ----------------------------------------------------------#     

                if pixel_red <= pixel_red_upper_bound_7 and pixel_red >= pixel_red_lower_bound_7:
                    if pixel_green <= pixel_green_upper_bound_7 and pixel_green >= pixel_green_lower_bound_7:
                        if pixel_blue <= pixel_blue_upper_bound_7 and pixel_blue >= pixel_blue_lower_bound_7:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_7: 
                                consistency_7 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_7:
                                consistency_7 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_7:
                                consistency_7 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_7:
                                consistency_7 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_7: 
                                consistency_7 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_7:
                                consistency_7 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_7:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_7:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_7:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_7:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_7:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_7:
                                                   consistency_7 = True

                            if consistency_7 == True:
                                pieces.append(Piece(i, j, "w", "knight_white"))
                                exit = True
                                break
                            
                            if consistency_7 == False:
                                print("stinky")

#-------------------------------------------------------- knight_black ---------------- piece_8 ----------------------------------------------------------#   

                if pixel_red <= pixel_red_upper_bound_8 and pixel_red >= pixel_red_lower_bound_8:
                    if pixel_green <= pixel_green_upper_bound_8 and pixel_green >= pixel_green_lower_bound_8:
                        if pixel_blue <= pixel_blue_upper_bound_8 and pixel_blue >= pixel_blue_lower_bound_8:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_8: 
                                consistency_8 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_8:
                                consistency_8 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_8:
                                consistency_8 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_8:
                                consistency_8 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_8: 
                                consistency_8 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_8:
                                consistency_8 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_8:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_8:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_8:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_8:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_8:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_8:
                                                   consistency_8 = True

                            if consistency_8 == True:
                                pieces.append(Piece(i, j, "b", "knight_black"))
                                exit = True
                                break
                            
                            if consistency_8 == False:
                                print("stinky")

#-------------------------------------------------------- king_white ---------------- piece_9 ----------------------------------------------------------#   

                if pixel_red <= pixel_red_upper_bound_9 and pixel_red >= pixel_red_lower_bound_9:
                    if pixel_green <= pixel_green_upper_bound_9 and pixel_green >= pixel_green_lower_bound_9:
                        if pixel_blue <= pixel_blue_upper_bound_9 and pixel_blue >= pixel_blue_lower_bound_9:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_9: 
                                consistency_9 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_9:
                                consistency_9 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_9:
                                consistency_9 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_9:
                                consistency_9 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_9: 
                                consistency_9 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_9:
                                consistency_9 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_9:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_9:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_9:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_9:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_9:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_9:
                                                   consistency_9 = True

                            if consistency_9 == True:
                                pieces.append(Piece(i, j, "w", "king_white"))
                                exit = True
                                break
                            
                            if consistency_9 == False:
                                print("stinky")

#-------------------------------------------------------- king_black ---------------- piece_10 ----------------------------------------------------------#     

                if pixel_red <= pixel_red_upper_bound_10 and pixel_red >= pixel_red_lower_bound_10:
                    if pixel_green <= pixel_green_upper_bound_10 and pixel_green >= pixel_green_lower_bound_10:
                        if pixel_blue <= pixel_blue_upper_bound_10 and pixel_blue >= pixel_blue_lower_bound_10:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_10: 
                                consistency_10 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_10:
                                consistency_10 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_10:
                                consistency_10 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_10:
                                consistency_10 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_10: 
                                consistency_10 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_10:
                                consistency_10 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_10:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_10:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_10:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_10:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_10:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_10:
                                                   consistency_10 = True

                            if consistency_10 == True:
                                pieces.append(Piece(i, j, "b", "king_black"))
                                exit = True
                                break
                            
                            if consistency_10 == False:
                                print("stinky")

#-------------------------------------------------------- queen_white ---------------- piece_11 ----------------------------------------------------------#     

                if pixel_red <= pixel_red_upper_bound_11 and pixel_red >= pixel_red_lower_bound_11:
                    if pixel_green <= pixel_green_upper_bound_11 and pixel_green >= pixel_green_lower_bound_11:
                        if pixel_blue <= pixel_blue_upper_bound_11 and pixel_blue >= pixel_blue_lower_bound_11:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_11: 
                                consistency_11 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_11:
                                consistency_11 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_11:
                                consistency_11 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_11:
                                consistency_11 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_11: 
                                consistency_11 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_11:
                                consistency_11 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_11:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_11:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_11:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_11:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_11:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_11:
                                                   consistency_11 = True

                            if consistency_11 == True:
                                pieces.append(Piece(i, j, "w", "queen_white"))
                                exit = True
                                break
                            
                            if consistency_11 == False:
                                print("stinky")

#-------------------------------------------------------- queen_black ---------------- piece_12 ----------------------------------------------------------#     

                if pixel_red <= pixel_red_upper_bound_12 and pixel_red >= pixel_red_lower_bound_12:
                    if pixel_green <= pixel_green_upper_bound_12 and pixel_green >= pixel_green_lower_bound_12:
                        if pixel_blue <= pixel_blue_upper_bound_12 and pixel_blue >= pixel_blue_lower_bound_12:
                    
                            failsafe_check_forward_red, failsafe_check_forward_green, failsafe_check_forward_blue = image_rgb.getpixel((x + 1,y + 1))
                            failsafe_check_backward_red, failsafe_check_backward_green, failsafe_check_backward_blue = image_rgb.getpixel((x - 1,y - 1))

                            if failsafe_check_backward_red and failsafe_check_forward_red > pixel_red_upper_bound_12: 
                                consistency_12 = False
                            if failsafe_check_backward_red and failsafe_check_forward_red < pixel_red_lower_bound_12:
                                consistency_12 = False
                            if failsafe_check_backward_green and failsafe_check_forward_green > pixel_green_upper_bound_12:
                                consistency_12 = False
                            if failsafe_check_backward_green and failsafe_check_forward_red < pixel_green_lower_bound_12:
                                consistency_12 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_blue > pixel_blue_upper_bound_12: 
                                consistency_12 = False
                            if failsafe_check_backward_blue and failsafe_check_forward_red < pixel_blue_lower_bound_12:
                                consistency_12 = False
                            
                            if failsafe_check_backward_red and failsafe_check_forward_red <= pixel_red_upper_bound_12:
                                if failsafe_check_backward_green and failsafe_check_forward_green <= pixel_green_upper_bound_12:
                                    if failsafe_check_backward_blue and failsafe_check_forward_blue <= pixel_blue_upper_bound_12:
                                        if failsafe_check_backward_red and failsafe_check_forward_red >= pixel_red_lower_bound_12:
                                            if failsafe_check_backward_green and failsafe_check_forward_green >= pixel_green_lower_bound_12:
                                               if failsafe_check_backward_blue and failsafe_check_forward_blue >= pixel_blue_lower_bound_12:
                                                   consistency_12 = True

                            if consistency_12 == True:
                                pieces.append(Piece(i, j, "b", "queen_black"))
                                exit = True
                                break
                            
                            if consistency_12 == False:
                                print("stinky")


            if exit:
                break

print(len(pieces))
for piece in pieces:
    print(piece.piece_type)
    print(piece.square_x)
    print(piece.square_y)