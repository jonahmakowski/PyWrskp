import pyWrkspPackage

def find_gaurd(data):
    """
    Finds the coordinates of the guard in the given 2D list.

    Args:
        data (list of list of str): A 2D list representing the grid where each element is a string.

    Returns:
        tuple: A tuple (x, y) representing the coordinates of the guard.

    Raises:
        Exception: If no guard is found in the grid.
    """
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "^":
                return x, y
    raise Exception("No gaurd found")

def mainloop(data: list, direc: tuple):
    """
    Executes the main loop logic for processing the data based on the given direction.

    Args:
        data (list): A 2D list representing the grid or map.
        direc (tuple): A tuple representing the current direction (dirx, diry).

    Returns:
        tuple: A tuple containing the updated data and direction.

    Raises:
        Exception: If the data contains an invalid character.
    """
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
    """
    Counts the number of occurrences of the character 'X' in a 2D list.

    Args:
        data (list of list of str): A 2D list where each element is a string.

    Returns:
        int: The count of 'X' characters found in the 2D list.
    """
    value = 1
    for row in data:
        for item in row:
            if item == "X":
                value += 1
    return value

def main():
    """
    Main function to execute the puzzle logic.
    This function performs the following steps:
    1. Loads data from the file "input.txt" using the pyWrkspPackage.
    2. Splits the data into lines and converts each line into a list of characters.
    3. Prints the initial state of the data.
    4. Calls the mainloop function to process the data and update the direction.
    5. Prints the updated state of the data.
    6. Continuously calls the mainloop function to process the data until an IndexError occurs.
    7. Prints the updated state of the data after each iteration.
    8. Returns the count of a specific condition in the data.
    Returns:
        int: The count of a specific condition in the data.
    """
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
