import math

def get_number(prompt:str):
    while True:
        number = input(prompt)
        try:
            return float(number)
        except ValueError:
            print("That's not a valid number. Try again.")

def area_of_triangle():
    b = get_number('Enter the base length of the triangle: ')
    h = get_number('Enter the height of the triangle: ')
    a = (b * h) / 2
    print('The area of the triangle is {}'.format(a))

def area_of_circle():
    r = get_number('Enter the radius of the circle: ')
    a = math.pi * (r ** 2)
    print('The area of the circle is {}'.format(a))

def area_of_rectangle():
    l = get_number("Enter the length of the rectangle: ")
    w = get_number("Enter the width of the rectangle: ")
    a = l * w
    print('The area of the rectangle is {}'.format(a))

def perimeter():
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
    r = get_number("Enter the radius of the circle: ")
    p = 2 * math.pi * r
    print('The perimeter of the circle is {}'.format(p))

def right_angle():
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
    h = get_number('Enter the height of the cylinder: ')
    r = get_number('Enter the radius of the cylinder: ')

    v = math.pi * (r ** 2) * h
    a = (2 * (2 * math.pi * r)) + (h*2*math.pi*r)

    print('The volume of the cylinder is {}, and the surface area is {}'.format(v, a))

def volume_of_prism():
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