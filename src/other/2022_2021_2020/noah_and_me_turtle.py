import turtle
import extra_turtle_stuff
def run():
    t = turtle.Turtle()
    t.speed(0)

    sides = 6
    length_sides = 50
    t.fillcolor('green')
    t.begin_fill()
    extra_turtle_stuff.draw_hex(sides, length_sides, t)

    t.left(120)

    extra_turtle_stuff.draw_hex(sides, length_sides, t)
    t.left(120)
    extra_turtle_stuff.draw_hex(sides, length_sides, t)
    t.left(120)
    t.penup()
    t.forward(50)
    t.left(60)
    t.pendown()
    extra_turtle_stuff.draw_hex(sides, length_sides, t)
    t.end_fill

    t.right(120)
    t.forward(length_sides)
    t.right(60)
    t.forward(length_sides)
    t.left(120)
    extra_turtle_stuff.turn(100, 0.65, 'left', t)
    t.right(2)
    t.forward(length_sides - 5)
    t.left(360 / sides)
    t.forward(length_sides)
    extra_turtle_stuff.turn(100, 0.65, 'left', t)
    t.right(sides + 2)
    t.forward(length_sides)
    extra_turtle_stuff.turn(90, 0.85, 'left', t)
    t.right(sides * 3)
    t.forward(length_sides - 10)
    t.left(360 / sides)
    t.forward(length_sides)
    extra_turtle_stuff.turn(100, 0.7, 'left', t)
    t.penup()
    t.goto((0 + (length_sides * 3 - 15)), 30)
    t.right(1)
    t.pendown()
    t.forward(length_sides)
    extra_turtle_stuff.turn(90, 2, 'right', t)
    t.forward(length_sides + (length_sides * 0.2))
    t.penup()
    t.goto((0 + (length_sides * 2 - 15)), 75)
    t.right(90)
    t.pendown()
    t.forward(length_sides)
    extra_turtle_stuff.turn(3, 30, 'left', t)
    t.forward(length_sides / 2)
    extra_turtle_stuff.turn(3, 30, 'left', t)
    t.forward(length_sides - 10)
    
    t.penup()
    t.goto((0 + (length_sides * -1.5)), 75)


run()