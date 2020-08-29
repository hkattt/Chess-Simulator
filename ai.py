# AI CLASS

class AI():
    def __init__(self, colour, game):
        self.colour = colour
        self.game = game
        if self.colour == "W":
            self.turn = True
        else:
            self.turn = False

    def move(self):
        pass