from board import Board
import copy
class Solver:




    def solve_soduku(self,board):
        
        empty_cell=board.empty_cell_exists()
        if empty_cell:
            row,column=empty_cell
        else:
            return True
        for i in range(1,10):
            if board.is_valid_to_fill_number_at_this_pos(row,column,i):
                board.cells[row][column]=i
                if self.solve_soduku(board):
                    return True
                else:
                    board.cells[row][column]=0
        return False
    
    def is_sovlable(self,board:Board):
        board_copy=copy.deepcopy(board)
        if self.solve_soduku(board_copy): return True
        return False