# Documentation for src/helpfulPackage/app/pyWrkspPackage/misc.py

**Script Documentation**

**Summary**

This Python script provides a set of utility functions to interact with the user and measure execution times. The `int_input` and `float_input` functions prompt the user to enter integer or floating-point numbers, respectively, until a valid value is entered. The `timer` decorator measures the execution time of a given function.

**Functions and Classes**

### int_input(prompt: str) -> int

*   Description: Prompts the user to enter an integer value.
*   Parameters:
    *   prompt (str): The message to display when asking for input.
*   Returns: The integer value entered by the user.

```python
def int_input(prompt: str) -> int:
    """
    Prompt the user to enter an integer value.

    This function repeatedly prompts the user with the given prompt string until
    a valid integer is entered. If the user enters a non-integer value, an error
    message is displayed and the prompt is shown again.

    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        int: The integer value entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")
```

### float_input(prompt: str) -> float

*   Description: Prompts the user to enter a floating-point number.
*   Parameters:
    *   prompt (str): The message to display when asking for input.
*   Returns: The floating-point number entered by the user.

```python
def float_input(prompt: str) -> float:
    """
    Prompt the user to enter a floating-point number.

    This function repeatedly prompts the user with the given prompt until a valid
    floating-point number is entered. If the user enters an invalid value, an error
    message is displayed and the prompt is shown again.

    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        float: The floating-point number entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")
```

### timer(func)

*   Description: A decorator that prints the execution time of the decorated function.
*   Parameters:
    *   func (callable): The function to be decorated.

```python
def timer(func):
    """
    A decorator that prints the execution time of the decorated function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function that prints its execution time.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper
```

### timestamp_print(*args, sep=' ', end='\n') -> None

*   Description: Prints the given arguments with a timestamp.
*   Parameters:
    *   args (variable length argument list): The values to be printed.
    *   sep (str): Separator between arguments. Defaults to a single space.
    *   end (str): String appended after the last value. Defaults to a newline.

```python
def timestamp_print(*args, sep=' ', end='\n') -> None:
    """
    Prints the given arguments with a timestamp.

    Args:
        *args: Variable length argument list to be printed.
        sep (str, optional): Separator between arguments. Defaults to a single space.
        end (str, optional): String appended after the last value. Defaults to a newline.

    Example:
        timestamp_print("Hello", "world")
        # Output: [2023-10-05 14:23:45] Hello world
    """
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ",end='')
    for arg in args:
        print(arg, end=sep)
    print(end, end='')
```

**Dependencies**

The script depends on the following external packages/modules:

*   `time`: Provides the time-related functions used in the script.
*   `input()`: Used to prompt the user for input.

```python
import time

# Rest of the code...
```

Note: The actual dependencies are not listed separately as they are built-in Python modules. However, if this script were part of a larger project or package, additional dependencies might be required.