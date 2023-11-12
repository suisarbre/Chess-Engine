

#this class keeps update of the game state
class GameState():
    def __init__(self):
        #2d list of board
        #the first letter b->Black, w->White
        #the second letter R->Rook N->Knight, B->Bishop
        #Q-> Queen, K->King, p -> pawn
        #-- means empty space
        self.board =[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            
            ["--","--","--","--","--","--","--","--"],
            
            ["--","--","--","--","--","--","--","--"],
            
            ["--","--","--","--","--","--","--","--"],
            
            ["--","--","--","--","--","--","--","--"],
            
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        #Turn flag
        self.whiteToMove = True
        #keeps the log
        self.moveLog = []