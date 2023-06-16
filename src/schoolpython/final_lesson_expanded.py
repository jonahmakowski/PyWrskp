'''
Jonah
Mrs. Brownhill
June 19, 2023
This program is supposed to draw a cylinder with the givin radius and height
'''

import turtle
from math import pi


def funct():
    # Getting radius and height from the user
    radius = float(input('What radius would you like to use?   '))
    height = float(input('What is the height you would like to use?   '))

    # Calculating the volume and surface
    volume = pi * (radius**2) * height
    surface = (2 * pi * radius * height) + (2 * pi * (radius ** 2))

    # Showing the user the volume and surface area
    print('The surface area is ' + str(surface))
    print('The surface area is ' + str(volume))

    # Show the user the rounded volume and surface area
    print('The rounded surface area is ' + str(round(surface)))
    print('The rounded surface area is ' + str(round(volume)))

    # Making it so it doesn't take forever!
    turtle.speed(0)
    
    # Making it centered
    turtle.setpos(0, -radius)

    # Starting first circle (The one that is farthest in the back)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    # Setting color in prep for the main cylinder
    turtle.color('green')
    
    # Defining a count var that is used in the loop to figure out when to end it.
    counter = 0
    
    # Drawing the main cylinder
    while counter < height - 2:
        counter = counter + 0.1
        turtle.forward(0.1)
        turtle.circle(radius)

    # Drawing the final circle
    turtle.forward(0.1)
    turtle.color('black')
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    # Displaying the amount of circles drawn
    print(str(counter+2) + ' circles were drawn!')
    '''
    This is where the +2 comes from,
    1. The first of the three comes from the first black circle that is drawn
    2. The final of the three comes from the final black circle that is drawn
    '''

    # I need this line on my computer at home so that the turtle window does not go away
    input('Press enter to continue')  # You should be able to remove it


funct()
