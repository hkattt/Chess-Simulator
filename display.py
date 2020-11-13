# Display objects that are used to make the menu

# importing required modules
import pygame as pg
# importing required files
from settings import *

class Button():
    def __init__(self, colour, x, y, width, height, text, text_size, game):
        """Initiates button"""
        self.game = game
        self.colour = colour
        self.x = int(x - width / 2)
        self.y = int(y - height / 2)
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
    
    def draw(self, surface):
        """Draws the button onto the display window"""
        pg.draw.rect(surface, BLACK, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pg.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            self.game.write(self.text, BLACK, self.text_size, int(self.x + self.width / 2), int(self.y + self.height / 2))

    def mouse_over(self, position):
        """Checks if the mouse is over the button"""
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
        return False