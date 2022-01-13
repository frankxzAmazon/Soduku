class Board:
    def _init__(self,row:int=9,column:int=9):
        self.cells=[[0 for _ in range(row)] for _ in range(row)]
    
    def is_valid_soduku_with_number_at_this_pos(self,position,number):
        if self.cells[position[0]][position[1]]!=0: return False
        for x in range(self.length):
            if self.cells[x][position[1]]==number:
                return False
        for x in range(9):
            if self.cells[position[0]][x]==number:
                return False
        row_section=position[0]//3
        column_section=position[1]//3
        for x in range(3):
            for y in range(3):
                if self.cells[row_section*3+x][column_section*3+y]==number:
                    return False
        return True
