from board import Board
class Solver:
    def find_empty_cell(self,board:Board):
        for i in range(board.row):
            for j in range(board.column):
                if board.cells[i][j]==0:
                    return i,j
        return False



    def solve_soduku(self,board):
        if self.find_empty_cell(board):
            row,column=self.find_empty_cell(board)
        else:
            return True
        for i in range(1,10):
            if board.is_valid_to_fill_number_at_this_pos(row,column,i):
                board.cells[row][column]=i
                if self.solve_soduku(board):
                    return True
                board.cells[row][column]=0
        return False