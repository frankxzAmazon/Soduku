import random
from board import Board
from generator import Generator
from solver import Solver

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


def main():
    number_of_filled_cells=get_difficulty_level()
    # number_of_filled_cells=32
    board=Board()
    generator=Generator()
    generator.generate(board,number_of_filled_cells)
    board.print_board()
    solver=Solver()
    solver.solve_soduku(board)
    print("solution\n")
    board.print_board()




if __name__ == "__main__":
    main()









