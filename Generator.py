from typing import Generator


import random
from board import Board
class Generator:
  
    def generate(self,board:Board,number_of_filled_cells:int):
        for _ in range(number_of_filled_cells):
            row,column,number=self.generate_row_col_num(board)
            while not board.is_valid_to_fill_number_at_this_pos(row,column,number):
                row,column,number=self.generate_row_col_num(board)
            board.cells[row][column]=number      

    def generate_row_col_num(self,board:Board):
        return random.randrange(board.row),random.randrange(board.column),random.randrange(1,10)

    