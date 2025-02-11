import json

def load_from_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(file_path: str, text: str) -> None:
    """
    Write the given text to a file at the specified file path.

    Args:
        file_path (str): The path to the file where the text will be written.
        text (str): The text to write to the file.

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        file.write(text)

def append_to_file(file_path: str, text: str) -> None:
    """
    Appends the given text to the end of the specified file.

    Args:
        file_path (str): The path to the file where the text will be appended.
        text (str): The text to append to the file.

    Returns:
        None
    """
    with open(file_path, 'a') as file:
        file.write(text)

def json_load_file(file_path: str) -> dict:
    """
    Load a JSON file and return its contents as a dictionary.

    Args:
        file_path (str): The path to the JSON file to be loaded.

    Returns:
        dict: The contents of the JSON file as a dictionary.

    Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def json_write_file(file_path: str, data: dict) -> None:
    """
    Write a dictionary to a JSON file.

    Args:
        file_path (str): The path to the file where the JSON data will be written.
        data (dict): The dictionary to be written to the JSON file.

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
