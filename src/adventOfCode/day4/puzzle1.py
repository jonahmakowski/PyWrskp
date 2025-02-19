import pyWrkspPackage

def custom_chunk(lis):
    """
    Splits a list into chunks of 4 characters.

    Args:
        lis (list of str): A list of characters to be split into chunks of 4.

    Returns:
        list of list of str: A list of lists where each inner list contains 4 characters.
    """
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
    verts = pyWrkspPackage.make_matrix(len(data), len(data))
    for index, row in enumerate(data):
        for char_index, char in enumerate(row):
            verts[char_index][index] = char
    
    amount = 0

    for coloumn in verts:
        amount += do_horizontal(coloumn)
    
    return amount

def do_diagnals(data):
    """
    Counts the number of times the diagonal sequence 'XMAS' appears in the given 2D list.

    The function checks for the sequence 'XMAS' in all four diagonal directions:
    - Top-left to bottom-right
    - Bottom-right to top-left
    - Top-right to bottom-left
    - Bottom-left to top-right

    Args:
        data (list of list of str): A 2D list representing the grid of characters.

    Returns:
        int: The number of times the diagonal sequence 'XMAS' appears in the grid.
    """
    amount = 0
    for index, row in enumerate(data):
        for char_index, char in enumerate(row):
            if char == 'X':
                if index + 3 < len(data) and char_index + 3 < len(row) and data[index+1][char_index+1] == 'M' and data[index+2][char_index+2] == 'A' and data[index+3][char_index+3] == 'S':
                    amount += 1
                if index - 3 >= 0 and char_index - 3 >= 0 and data[index-1][char_index-1] == 'M' and data[index-2][char_index-2] == 'A' and data[index-3][char_index-3] == 'S':
                    amount += 1
                if index + 3 < len(data) and char_index - 3 >= 0 and data[index+1][char_index-1] == 'M' and data[index+2][char_index-2] == 'A' and data[index+3][char_index-3] == 'S':
                    amount += 1
                if index - 3 >= 0 and char_index + 3 < len(row) and data[index-1][char_index+1] == 'M' and data[index-2][char_index+2] == 'A' and data[index-3][char_index+3] == 'S':
                    amount += 1
    return amount

def main():
    """
    Main function to process the input data and calculate the total amount.
    This function performs the following steps:
    1. Loads data from the file "input.txt" using the pyWrkspPackage.
    2. Splits the data into lines.
    3. Initializes the amount to 0.
    4. Iterates through each line and adds the result of do_horizontal(line) to the amount.
    5. Adds the result of do_vertical(data) to the amount.
    6. Adds the result of do_diagnals(data) to the amount.
    Returns:
        int: The total calculated amount.
    """
    data = pyWrkspPackage.load_from_file("input.txt").split('\n')
    
    amount = 0
    
    for line in data:
        amount += do_horizontal(line)
    
    amount += do_vertical(data)
    
    amount += do_diagnals(data)

    return amount

print(main())
