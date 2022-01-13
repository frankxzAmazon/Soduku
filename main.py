import random

# the sudoku grid

# +-------+-------+-------+
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |    #The classic Sudoku game involves a grid of 81 squares.
# +-------+-------+-------+    # The grid is divided into nine blocks, each containing nine squares.
# | 0 0 0 | 0 0 0 | 0 0 0 |    # The rules of the game are simple:
# | 0 0 0 | 0 0 0 | 0 0 0 |       # each of the nine blocks has to contain all the numbers 1-9 within its squares.
# | 0 0 0 | 0 0 0 | 0 0 0 |       # Each number can only appear once in a row, column or box.
# +-------+-------+-------+       # The difficulty lies in that each vertical nine-square column,
# | 0 0 0 | 0 0 0 | 0 0 0 |       # or horizontal nine-square line across, within the larger square,
# | 0 0 0 | 0 0 0 | 0 0 0 |       # must also contain the numbers 1-9, without repetition or omission.
# | 0 0 0 | 0 0 0 | 0 0 0 |    # Every puzzle has just one correct solution.
# +-------+-------+-------+

#option to choose the difficulty level

def get_filled_cell(difficulty_level:str):
    if difficulty_level=="1":
        return 32
    if difficulty_level=="2":
        return 16
    if difficulty_level=="3":
        return 8
    return "incorrect difficulty level"

def get_difficulty_level():
    print("Level of Difficulty: ")
    print("        1.Beginner")
    print("        2.Intermediate")
    print("        3.Advanced")
    print()
    print("Enter the level of difficulty: ")
    difficulty_level=input()
    if difficulty_level not in (["1","2","3"]):
        print("you must enter 1 or 2 or 3")
        exit()
    return get_filled_cell(difficulty_level)

def generate_empty_board():
    return [[0 for _ in range(9)] for _ in range(9)]


def is_valid_soduku(board:list[list],row:int,column:int,number:int):
    for x in range(9):
        if board[x][column]==number:
            return False
    for x in range(9):
        if board[row][x]==number:
            return False
    row_section=row//3
    column_section=column//3
    for x in range(3):
        for y in range(3):
            if board[row_section*3+x][column_section*3+y]==number:
                return False
    return True

def generate_row_col_num():
    return random.randrange(9),random.randrange(9),random.randrange(1,10)

def cannot_fill_numbert_at_this_position(board,row,column,number):
    return board[row][column]!=0 or is_valid_soduku(board,row,column,number)==False

def generate_soduku(board):
    for _ in range(number_of_filled_cells):
        row,column,number=generate_row_col_num()
        while cannot_fill_numbert_at_this_position(row,column,number):
            row,column,number=generate_row_col_num()
        board[row][column]=number


def print_board(board:list[list]):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("-------------------")
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print("|",end="")
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ",end="")

# if __name__=="__main__":
     

def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return i,j
    return False



def solver(board):
    if find_empty_cell(board):
        row,column=find_empty_cell(board)
    else:
        return True
    for i in range(1,10):
        if is_valid_soduku(board,row,column,i):
            board[row][column]=i
            if solver(board):
                return True
            board[row][column]=0
    return False

if __name__ == "__main__":

    print("solution\n")
    solver(board)
    print_board(board) 








