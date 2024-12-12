class Piece:
    def __init__(self, matrix:list, position:tuple):
        self.matrix = matrix # In format of a 4x4 list, with 0s for unoccupided positions, and 1s for occupied
        self.position = position # The position of the top right of the matrix
    
    def rotate(self, direction:int): # Direction is either -1 or 1
        new_matrix = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        
        for y, row in enumerate(self.matrix):
            for x, value in enumerate(row):
                new_y = 3-x if direction == 1 else x
                new_x = y if direction == 1 else 3-y
                new_matrix[new_y][new_x] = value
        
        self.matrix = new_matrix.copy()
    
    def move_down(self):
        self.position = (self.position[0], self.position[1]+1)
    
    def move_left(self):
        self.position = (self.position[0]-1, self.position[1])
    
    def move_left(self):
        self.position = (self.position[0]-1, self.position[1])
    
    def extrapolate_positions(self):
        position_matrix = []
        for y, row in enumerate(self.matrix):
            position_matrix.append([])
            for x, value in enumerate(row):
                position_matrix[-1].append({'pos': (x+self.position[0], y+self.position[1]), 'value': value})

        return position_matrix

class Piece0(Piece):
    def __init__(self, position):
        matrix = [[0, 0, 1, 0],
                  [0, 0, 1, 0],
                  [0, 0, 1, 0],
                  [0, 0, 1, 0]]
        super().__init__(matrix, position)

class Piece1(Piece):
    def __init__(self, position):
        matrix = [[0, 1, 1, 0],
                  [0, 1, 1, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        super().__init__(matrix, position)

class Piece2(Piece):
    def __init__(self, position):
        matrix = [[0, 1, 0, 0],
                  [0, 1, 0, 0],
                  [0, 1, 1, 0],
                  [0, 0, 0, 0]]
        super().__init__(matrix, position)

class Piece3(Piece):
    def __init__(self, position):
        matrix = [[0, 1, 0, 0],
                  [0, 1, 1, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0]]
        super().__init__(matrix, position)

class Piece4(Piece):
    def __init__(self, position):
        matrix = [[0, 0, 1, 0],
                  [0, 0, 1, 0],
                  [0, 1, 1, 0],
                  [0, 0, 0, 0]]
        super().__init__(matrix, position)

class Piece5(Piece):
    def __init__(self, position):
        matrix = [[0, 0, 1, 0],
                  [0, 1, 1, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0]]
        super().__init__(matrix, position)

class Piece6(Piece):
    def __init__(self, position):
        matrix = [[0, 1, 0, 0],
                  [0, 1, 1, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 0]]
        super().__init__(matrix, position)
