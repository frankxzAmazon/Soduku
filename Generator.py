from typing import Generator


import random
from Board import Board
class Generator:
    def generate(board:Board，number_of_filled_cells:int):
        for _ in range(number_of_filled_cells):
            row,column,number=generate_row_col_num()
            while cannot_fill_numbert_at_this_position(row,column,number):
                row,column,number=generate_row_col_num()
            board[row][column]=number        
    
    def generate_row_col_num(board:Board):
        return random.randrange(board.length),random.randrange(9),random.randrange(1,10)

    