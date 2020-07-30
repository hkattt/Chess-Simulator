# PIECE CLASSES

class Piece():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class King(Piece):
    def __init__(self, x, y):
        super().__init__(x, y):
        