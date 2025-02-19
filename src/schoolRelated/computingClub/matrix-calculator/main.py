class Matrix:
    def __init__(self, matrix=None, size_x=None, size_y=None):
        self.matrix = matrix if matrix is not None else self.gen_matrix(size_x, size_y)
        self.length_row = len(self.matrix[0])
        self.length_col = len(self.matrix)
    def get_location(self, x, y):
        return self.matrix[y][x]
    def set_position(self, x, y, data):
        self.matrix[y][x] = data
    def get_row(self, row):
        return self.matrix[row]
    def get_col(self, col):
        col_result = []
        for row in self.matrix:
            col_result.append(row[col])
    def invert(self):
        result = []
        for col in range(self.length_col):
            result.append(self.get_col(col))
        return result
    @staticmethod
    def gen_matrix(size_x, size_y):
        row = []
        for _ in range(size_x):
            row.append(0)
        result = []
        for _ in range(size_y):
            result.append(row.copy())

def add(matrix:Matrix, value:float):
    result_matrix = Matrix(size_x=matrix.length_row, size_y=matrix.length_col)
    for row in range(matrix.length_col):
        for col in range(matrix.length_row):
            result_matrix.set_position(col, row, matrix.get_location(col, row) + value)
    return result_matrix
