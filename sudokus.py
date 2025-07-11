
class Sudoku:
    def __init__(self, rowList:list):
        self.data = []
        for i in range(9):
            self.data.append(rowList[i])

    def row(self, rowNum:int):
        return self.data[rowNum]
    
    def column(self, colNum:int):
        col = []
        for i in range(9):
            tmp = self.row(i)
            col.append(self.row(i)[colNum])
        return col
    
    def subGrid(self, gridNum:int):
        row = int(gridNum/3) * 3
        col = (gridNum % 3) * 3
        subGrid = []
        for i in range(3):
            for j in range(3):
                subGrid.append(self.row(row+i)[col+j])
        return subGrid
    

class Checker:
    def __init__(self, sudoku:Sudoku):
        self.sudoku = sudoku
    
    def checkList(self, list):
        if len(list) != 9:
            return False
        for i in range(9):
            if i+1 in list:
                list.remove(i+1)
            else:
                return False
        return True
    
    def checkRows(self):
        for i in range(9):
            if not(self.checkList(self.sudoku.row(i))):
                return False
        return True
    
    def checkColumns(self):
        for i in range(9):
            if not(self.checkList(self.sudoku.column(i))):
                return False
        return True
            
    def checkGrids(self):
        for i in range(9):
            if not(self.checkList(self.sudoku.subGrid(i))):
                return False
        return True
            
    def check(self):
        if self.checkRows() and self.checkColumns() and self.checkGrids():
            return True
        return False

