from board import Board
class Solver:




    def solve_soduku(self,board):
        if board.empty_cell_exists():
            row,column=board.empty_cell_exists()
        else:
            return True
        for i in range(1,10):
            if board.is_valid_to_fill_number_at_this_pos(row,column,i):
                board.cells[row][column]=i
                if self.solve_soduku(board):
                    return True
                board.cells[row][column]=0
        return False