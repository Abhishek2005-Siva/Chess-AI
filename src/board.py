from const import *
from square import Square
from piece import *

class Board:
    def __init__(self):
        self.squares=[[0,0,0,0,0,0,0,0]for col in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row,col)

    def _add_pieces(self,color):
        row_pawn,row_other=(6,7) if color=='white' else (1,0)

        #pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn,col,Pawn(color)) # type: ignore
        #knights
        self.squares[row_other][1] = Square(row_pawn,1,Knight(color)) # type: ignore
        self.squares[row_other][6] = Square(row_pawn,6,Knight(color)) # type: ignore
        #bishops
        self.squares[row_other][2] = Square(row_pawn,2,Bishop(color)) # type: ignore
        self.squares[row_other][5] = Square(row_pawn,5,Bishop(color)) # type: ignore
        #rook
        self.squares[row_other][0] = Square(row_pawn,0,Rook(color)) # type: ignore
        self.squares[row_other][7] = Square(row_pawn,7,Rook(color)) # type: ignore
        #queen
        self.squares[row_other][3] = Square(row_pawn,3,Queen(color)) # type: ignore
        #King
        self.squares[row_other][4] = Square(row_pawn,4,King(color)) # type: ignore