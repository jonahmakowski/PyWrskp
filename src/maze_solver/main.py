import random
import time


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[0 for _ in range(width)] for _ in range(height)]
        self.options = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.start = ()
        self.finish = ()

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

    def make_str(self, lis=None):
        if lis is None:
            lis = self.maze
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                if (j, i) == self.start:
                    output += "S"
                elif (j, i) == self.finish:
                    output += "F"
                elif lis[i][j] == 1:
                    output += "█"
                elif lis[i][j] == 2:
                    output += "●"
                else:
                    output += " "
            output += "\n"
        return output

    def __str__(self):
        return self.make_str()

    def open_path(self, direction, location):
        if self.maze[direction[1] + location[1]][direction[0] + location[0]] == 1:
            return False
        else:
            return True

    def plot_solved(self, path):
        result = self.maze.copy()
        for x, y in path:
            if (x, y) != self.start and (x, y) != self.finish:
                result[y][x] = 2  # 2 represents the solution path
        return result

    def dfs_solve(self):
        stack = [(self.start[0], self.start[1], [])]
        visited = set()
        steps = 0

        while stack:
            x, y, path = stack.pop()
            steps += 1

            if (x, y) == self.finish:
                return steps, self.plot_solved(path + [(x, y)])

            if (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in self.options:
                    next_x, next_y = x + dx, y + dy
                    if self.open_path((dx, dy), (x, y)) and (next_x, next_y) not in visited:
                        stack.append((next_x, next_y, path + [(x, y)]))

        print(f"No solution found after {steps} steps.")
        return False

    def plot_current_path(self, path):
        # Reset all path markers
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 2:
                    self.maze[y][x] = 0

        # Plot the current path
        for x, y in path:
            if (x, y) != self.start and (x, y) != self.finish:
                self.maze[y][x] = 2  # 2 represents the current path

    def print_maze_state(self):
        # Print newlines to push old output off screen
        print("\n" * 50)
        print(self)

    def visual_dfs_solve(self, delay=0.5):
        stack = [(self.start[0], self.start[1], [])]
        visited = set()
        steps = 0

        while stack:
            x, y, path = stack.pop()
            steps += 1

            if (x, y) == self.finish:
                self.plot_current_path(path + [(x, y)])
                self.print_maze_state()
                print(f"Maze solved in {steps} steps!")
                return True

            if (x, y) not in visited:
                visited.add((x, y))
                self.plot_current_path(path + [(x, y)])
                self.print_maze_state()
                print(f"Step: {steps}")
                time.sleep(delay)

                for dx, dy in self.options:
                    next_x, next_y = x + dx, y + dy
                    if self.open_path((dx, dy), (x, y)) and (next_x, next_y) not in visited:
                        stack.append((next_x, next_y, path + [(x, y)]))

        print("No solution found.")
        return False



# Generate and print the maze
maze = Maze(301, 301)  # Odd dimensions to ensure walls on all sides
maze.generate()
print(maze)
steps_taken, path_lis = maze.dfs_solve()
print(maze.make_str(lis=path_lis))
print(steps_taken)
