import pyWrkspPackage

def find_gaurd(data):
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "^":
                return x, y
    raise Exception("No gaurd found")

def mainloop(data: list, direc: tuple):
    x, y = find_gaurd(data)
    dirx, diry = direc
    if data[y+diry][x+dirx] == "." or data[y+diry][x+dirx] == "X":
        data[y][x] = "X"
        data[y+diry][x+dirx] = "^"
        return data, direc
    if data[y+diry][x+dirx] == "#":
        if direc == (0, -1):
            direc = (1, 0)
        elif direc == (1, 0):
            direc = (0, 1)
        elif direc == (0, 1):
            direc = (-1, 0)
        else:
            direc = (0, -1)
        return data, direc
    raise Exception("Invalid data")

def count(data):
    value = 1
    for row in data:
        for item in row:
            if item == "X":
                value += 1
    return value

def main():
    data = pyWrkspPackage.load_from_file("input.txt").split("\n")
    data = [list(item) for item in data]
    for point in data: print(*point)
    data, direc = mainloop(data, (0, -1))
    for point in data: print(*point)
    while True:
        try:
            print()
            data, direc = mainloop(data, direc)
            for point in data: print(*point)
        except IndexError:
            break
    
    return count(data)

if __name__ == "__main__":
    print(main())
