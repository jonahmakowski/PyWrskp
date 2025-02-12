import math

def get_number(prompt:str):
    def get_number(prompt: str):
        """
        Prompt the user to enter a number and return it as a float.

        Args:
            prompt (str): The message to display to the user when asking for input.

        Returns:
            float: The number entered by the user.

        Raises:
            ValueError: If the input cannot be converted to a float, the user is prompted to try again.
        """
    while True:
        number = input(prompt)
        try:
            return float(number)
        except ValueError:
            print("That's not a valid number. Try again.")

def area_of_triangle():
    """
    Calculate and print the area of a triangle based on user-provided base length and height.

    Prompts the user to enter the base length and height of the triangle, calculates the area using the formula:
    area = (base * height) / 2, and prints the result.

    Returns:
        None
    """
    b = get_number('Enter the base length of the triangle: ')
    h = get_number('Enter the height of the triangle: ')
    a = (b * h) / 2
    print('The area of the triangle is {}'.format(a))

def area_of_circle():
    """
    Calculate and print the area of a circle based on user-provided radius.

    Prompts the user to enter the radius of the circle, calculates the area using the formula:
    area = π * radius^2, and prints the result.

    Returns:
        None
    """
    r = get_number('Enter the radius of the circle: ')
    a = math.pi * (r ** 2)
    print('The area of the circle is {}'.format(a))

def area_of_rectangle():
    """
    Calculate and print the area of a rectangle.

    Prompts the user to enter the length and width of the rectangle,
    calculates the area, and prints the result.

    Returns:
        None
    """
    l = get_number("Enter the length of the rectangle: ")
    w = get_number("Enter the width of the rectangle: ")
    a = l * w
    print('The area of the rectangle is {}'.format(a))

def perimeter():
    """
    Calculates the perimeter of a shape based on user input for side lengths.

    The function repeatedly prompts the user to enter side lengths until the user enters 0.
    It then calculates the sum of all entered side lengths and prints the perimeter along with the number of sides.

    Returns:
        None
    """
    sides = []
    while True:
        side_length = get_number("Enter a side length (Enter 0 to end calculate): ")
        if side_length == 0:
            break
        else:
            sides.append(side_length)

    p = sum(sides)
    print('The perimeter of the shape with {} sides is {}'.format(len(sides), p))

def perimeter_of_circle():
    """
    Calculates and prints the perimeter of a circle based on user-provided radius.

    Prompts the user to enter the radius of the circle, calculates the perimeter
    using the formula 2 * pi * radius, and prints the result.

    Returns:
        None
    """
    r = get_number("Enter the radius of the circle: ")
    p = 2 * math.pi * r
    print('The perimeter of the circle is {}'.format(p))

def right_angle():
    """
    Calculates the third side of a right-angled triangle based on user input.

    Prompts the user to specify whether they are looking for a leg or the hypotenuse,
    and then asks for the lengths of the two known sides of the triangle. Depending on
    the user's choice, it calculates the length of the third side using the Pythagorean theorem.

    Returns:
        None

    Raises:
        ValueError: If the input for the type of side is invalid or if the calculation
                    for the leg results in a negative value under the square root.

    Notes:
        - The function uses the `get_number` function to obtain the lengths of the sides.
        - The function prints the length of the third side of the triangle.
    """
    type = input('Are you looking for a leg (l) or the hypotenuse (h): ')
    first_side = get_number("Enter the first side of the triangle: ")
    second_side = get_number("Enter the second side of the triangle: ")
    match type:
        case 'h':
            third_side = math.sqrt(first_side ** 2 + second_side ** 2)
        case 'l':
            third_side = math.sqrt(first_side ** 2 - second_side ** 2)
        case _:
            print("That isn't a valid")
            return
    print("The third side of the triangle is {}".format(third_side))

def is_right_angle():
    """
    Determines if a triangle with given side lengths is a right-angle triangle.

    Prompts the user to enter the lengths of the three sides of a triangle.
    The third side should be the hypotenuse. The function then calculates
    the expected length of the hypotenuse using the Pythagorean theorem and
    compares it to the user-provided length.

    If the calculated hypotenuse matches the user-provided hypotenuse, it
    prints a message confirming that the triangle is a right-angle triangle.
    Otherwise, it prints a message indicating that the triangle is not a
    right-angle triangle and shows the expected hypotenuse length.

    Returns:
        None
    """
    print('The third side of the triangle should be the hypotenuse!')
    first_side = get_number("Enter the first side of the triangle: ")
    second_side = get_number("Enter the second side of the triangle: ")
    third_side = get_number("Enter the third side of the triangle: ")

    third_side_calculation = math.sqrt(first_side ** 2 + second_side ** 2)

    if third_side_calculation == third_side:
        print('Yep! This is a right angle triangle!')
    else:
        print("Nope, this isn't a right angle triangle. You entered {} as the third side, and {} was calculated"
              .format(third_side, third_side_calculation))

def volume_of_cylinder():
    """
    Calculates and prints the volume and surface area of a cylinder.

    Prompts the user to enter the height and radius of the cylinder, then calculates
    the volume using the formula V = πr^2h and the surface area using the formula 
    A = 2πr(h + r). Finally, prints the results.

    Returns:
        None
    """
    h = get_number('Enter the height of the cylinder: ')
    r = get_number('Enter the radius of the cylinder: ')

    v = math.pi * (r ** 2) * h
    a = (2 * (2 * math.pi * r)) + (h*2*math.pi*r)

    print('The volume of the cylinder is {}, and the surface area is {}'.format(v, a))

def volume_of_prism():
    """
    Calculates and prints the volume and surface area of a rectangular prism.

    Prompts the user to enter the height, length, and width of the prism.
    Uses these dimensions to calculate the volume and surface area of the prism.
    Prints the results in a formatted string.

    Returns:
        None
    """
    h = get_number('Enter the height of the prism: ')
    l = get_number('Enter the length of the prism: ')
    w = get_number('Enter the width of the prism: ')

    a = 2 * (w*h + l*w + l*h)
    v = l * w * h

    print('The volume of the prism is {}, and the surface area is {}'.format(v, a))

def percentage_calculations():
    number_to_modify = get_number("Enter the number to modify: ")
    percentage = get_number("Enter the percentage to modify it by: ")
    percentage /= 100
    result = number_to_modify * percentage

    print('The result is {}'.format(result))

def main():
    """
    Main function to interact with the user and perform various mathematical calculations.
    
    The options available are:
    - Area of a triangle (Type 'AT')
    - Area of a circle (Type 'AC')
    - Area of a rectangle (Type 'AR')
    - Perimeter of a shape with three or more sides (Type 'P')
    - Perimeter of a circle (Type 'PC')
    - Third side of a right-angle triangle calculation (Type 'RT')
    - Check if the given side lengths form a right-angle triangle (Type 'RS')
    - Percentage calculations (Type '%C')
    - Volume/surface area of a cylinder (Type 'VC')
    - Volume/surface area of a rectangle-based prism (Type 'VR')
    
    Prompts the user to select an option and calls the corresponding function to perform the calculation.
    If an invalid option is selected, it notifies the user.
    """
    print('What would you like to do?')
    print('The options are:')
    print('\t- Area of a triangle (Type AT)')
    print('\t- Area of a circle (Type AC)')
    print('\t- Area of a rectangle (Type AR)')
    print('\t- Perimeter of a shape with three or more sides (Type P)')
    print('\t- Perimeter of a circle (Type PC)')
    print('\t- Third Side of a right angle triangle calculation (Type RT)')
    print('\t- Is this a right angle from side lengths (Type RS)')
    print('\t- Percentage calculations (Type %C)')
    print('\t- Volume/surface area of a cylinder (Type VC)')
    print('\t- Volume/surface area of a rectangle-based-prism (Type VR)')
    option = input()
    match option:
        case 'AT':
            area_of_triangle()
        case 'AC':
            area_of_circle()
        case 'AR':
            area_of_rectangle()
        case 'P':
            perimeter()
        case 'PC':
            perimeter_of_circle()
        case 'RT':
            right_angle()
        case 'RS':
            is_right_angle()
        case '%C':
            percentage_calculations()
        case 'VC':
            volume_of_cylinder()
        case 'VR':
            volume_of_prism()
        case _:
            print('That is not a valid option')

if __name__ == '__main__':
    main()