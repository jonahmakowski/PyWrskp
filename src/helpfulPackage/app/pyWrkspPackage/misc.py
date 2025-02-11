import time

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
