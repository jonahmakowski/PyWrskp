import turtle

def display():
    counter = 1
    for x in range(100, 140):
        print(counter)
        turtle.forward(x)
        turtle.left(90)
        counter += 1
        
display()
