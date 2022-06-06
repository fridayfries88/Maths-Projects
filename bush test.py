import turtle
turtle.speed(10)

def triangle (x):
    for i in range(3):
        turtle.forward(x)
        turtle.left(120)

def bush (wide, high):
    turtle.color("green")
    turtle.begin_fill()
    for i in range(2):
        turtle.right(25)
        for i in range(wide):
            turtle.forward(15)
            turtle.left(50)
            turtle.forward(15)
            turtle.right(50)
        turtle.right(90)
        for i in range(high):
            turtle.forward(15)
            turtle.left(50)
            turtle.forward(15)
            turtle.right(50)
        turtle.right(65)
    turtle.end_fill()

bush(5, 3)