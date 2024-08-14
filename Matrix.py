
'''
example matrix: matrix = [
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12]
                        ]
'''
class Matrix:

    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.matrix = []

    def __printMatrix__(self):
        Row = self.rows
        Column = self.cols
        for row in range(Row):
            for column in range(Column):
                print(self.matrix[row][column], end=" ")
            print()