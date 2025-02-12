# Documentation for src/schoolpython/grade9/scientific_notation.py

**Standard Notation Conversion Script Documentation**

**Summary:**
This script provides a simple command-line interface to convert numbers between standard decimal form and scientific notation. It allows users to choose the direction of conversion (standard to scientific or vice versa) and input their numbers accordingly.

**Functions and Classes:**

### make_standered

*   Description:
    *   Converts a number in scientific notation (as a string) to its standard form.
*   Parameters:
    *   `scientific` (str): A string representing a number in scientific notation. The format should be 'base*10^exponent'.
*   Returns:
    *   float: The number in its standard form.

### make_scientific

*   Description:
    *   Convert a standard decimal number to scientific notation.
*   Parameters:
    *   `standard` (float or int): The standard decimal number to be converted.
*   Returns:
    *   str: The number in scientific notation as a string in the format 'base*10^exponent'.

**Dependencies:**

The script depends on the following external packages/modules:

*   None

**Code with Comments:**
```python
# Define a function to convert from scientific notation to standard form
def make_standered(scientific):
    """
    Converts a number in scientific notation (as a string) to its standard form.

    Args:
        scientific (str): A string representing a number in scientific notation.
                          The format should be 'base*10^exponent'.

    Returns:
        float: The number in its standard form.

    Example:
        >>> make_standered("3.5*10^4")
        35000.0
    """
    # Initialize flags to track the presence of '*' and '^' characters
    found_mult = False
    found_squa = False

    # Initialize variables to store the base and exponent values
    exponent = ''
    base = ''

    # Iterate through each character in the input string
    for char in str(scientific):
        # Check if the current character is '*'
        if char == '*':
            # Set the found_mult flag to True
            found_mult = True
        # Check if the current character is '^'
        elif char == '^':
            # If it's not the first '*' we've seen, set the found_squa flag to True
            if found_mult:
                found_squa = True
            # Continue to the next iteration of the loop
            continue

        # If we haven't seen '*' yet, add the current character to the base value
        if not found_mult:
            base += char
        # If we've seen '*' and '^', add the current character to the exponent value
        elif found_squa:
            exponent += char

    # Return the converted number by multiplying the base by 10 raised to the power of the exponent
    return float(base) * 10 ** float(exponent)


# Define a function to convert from standard form to scientific notation
def make_scientific(standard):
    """
    Convert a standard decimal number to scientific notation.

    Parameters:
        standard (float or int): The standard decimal number to be converted.

    Returns:
        str: The number in scientific notation as a string in the format 'base*10^exponent'.
    """
    # Store the base value
    base = float(standard)
    # Initialize the exponent value to 0
    exponent = 0

    # If the base is greater than 10, repeatedly divide by 10 and increment the exponent until it's less than or equal to 10
    if base > 10:
        while base >= 10:
            base /= 10
            exponent += 1
    # If the base is less than 0, repeatedly multiply by 10 and decrement the exponent until it's greater than or equal to 0
    else:
        while base < 0:
            base *= 10
            exponent -= 1

    # Return the converted number as a string in scientific notation format
    return '{}*10^{}'.format(base, exponent)


# Check if this script is being run directly (not being imported)
if __name__ == '__main__':
    # Ask the user to choose the conversion direction
    choice = input('Do you want to convert from standard to scientific or other way round (1 or 2) ')
    
    # If the user chooses conversion from standard to scientific, ask for their number and print the result
    if choice == '1':
        print("It's", make_scientific(input('Enter your number in standard notation  ')))
    # If the user chooses other way round (scientific to standard), ask for their number and print the result
    else:
        print("It's", make_standered(input('Enter your number in scientific notation  ')))
```

**Note:** This documentation includes a comment that notes there are no dependencies listed. However, the script is using the built-in Python functions `float()` and `input()`, which are part of the standard library but don't have explicit dependencies declared in this context.

Also note that comments were added to make the code easier to understand for users who may not be familiar with how it works, even though they haven't changed the actual script itself.