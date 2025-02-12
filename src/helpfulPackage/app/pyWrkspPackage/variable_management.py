from dotenv import load_dotenv
import os

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
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def flatten(lst: list) -> list:
    """
    Flattens a list of lists into a single list.

    Args:
        lst (list): A list of lists to be flattened.

    Returns:
        list: A single flattened list containing all the elements of the sublists.
    """
    return [item for sublist in lst for item in sublist]

def load_from_env(variable: str) -> str:
    """
    Load the value of an environment variable.

    This function loads the environment variables from a .env file and retrieves
    the value of the specified environment variable.

    Args:
        variable (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the specified environment variable as a string.
    """
    load_dotenv()
    return str(os.getenv(variable))
