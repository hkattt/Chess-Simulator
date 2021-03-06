# CONTAINS TILE VALUES (for moves)

""" These move tiles have been adapted from the following source:
    https://github.com/devinalvaro/yachess/tree/master/src """

PAWN_TILES = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 1, 1, -2, -2, 1, 1, 0.5],
    [0.5, -0.5, -1, 2, 2, -1, -0.5, 0.5],
    [0, 0, 0, 4, 4, 0, 0, 0],
    [0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5],
    [1, 1, 2, 3, 3, 2, 1, 1],
    [5, 5, 5, 5, 5, 5, 5, 5],
    [0, 0, 0, 0, 0, 0, 0, 0]]

KNIGHT_TILES = [
    [-5, -4, -3, -3, -3, -3, -4, -5],
    [-4, -2, 0, 0.5, 0.5, 0, -2, -4],
    [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
    [-3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3],
    [-3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3],
    [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
    [-4, -2, 0, 0.5, 0.5, 0, -2, -4],
    [-5, -4, -3, -3, -3, -3, -4, -5]]

BISHOP_TILES = [
    [-2, -1, -1, -1, -1, -1, -1, -2],
    [-1, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, 0.5, 1, 1, 0.5, 0, -1],
    [-1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1],
    [-1, 0, 1, 1, 1, 1, 0, -1],
    [-1, 1, 1, 1, 1, 1, 1, -1],
    [-1, 0.5, 0, 0, 0, 0, 0.5, -1],
    [-2, -1, -1, -1, -1, -1, -1, -2]]

ROOK_TILES = [
    [-1, 0, 2, 3, 3, 2, 0, -1],
    [0.5, 1, 1, 1, 1, 1, 1, 0.5],
    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [0.5, 1, 1, 1, 1, 1, 1, 0.5],
    [-1, 0, 0, 3, 3, 0, 0, -1]]

QUEEN_TILES = [
    [-2, -1, -1, -0.5, -0.5, -1, -1, -2],
    [-1, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1],
    [-0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
    [0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
    [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1],
    [-1, 0, 0.5, 0, 0, 0, 0, -1],
    [-2, -1, -1, -0.5, -0.5, -1, -1, -2]]

KING_TILES = [
    [2, 3, 1, 0, 0, 1, 3, 2],
    [2, 2, -3, -4, -4, -3, 2, 2],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-2, -3, -3, -4, -4, -3, -3, -2],
    [-1, -2, -2, -2, -2, -2, -2, -1]]