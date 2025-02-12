# Documentation for src/helpfulPackage/app/pyWrkspPackage/file_management.py

**Python Script Documentation**

**Summary**
------------

This Python script provides a set of functions for reading and writing files, as well as handling JSON data. It includes functions for loading JSON files, writing dictionaries to JSON files, creating folders and checking if files exist.

**Functions and Classes**
-------------------------

### Functions

*   `load_from_file(file_path: str) -> str`:
    *   Reads the content of a file and returns it as a string.
    *   Args:
        *   `file_path (str)`: The path to the file to be read.
    *   Returns:
        *   `str`: The content of the file as a string.

*   `write_to_file(file_path: str, text: str) -> None`:
    *   Writes the given text to a file at the specified file path.
    *   Args:
        *   `file_path (str)`: The path to the file where the text will be written.
        *   `text (str)`: The text to write to the file.
    *   Returns:
        *   None

*   `append_to_file(file_path: str, text: str) -> None`:
    *   Appends the given text to the end of the specified file.
    *   Args:
        *   `file_path (str)`: The path to the file where the text will be appended.
        *   `text (str)`: The text to append to the file.
    *   Returns:
        *   None

*   `json_load_file(file_path: str) -> dict`:
    *   Loads a JSON file and returns its contents as a dictionary.
    *   Args:
        *   `file_path (str)`: The path to the JSON file to be loaded.
    *   Returns:
        *   `dict`: The contents of the JSON file as a dictionary.

*   `json_write_file(file_path: str, data: dict) -> None`:
    *   Writes a dictionary to a JSON file.
    *   Args:
        *   `file_path (str)`: The path to the file where the JSON data will be written.
        *   `data (dict)`: The dictionary to be written to the JSON file.
    *   Returns:
        *   None

*   `create_folders(path: str) -> None`:
    *   Creates a folder and all its parent directories if they do not exist.
    *   Args:
        *   `path (str)`: The path to the folder to be created.
    *   Returns:
        *   None

*   `file_exists(file_path: str) -> bool`:
    *   Checks if a file exists at the specified path.
    *   Args:
        *   `file_path (str)`: The path to the file to be checked.
    *   Returns:
        *   `bool`: True if the file exists, False otherwise.

**Classes**
------------

None

**Dependencies**
-----------------

*   `json` (built-in Python module)
*   `os` (built-in Python module)

```python
import json
import os

# Load content of a file and return it as a string.
def load_from_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    # Open the file in read mode.
    with open(file_path, 'r') as file:
        # Read the contents of the file and return it.
        return file.read()

# Write given text to a file at specified file path.
def write_to_file(file_path: str, text: str) -> None:
    """
    Writes the given text to a file at the specified file path.

    Args:
        file_path (str): The path to the file where the text will be written.
        text (str): The text to write to the file.

    Returns:
        None
    """
    # Open the file in write mode.
    with open(file_path, 'w') as file:
        # Write the given text to the file.
        file.write(text)

# Append given text to end of specified file.
def append_to_file(file_path: str, text: str) -> None:
    """
    Appends the given text to the end of the specified file.

    Args:
        file_path (str): The path to the file where the text will be appended.
        text (str): The text to append to the file.

    Returns:
        None
    """
    # Open the file in append mode.
    with open(file_path, 'a') as file:
        # Write the given text to the end of the file.
        file.write(text)

# Load JSON file and return its contents as a dictionary.
def json_load_file(file_path: str) -> dict:
    """
    Loads a JSON file and returns its contents as a dictionary.

    Args:
        file_path (str): The path to the JSON file to be loaded.

    Returns:
        dict: The contents of the JSON file as a dictionary.

    Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    # Open the file in read mode.
    with open(file_path, 'r') as file:
        # Load the JSON data from the file and return it.
        return json.load(file)

# Write dictionary to JSON file.
def json_write_file(file_path: str, data: dict) -> None:
    """
    Writes a dictionary to a JSON file.

    Args:
        file_path (str): The path to the file where the JSON data will be written.
        data (dict): The dictionary to be written to the JSON file.

    Returns:
        None
    """
    # Open the file in write mode.
    with open(file_path, 'w') as file:
        # Write the given dictionary to the JSON file.
        json.dump(data, file, indent=4)

# Create folder and all its parent directories if they do not exist.
def create_folders(path: str) -> None:
    """
    Creates a folder and all its parent directories if they do not exist.

    Args:
        path (str): The path to the folder to be created.
    """
    # Use os.makedirs() to recursively create the directory.
    os.makedirs(path, exist_ok=True)

# Check if file exists at specified path.
def file_exists(file_path: str) -> bool:
    """
    Checks if a file exists at the specified path.

    Args:
        file_path (str): The path to the file to be checked.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    # Use os.path.exists() to check if the file exists.
    return os.path.exists(file_path)
```