# Documentation for src/helpfulPackage/app/pyWrkspPackage/variable_management.py

**Script Documentation**

**Summary**
------------

This Python script provides various utility functions for data manipulation, environment variable management, and matrix creation. It includes functions for merging dictionaries, splitting lists into chunks, flattening lists, loading environment variables from a `.env` file, converting lists to strings, creating matrices with specified dimensions, and recursively copying nested lists.

**Functions and Classes**
------------------------

### Functions

#### `dict_merge(d1: dict, d2: dict) -> dict`

Merges two dictionaries recursively. If a key in both dictionaries has a dictionary as its value,
the function will merge those dictionaries as well. Otherwise, the value from the second dictionary
will overwrite the value from the first dictionary.

*   **Args:** `d1 (dict)`: The first dictionary to merge.
*   `d2 (dict)`: The second dictionary to merge.
*   **Returns:** `dict`: The merged dictionary.

#### `chunk_list(lst: list, size: int) -> list`

Splits a list into smaller lists (chunks) of a specified size.

*   **Args:** `lst (list)`: The list to be split into chunks.
*   `size (int)`: The size of each chunk.
*   **Returns:** `list`: A list of lists, where each sublist is a chunk of the original list.

#### `flatten(lst: list) -> list`

Flattens a list of lists into a single list.

*   **Args:** `lst (list)`: A list of lists to be flattened.
*   **Returns:** `list`: A single flattened list containing all the elements of the sublists.

#### `load_from_env(variable: str) -> str`

Loads the value of an environment variable from a `.env` file.

*   **Args:** `variable (str)`: The name of the environment variable to retrieve.
*   **Returns:** `str`: The value of the specified environment variable as a string.

#### `list_to_str(list, sep='') -> str`

Converts a list of items into a single string with each item separated by a specified separator.

*   **Args:** `list (list)`: The list of items to be converted to a string.
*   `sep (str, optional)`: The separator to be used between items. Defaults to an empty string.
*   **Returns:** `str`: A single string with all items from the list separated by the specified separator.

#### `make_matrix(rows: int, cols: int, default=None) -> list`

Creates a matrix (2D list) with the specified number of rows and columns.

*   **Args:** `rows (int)`: The number of rows in the matrix.
*   `cols (int)`: The number of columns in the matrix.
*   `default (optional)`: The default value to fill the matrix with. Defaults to None.
*   **Returns:** `list`: A 2D list representing a matrix with the specified number of rows and columns.

#### `recursive_copy(lst: list) -> list`

Recursively copies a list of lists.

*   **Args:** `lst (list)`: The list to be copied. This can be a nested list.
*   **Returns:** `list`: A new list that is a deep copy of the input list.

**Dependencies**
---------------

This script depends on the following external packages/modules:

*   `dotenv`: A Python library for loading environment variables from a `.env` file.
*   `os`: A built-in Python module for interacting with the operating system and accessing environment variables.
*   `copy`: A built-in Python module for deep copying lists.

**Code**
------

```python
# Import required modules
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
            dict_merge(d1[key], value)
        else:
            d1[key] = value
    return d1

# Function to split a list into smaller lists (chunks) of a specified size
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

# Function to flatten a list of lists
def flatten(lst: list) -> list:
    """
    Flattens a list of lists into a single list.

    Args:
        lst (list): A list of lists to be flattened.

    Returns:
        list: A single flattened list containing all the elements of the sublists.
    """
    return [item for sublist in lst for item in sublist]

# Function to load an environment variable from a .env file
def load_from_env(variable: str) -> str:
    """
    Loads the value of an environment variable from a .env file.

    Args:
        variable (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the specified environment variable as a string.
    """
    with open('.env', 'r') as env_file:
        lines = env_file.readlines()
    return [line.strip() for line in lines if line.startswith(variable + '=')][0].split('=')[1]

# Function to convert a list of items into a single string
def list_to_str(lst: list, sep='') -> str:
    """
    Converts a list of items into a single string with each item separated by a specified separator.

    Args:
        lst (list): The list of items to be converted to a string.
        sep (str, optional): The separator to be used between items. Defaults to an empty string.

    Returns:
        str: A single string with all items from the list separated by the specified separator.
    """
    return sep.join(map(str, lst))

# Function to create a matrix (2D list) with specified dimensions
def make_matrix(rows: int, cols: int, default=None) -> list:
    """
    Creates a matrix (2D list) with specified dimensions.

    Args:
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        default (optional): The default value to fill the matrix with. Defaults to None.

    Returns:
        list: A 2D list representing a matrix with the specified number of rows and columns.
    """
    return [[default] * cols for _ in range(rows)]

# Function to recursively copy a list of lists
def recursive_copy(lst: list) -> list:
    """
    Recursively copies a list of lists.

    Args:
        lst (list): The list to be copied. This can be a nested list.

    Returns:
        list: A new list that is a deep copy of the input list.
    """
    return [recursive_copy(item) if isinstance(item, list) else item for item in lst]
```

Note that this code snippet only includes the functions and their documentation comments as per your request. The actual usage and implementation details may vary based on the specific requirements and context.