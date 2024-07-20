import random


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[0 for _ in range(width)] for _ in range(height)]

    def generate(self):
        # Start with a grid full of walls
        for i in range(self.height):
            for j in range(self.width):
                self.maze[i][j] = 1

        # Create a starting point
        start_x, start_y = 1, 1
        self.maze[start_y][start_x] = 0
        stack = [(start_x, start_y)]

        while stack:
            current_x, current_y = stack.pop()
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                next_x, next_y = current_x + dx*2, current_y + dy*2

                if 0 <= next_x < self.width and 0 <= next_y < self.height and self.maze[next_y][next_x] == 1:
                    self.maze[next_y][next_x] = 0
                    self.maze[current_y + dy][current_x + dx] = 0
                    stack.append((next_x, next_y))

        # Set start and finish
        self.start = (1, 1)
        self.finish = (self.width - 2, self.height - 2)
        self.maze[self.finish[1]][self.finish[0]] = 0

    def make_str(self):
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                if (j, i) == self.start:
                    output += "S"
                elif (j, i) == self.finish:
                    output += "F"
                elif self.maze[i][j] == 1:
                    output += "█"
                else:
                    output += " "
            output += "\n"
        return output

    def __str__(self):
        return self.make_str()

    def open_path(self, direction, location):
        if self.maze[direction[0] + location[0]][direction[1] + location[1]] == 1:
            return False
        else:
            return True

    def brute_force_solve(self):
        cur_pos_x = self.start[0]
        cur_pos_y = self.start[1]
        cur_direction = None
        options = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        choices = []
        # Each choice will get a dictionary {'location': (x,y), 'direction':(x,y), 'possible':[(x,y)], 'explored':[(x,y)]}
        while True:


# Generate and print the maze
maze = Maze(201, 201)  # Odd dimensions to ensure walls on all sides
maze.generate()
print(maze)