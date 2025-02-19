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
    found_mult = False
    found_squa = False

    exponent = ''
    base = ''

    for char in str(scientific):
        if char == '*':
            found_mult = True
        elif char == '^':
            found_squa = True
            continue

        if not found_mult:
            base += char
        elif found_squa:
            exponent += char

    return float(base) * 10 ** float(exponent)

def make_scientific(standard):
    """
    Convert a standard decimal number to scientific notation.

    Parameters:
    standard (float or int): The standard decimal number to be converted.

    Returns:
    str: The number in scientific notation as a string in the format 'base*10^exponent'.
    """
    base = float(standard)
    exponent = 0
    if base > 10:
        while base >= 10:
            base /= 10
            exponent += 1
    else:
        while base < 0:
            base *= 10
            exponent -= 1

    return '{}*10^{}'.format(base, exponent)


if __name__ == '__main__':
    if input('Do you want to convert from standard to scientific or other other way round (1 or 2)  ') == '1':
        print("It's", make_scientific(input('Enter your number in standard notation  ')))
    else:
        print("It's", make_standered(input('Enter your number in scientific notation  ')))
