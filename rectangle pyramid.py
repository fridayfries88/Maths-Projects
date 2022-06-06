import turtle
turtle.speed(2)
turtle.shape("turtle")
turtle.color("magenta")
turtle.pensize(4)


x = 200
y = 100

def rect ():
    turtle.pendown()
    for i in range (2):
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(y)
        turtle.right(90)
    turtle.penup()

rect()
turtle.forward(x / 7)
turtle.left(90)
turtle.forward(y * 0.75)
turtle.right(90)
x *= 0.75
y *= 0.75
rect()
turtle.forward(x / 7)
turtle.left(90)
turtle.forward(y * 0.75)
turtle.right(90)
x *= 0.75
y *= 0.75
rect()
