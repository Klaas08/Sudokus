
class sudoku:
    def __init__(self, rowList):
        self.data = rowList

    def row(self, rowNum):
        return self.data[rowNum]
    
    def column(self, colNum):
        col = []
        for i in range(10):
            col.append(self.row(i)[colNum])
        return col
    
    def subGrid(self, gridNum):
        row = int(gridNum/3) * 3
        col = (gridNum % 3) * 3
        subGrid = []
        for i in range(3):
            subGrid.append(self.row(row+i)[col:col+3])
        return subGrid
    
