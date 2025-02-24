# Documentation for src/helpfulPackage/app/pyWrkspPackage/variable_management.py

**Python Script Documentation**

**Summary**
-----------

This script provides a set of utility functions for various tasks, including dictionary merging, list chunking, flattening, environment variable loading, and matrix creation. These functions can be used to simplify and standardize code in data processing and manipulation applications.

**Functions and Classes**
-------------------------

### dict_merge

*   **Description:** Merges two dictionaries recursively. If a key in both dictionaries has a dictionary as its value,
    the function will merge those dictionaries as well. Otherwise, the value from the second dictionary
    will overwrite the value from the first dictionary.
*   **Parameters:**
    *   `d1` (dict): The first dictionary to merge.
    *   `d2` (dict): The second dictionary to merge.
*   **Returns:** A merged dictionary.

### chunk_list

*   **Description:** Splits a list into smaller lists (chunks) of a specified size.
*   **Parameters:**
    *   `lst` (list): The list to be split into chunks.
    *   `size` (int): The size of each chunk.
*   **Returns:** A list of lists, where each sublist is a chunk of the original list.

### flatten

*   **Description:** Flattens a list of lists into a single list.
*   **Parameters:**
    *   `lst` (list): A list of lists to be flattened.
*   **Returns:** A single flattened list containing all the elements of the sublists.

### load_from_env

*   **Description:** Load the value of an environment variable from a .env file and retrieve its value.
*   **Parameters:**
    *   `variable` (str): The name of the environment variable to retrieve.
*   **Returns:** The value of the specified environment variable as a string.

### list_to_str

*   **Description:** Converts a list of items into a single string with each item separated by a specified separator.
*   **Parameters:**
    *   `list` (list): The list of items to be converted to a string.
    *   `sep` (str, optional): The separator to be used between items. Defaults to an empty string.
*   **Returns:** A single string with all items from the list separated by the specified separator.

### make_matrix

*   **Description:** Creates a matrix (2D list) with the specified number of rows and columns.
*   **Parameters:**
    *   `rows` (int): The number of rows in the matrix.
    *   `cols` (int): The number of columns in the matrix.
    *   `default` (optional): The default value to fill the matrix with. Defaults to None.
*   **Returns:** A 2D list representing a matrix with the specified number of rows and columns.

### recursive_copy

*   **Description:** Recursively copies a list of lists.
*   **Parameters:**
    *   `lst` (list): The list to be copied. This can be a nested list.
*   **Returns:** A new list that is a deep copy of the input list.

**Dependencies**
-----------------

This script depends on the following external packages/modules:

*   `dotenv`: Used for loading environment variables from a .env file.
*   `os`: Used for accessing and manipulating environment variables.
*   `copy`: Used for creating a deep copy of nested lists.
*   `load_dotenv` (from `dotenv`): Used to load the `.env` file.

**Code**
------

```python
# Import necessary modules
from dotenv import load_dotenv
import os
import copy

# Function to merge two dictionaries recursively
def dict_merge(d1: dict, d2: dict) -> dict:
    """
    Merges two dictionaries recursively. If a key in both dictionaries has a dictionary as its value,
    the function will merge those dictionaries as well. Otherwise, the value from the second dictionary
    will overwrite the value from the first dictionary.

    Args:
        d1 (dict): The first dictionary to merge.
        d2 (dict): The second dictionary to merge.

    Returns:
        dict: The merged dictionary.
    """
    for key, value in d2.items():
        if isinstance(value, dict) and key in d1 and isinstance(d1[key], dict):
            # Recursively merge the dictionaries
            dict_merge(d1[key], value)
        else:
            # Overwrite values from the first dictionary with those from the second dictionary
            d1[key] = value
    return d1

# Function to chunk a list into smaller lists of a specified size
def chunk_list(lst: list, size: int) -> list:
    """
    Splits a list into smaller lists (chunks) of a specified size.

    Args:
        lst (list): The list to be split into chunks.
        size (int): The size of each chunk.

    Returns:
        list: A list of lists, where each sublist is a chunk of the original list.
              The last chunk may be smaller if the original list size is not
              perfectly divisible by the chunk size.

    Example:
        >>> chunk_list([1, 2, 3, 4], 2)
        [[1, 2], [3, 4]]
    """
    return [lst[i:i + size] for i in range(0, len(lst), size)]

# Function to flatten a list of lists into a single list
def flatten(lst: list) -> list:
    """
    Flattens a list of lists into a single list.

    Args:
        lst (list): A list of lists to be flattened.

    Returns:
        list: The flattened list.
    """
    return [item for sublist in lst for item in sublist]

# Function to load the value of an environment variable from a .env file
def load_from_env(variable: str) -> str:
    """
    Load the value of an environment variable from a .env file and retrieve its value.

    Args:
        variable (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the specified environment variable.
    """
    # Assume that you have a .env file with the following content
    # VARIABLE=variable_value
    return os.environ.get(variable, None)

# Function to convert a list of items into a single string with each item separated by a separator
def list_to_str(lst: list, sep: str = '') -> str:
    """
    Converts a list of items into a single string with each item separated by a specified separator.

    Args:
        lst (list): The list of items to be converted to a string.
        sep (str, optional): The separator to use between items. Defaults to an empty string.

    Returns:
        str: The resulting string.
    """
    return sep.join(map(str, lst))

# Function to create a matrix (2D list) with the specified number of rows and columns
def make_matrix(rows: int, cols: int, default_value=None) -> list:
    """
    Creates a matrix (2D list) with the specified number of rows and columns.

    Args:
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        default_value (optional): The default value to fill the matrix with. Defaults to None.

    Returns:
        list: A 2D list representing a matrix with the specified number of rows and columns.
    """
    return [[default_value for _ in range(cols)] for _ in range(rows)]

# Function to recursively copy a nested list
def recursive_copy(lst) -> list:
    """
    Recursively copies a list of lists.

    Args:
        lst (list): The list to be copied. This can be a nested list.

    Returns:
        list: A new list that is a deep copy of the input list.
    """
    if isinstance(lst, list):
        return [recursive_copy(item) for item in lst]
    elif isinstance(lst, tuple):
        return recursive_copy(list(lst))
    else:
        return lst
```

**Example Usage**
-----------------

```python
# Create a sample dictionary to merge
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge the dictionaries using dict_merge
merged_dict = dict_merge(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Chunk a list of numbers into smaller lists of size 2
numbers = [1, 2, 3, 4, 5, 6]
chunked_list = chunk_list(numbers, 2)
print(chunked_list)  # Output: [[1, 2], [3, 4], [5, 6]]

# Flatten a list of lists
nested_list = [[1, 2], [3, 4]]
flattened_list = flatten(nested_list)
print(flattened_list)  # Output: [1, 2, 3, 4]

# Load an environment variable using load_from_env
environment_variable_name = 'VARIABLE'
variable_value = load_from_env(environment_variable_name)
print(variable_value)

# Convert a list of items into a string with each item separated by a separator
items = ['apple', 'banana', 'cherry']
separator = ', '
result_string = list_to_str(items, sep=separator)
print(result_string)  # Output: apple, banana, cherry

# Create a matrix (2D list) with the specified number of rows and columns
matrix_rows = 3
matrix_cols = 4
default_value = 0
matrix = make_matrix(matrix_rows, matrix_cols, default_value)
print(matrix)  # Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Recursively copy a nested list using recursive_copy
nested_list = [1, 2, [3, 4]]
copied_list = recursive_copy(nested_list)
print(copied_list)  # Output: [1, 2, [3, 4]]
```