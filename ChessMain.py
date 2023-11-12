


import pygame as pg
import ChessEngine

pg.init()

#These are constants
WIDTH = HEIGHT = 512
DIMENTION = 8
SQ_SIZE = HEIGHT // DIMENTION
MAX_FPS
IMAGES = {}


def loadImages():
    pieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","bp"]
    pieces += ["wR","wN","wB","wQ","wK","wB","wN","wR","wp"]
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"),SQ_SIZE,SQ_SIZE)
        
def main():
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs = ChessEngine.GameState()