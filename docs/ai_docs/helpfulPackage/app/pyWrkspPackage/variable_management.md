# Documentation for src/helpfulPackage/app/pyWrkspPackage/variable_management.py

**Script Documentation**

**Summary**
----------

This script provides utility functions for merging dictionaries, splitting lists into chunks, flattening lists, and loading environment variables.

**Functions and Classes**

### dict_merge(d1: dict, d2: dict) -> dict
Merges two dictionaries recursively. If a key in both dictionaries has a dictionary as its value,
the function will merge those dictionaries as well. Otherwise, the value from the second dictionary
will overwrite the value from the first dictionary.

*   **Inputs:** `d1` (dict): The first dictionary to merge.
    *   `d2` (dict): The second dictionary to merge.
*   **Output:** `dict`: The merged dictionary.

```python
# Example usage:
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged_dict = dict_merge(d1, d2)
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

### chunk_list(lst: list, size: int) -> list
Splits a list into smaller lists (chunks) of a specified size.

*   **Inputs:** `lst` (list): The list to be split into chunks.
    *   `size` (int): The size of each chunk.
*   **Output:** `list`: A list of lists, where each sublist is a chunk of the original list.

```python
# Example usage:
numbers = [1, 2, 3, 4, 5]
chunks = chunk_list(numbers, 2)
print(chunks)  # Output: [[1, 2], [3, 4], [5]]
```

### flatten(lst: list) -> list
Flattens a list of lists into a single list.

*   **Inputs:** `lst` (list): A list of lists to be flattened.
*   **Output:** `list`: A single flattened list containing all the elements of the sublists.

```python
# Example usage:
nested_list = [[1, 2], [3, 4]]
flattened_list = flatten(nested_list)
print(flattened_list)  # Output: [1, 2, 3, 4]
```

### load_from_env(variable: str) -> str
Loads the value of an environment variable.

*   **Inputs:** `variable` (str): The name of the environment variable to retrieve.
*   **Output:** `str`: The value of the specified environment variable as a string.

```python
# Example usage:
env_variable = 'MY_VAR'
value = load_from_env(env_variable)
print(value)  # Output: The value of MY_VAR from your .env file
```

**Dependencies**
--------------

This script depends on the following external packages/modules:

*   `dotenv`: Used to load environment variables from a .env file.
*   `os`: Used to access environment variables.

```python
from dotenv import load_dotenv
import os
```