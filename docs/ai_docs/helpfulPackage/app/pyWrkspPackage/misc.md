# Documentation for src/helpfulPackage/app/pyWrkspPackage/misc.py

**Script Documentation**

**Summary**
------------

This Python script provides a set of utility functions to interact with the user and measure execution time. The `int_input` and `float_input` functions prompt users to enter integer and floating-point numbers, respectively, until valid input is provided. The `timer` decorator prints the execution time of a given function. The `timestamp_print` function prints its arguments with a timestamp.

**Functions and Classes**
-------------------------

### int_input(prompt: str) -> int

*   Description: Prompts the user to enter an integer value.
*   Inputs:
    *   prompt (str): The message to display when asking for input.
*   Output:
    *   int: The integer value entered by the user.

```python
while True:
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a number.")
```

### float_input(prompt: str) -> float

*   Description: Prompts the user to enter a floating-point number.
*   Inputs:
    *   prompt (str): The message to display when asking for input.
*   Output:
    *   float: The floating-point number entered by the user.

```python
while True:
    try:
        return float(input(prompt))
    except ValueError:
        print("Please enter a number.")
```

### timer(func)

*   Description: A decorator that prints the execution time of the decorated function.
*   Inputs:
    *   func (callable): The function to be decorated.
*   Output:
    *   callable: The wrapped function that prints its execution time.

```python
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
*   Inputs:
    *   *args: Variable length argument list to be printed.
    *   sep (str, optional): Separator between arguments. Defaults to a single space.
    *   end (str, optional): String appended after the last value. Defaults to a newline.

```python
print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ",end='')
for arg in args:
    print(arg, end=sep)
print(end)
```

**Dependencies**
--------------

*   time: For timing-related functions (e.g., `time.time()`).

**Code with Comments**
--------------------

```python
import time

# Function to prompt the user for an integer input.
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
    # Use a while loop to repeatedly ask for input until valid input is provided.
    while True:
        try:
            # Attempt to convert the user's input to an integer and return it.
            return int(input(prompt))
        except ValueError:
            # If the conversion fails, print an error message and show the prompt again.
            print("Please enter a number.")

# Function to prompt the user for a floating-point input.
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
    # Use a while loop to repeatedly ask for input until valid input is provided.
    while True:
        try:
            # Attempt to convert the user's input to a float and return it.
            return float(input(prompt))
        except ValueError:
            # If the conversion fails, print an error message and show the prompt again.
            print("Please enter a number.")

# Function to measure the execution time of a given function using a decorator.
def timer(func):
    """
    A decorator that prints the execution time of the decorated function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function that prints its execution time.
    """
    # Define a nested function wrapper that will print the execution time and return the result.
    def wrapper(*args, **kwargs):
        start = time.time()  # Record the start time of the function's execution.
        result = func(*args, **kwargs)  # Execute the function.
        end = time.time()  # Record the end time of the function's execution.
        print(f"{func.__name__} took {end - start:.4f} seconds")  # Print the execution time.
        return result  # Return the result of the function.
    return wrapper  # Return the wrapped function.

# Function to print its arguments with a timestamp.
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
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ", end='')  # Print the timestamp.
    for arg in args:
        print(arg, end=sep)  # Print each argument with the specified separator.
    print(end)  # Append the newline string after printing all arguments.

```