from board import Board
from generator import Generator
from solver import Solver


def get_filled_cell(difficulty_level:str):
    if difficulty_level=="1":
        return 20
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
    # number_of_filled_cells=15
    solver=Solver()
    generator=Generator()
    
    board=Board()
    generator.generate(board,number_of_filled_cells)
    while not solver.is_sovlable(board):
        board=Board()
        generator.generate(board,number_of_filled_cells)


    board.print_board()
    print("solution\n")
    solver.solve_soduku(board)
    board.print_board()





if __name__ == "__main__":
    main()









