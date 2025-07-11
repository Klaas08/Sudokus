from sudokus import Sudoku, Checker

test = Sudoku([[1,2,3,4,5,6,7,8,9],
               [2,3,4,5,6,7,8,9,1],
               [3,4,5,6,7,8,9,1,2],
               [4,5,6,7,8,9,1,2,3],
               [5,6,7,8,9,1,2,3,4],
               [6,7,8,9,1,2,3,4,5],
               [7,8,9,1,2,3,4,5,6],
               [8,9,1,2,3,4,5,6,7],
               [9,1,2,3,4,5,6,7,8]])

checker = Checker(test)

print(checker.check())