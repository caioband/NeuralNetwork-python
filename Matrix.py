
'''
example matrix: matrix = [
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12]
                        ]
'''
class Matrix:

    def __init__(self, rows=0, cols=0,matrix=[]):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix

    def __printMatrix__(self):
        Row = self.rows
        Column = self.cols
        print(Row, Column)
        for row in range(self.rows):
            for column in range(self.cols):
                print(self.matrix[row][column], end=" ")
            print()
    def __debugMatrix__(self):
        row = 0
        col = 0
        for row in range(self.rows):
            for column in range(self.cols):
                col +=1
                print(row, col)
            row +=1