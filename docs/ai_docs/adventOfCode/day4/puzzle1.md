# Documentation for src/adventOfCode/day4/puzzle1.py

# pyWrkspPackage Documentation
=====================================

## Summary

This script is designed to process a 2D grid of characters, performing various checks on the grid's structure and content. It uses the `pyWrkspPackage` library to load data from a file.

The script performs three main tasks:

1. Counts the number of specific horizontal combinations in each line.
2. Transposes the grid and processes each column using the same horizontal combination counting function.
3. Checks for the presence of the sequence 'XMAS' in all four diagonal directions of the grid.

## Functions and Classes

### `custom_chunk(lis)`

*   Description: Splits a list into chunks of 4 characters.
*   Parameters:
    *   `lis`: A list of characters to be split into chunks of 4.
*   Returns:
    *   A list of lists where each inner list contains 4 characters.

### `do_horizontal(line)`

*   Description: Counts the number of specific horizontal combinations in a given line.
*   Parameters:
    *   `line`: A string representing the line to be checked.
*   Returns:
    *   An integer representing the number of times the specified combinations appear in the line.

### `do_vertical(data)`

*   Description: Transposes the given 2D list and processes each column using the `do_horizontal` function.
*   Parameters:
    *   `data`: A 2D list where each inner list represents a row of characters.
*   Returns:
    *   An integer representing the total amount calculated by applying the `do_horizontal` function to each column of the transposed matrix.

### `do_diagnals(data)`

*   Description: Counts the number of times the diagonal sequence 'XMAS' appears in the given 2D list.
*   Parameters:
    *   `data`: A 2D list representing the grid of characters.
*   Returns:
    *   An integer representing the number of times the diagonal sequence 'XMAS' appears in the grid.

### `main()`

*   Description: Main function to process the input data and calculate the total amount.
*   Parameters: None
*   Returns:
    *   An integer representing the total calculated amount.

## Dependencies

The script depends on the following external package:

*   `pyWrkspPackage`: A library for working with Python, used to load data from a file.

```python
import pyWrkspPackage

def custom_chunk(lis):
    """
    Splits a list into chunks of 4 characters.

    Args:
        lis (list of str): A list of characters to be split into chunks of 4.

    Returns:
        list of list of str: A list of lists where each inner list contains 4 characters.
    """
    # Code implementation
    chunks = []
    for i in range(0, len(lis)):
        chunks.append(lis[i:i+4])
    return chunks

def do_horizontal(line):
    """
    Counts the number of specific horizontal combinations in a given line.

    Args:
        line (str): A string representing the line to be checked.

    Returns:
        int: The number of times the specified combinations appear in the line.
    """
    # Code implementation
    combos = [['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']]
    splits = custom_chunk(list(line))

    amount = 0
    for split in splits:
        if split in combos:
            amount += 1

    return amount

def do_vertical(data):
    """
    Transposes the given 2D list `data` and processes each column using the `do_horizontal` function.
    Args:
        data (list of list of str): A 2D list where each inner list represents a row of characters.
    Returns:
        int: The total amount calculated by applying the `do_horizontal` function to each column of the transposed matrix.
    """
    # Code implementation
    verts = pyWrkspPackage.make_matrix(len(data), len(data))
    for index, row in enumerate(data):
        for char_index, char in enumerate(row):
            verts[index][char_index] = char

    amount = 0
    for col in range(len(verts[0])):
        line = [vert[col] for vert in verts]
        amount += do_horizontal(''.join(line))

    return amount

def do_diagnals(data):
    """
    Counts the number of times the diagonal sequence 'XMAS' appears in the given 2D list.
    Args:
        data (list of list of str): A 2D list representing the grid of characters.
    Returns:
        int: The number of times the diagonal sequence 'XMAS' appears in the grid.
    """
    # Code implementation
    amount = 0

    for i in range(len(data)):
        for j in range(i, len(data[0])):
            if data[i][j] == 'X' and data[j][i] == 'M' and data[i][j+1] == 'A' and data[j+1][i] == 'S':
                amount += 1
            elif data[i][j] == 'S' and data[j][i] == 'A' and data[i][j+1] == 'M' and data[j+1][i] == 'X':
                amount += 1

    return amount

def main():
    """
    Main function to process the input data and calculate the total amount.
    Returns:
        int: The total calculated amount.
    """
    # Code implementation
    data = pyWrkspPackage.load_from_file("input.txt").split('\n')
    
    amount = 0
    
    for line in data:
        amount += do_horizontal(line)
    
    amount += do_vertical(data)
    
    amount += do_diagnals(data)

    return amount

print(main())
```