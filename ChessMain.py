


import pygame as pg
import ChessEngine

pg.init()

#These are constants
WIDTH = HEIGHT = 512
DIMENTION = 8
SQ_SIZE = HEIGHT // DIMENTION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","bp","wR","wN","wB","wQ","wK","wB","wN","wR","wp"]
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))
        
def main():
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    
    while running:#game loop
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        pg.display.flip()

#Graphics
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

#Draws squares
def drawBoard(screen):
    colors = [pg.Color("white"),pg.Color("gray")]
    for r in range(DIMENTION):
        for c in range(DIMENTION):
            color = colors[(r+c)%2]
            pg.draw.rect(screen,color,pg.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    
#Draws pieces based on the gamestate
def drawPieces(screen,board):
    for r in range(DIMENTION):
        for c in range(DIMENTION):
            piece = board[r][c]
            if piece != "--": #if the board is not empty
                screen.blit(IMAGES[piece],pg.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
                
    

if __name__ == "__main__":
    main()