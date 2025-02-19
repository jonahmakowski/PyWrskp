local math = require("math")

-- Utility function to create a 2D array
local function create2DArray(width, height, value)
    local arr = {}
    for i = 1, height do
        arr[i] = {}
        for j = 1, width do
            arr[i][j] = value
        end
    end
    return arr
end

-- Maze class
local Maze = {}
Maze.__index = Maze

function Maze.new(width, height)
    local self = setmetatable({}, Maze)
    self.width = width
    self.height = height
    self.maze = create2DArray(width, height, 1)
    self.options = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
    self.start = {}
    self.finish = {}
    return self
end

function Maze:generate()
    -- Start with a grid full of walls
    for i = 1, self.height do
        for j = 1, self.width do
            self.maze[i][j] = 1
        end
    end

    -- Create a starting point
    local start_x, start_y = 2, 2
    self.maze[start_y][start_x] = 0
    local stack = {{start_x, start_y}}

    while #stack > 0 do
        local current = table.remove(stack)
        local current_x, current_y = current[1], current[2]
        local directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
        
        -- Shuffle directions
        for i = #directions, 2, -1 do
            local j = math.random(i)
            directions[i], directions[j] = directions[j], directions[i]
        end

        for _, dir in ipairs(directions) do
            local dx, dy = dir[1], dir[2]
            local next_x, next_y = current_x + dx*2, current_y + dy*2

            if next_x > 0 and next_x <= self.width and next_y > 0 and next_y <= self.height and self.maze[next_y][next_x] == 1 then
                self.maze[next_y][next_x] = 0
                self.maze[current_y + dy][current_x + dx] = 0
                table.insert(stack, {next_x, next_y})
            end
        end
    end

    -- Set start and finish
    self.start = {2, 2}
    self.finish = {self.width - 1, self.height - 1}
    self.maze[self.finish[2]][self.finish[1]] = 0
end

function Maze:makeStr(lis)
    lis = lis or self.maze
    local output = ""
    for i = 1, self.height do
        for j = 1, self.width do
            if j == self.start[1] and i == self.start[2] then
                output = output .. "S"
            elseif j == self.finish[1] and i == self.finish[2] then
                output = output .. "F"
            elseif lis[i][j] == 1 then
                output = output .. "█"
            elseif lis[i][j] == 2 then
                output = output .. "●"
            else
                output = output .. " "
            end
        end
        output = output .. "\n"
    end
    return output
end

function Maze:__tostring()
    return self:makeStr()
end

function Maze:openPath(direction, location)
    return self.maze[direction[2] + location[2]][direction[1] + location[1]] ~= 1
end

function Maze:plotSolved(path)
    local result = {}
    for i = 1, #self.maze do
        result[i] = {}
        for j = 1, #self.maze[i] do
            result[i][j] = self.maze[i][j]
        end
    end

    for _, point in ipairs(path) do
        local x, y = point[1], point[2]
        if (x ~= self.start[1] or y ~= self.start[2]) and (x ~= self.finish[1] or y ~= self.finish[2]) then
            result[y][x] = 2  -- 2 represents the solution path
        end
    end
    return result
end

function Maze:dfsSolve()
    local stack = {{self.start[1], self.start[2], {}}}
    local visited = {}
    local steps = 0

    while #stack > 0 do
        local current = table.remove(stack)
        local x, y, path = current[1], current[2], current[3]
        steps = steps + 1

        if x == self.finish[1] and y == self.finish[2] then
            table.insert(path, {x, y})
            return steps, self:plotSolved(path)
        end

        if not visited[y .. "," .. x] then
            visited[y .. "," .. x] = true
            for _, option in ipairs(self.options) do
                local dx, dy = option[1], option[2]
                local next_x, next_y = x + dx, y + dy
                if self:openPath({dx, dy}, {x, y}) and not visited[next_y .. "," .. next_x] then
                    local newPath = {}
                    for _, p in ipairs(path) do
                        table.insert(newPath, p)
                    end
                    table.insert(newPath, {x, y})
                    table.insert(stack, {next_x, next_y, newPath})
                end
            end
        end
    end

    print("No solution found after " .. steps .. " steps.")
    return false
end

-- Generate and print the maze
local maze = Maze.new(11, 11)  -- Odd dimensions to ensure walls on all sides
maze:generate()
print(maze)
local steps_taken, path_lis = maze:dfsSolve()
print(maze:makeStr(path_lis))
print(steps_taken)