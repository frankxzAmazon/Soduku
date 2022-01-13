# from functools import lru_cache
class Board:
    def __init__(self,row:int=9,column:int=9):
        self.row=row
        self.column=column
        self.cells=[[0 for _ in range(row)] for _ in range(row)]
    
    def is_valid_to_fill_number_at_this_pos(self,row,column,number):
        if self.cells[row][column]!=0: return False
        for x in range(self.row):
            if self.cells[x][column]==number:
                return False
        for x in range(self.column):
            if self.cells[row][x]==number:
                return False
        row_section=row//3
        column_section=column//3
        for x in range(3):
            for y in range(3):
                if self.cells[row_section*3+x][column_section*3+y]==number:
                    return False
        return True
    
    def print_board(self):
        for i in range(self.row):
            if i%3==0 and i!=0:
                print("-------------------")
            for j in range(self.column):
                if j%3==0 and j!=0:
                    print("|",end="")
                if j==8:
                    print(self.cells[i][j])
                else:
                    print(str(self.cells[i][j])+" ",end="")
    # @lru_cache()
    def empty_cell_exists(self):
        for i in range(self.row):
            for j in range(self.column):
                if self.cells[i][j]==0:
                    return i,j
        return False
