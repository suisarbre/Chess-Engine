

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
        
    #takes Move class as a parameter, won't do castling and en passant
    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove #swap turns
        
    #Undo the last move based on self.moveLog
    def undoMove(self):
        if self.moveLog:
            lastMove = self.moveLog.pop() #returns the last element of the list
            self.board[lastMove.endRow][lastMove.endCol] = lastMove.pieceCaptured
            self.board[lastMove.startRow][lastMove.startCol] = lastMove.pieceMoved
            self.whiteToMove = not self.whiteToMove
        

    
class Move():
    #maps keys to values
    #key : value
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,
                   "5":3,"6":2,"7":1,"8":0}
    rowsToRanks = {v:k for k, v in ranksToRows.items()}
    filesToCols = {"a":0,"b":1,"c":2,"d":3,
                   "e":4,"f":5,"g":6,"h":7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    
    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
    
    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)
    
    
    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]