#turtle setup
import turtle
turtle.screensize(512)
turtle.pensize(5)
turtle.speed(0)
turtle.shape("turtle")
#function that draws a (sort spikey) bush
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
#function to draw a rectangle
def rectangle (x, y):
    for i in range(2):
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(y)
        turtle.left(90)
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)
#function to draw a triangle
def triangle (x):
    for i in range(3):
        turtle.forward(x)
        turtle.left(120)
#function that draws a window
def window (x, y):
    for i in range(2):
        #draws the window frame
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(y)
        turtle.left(90)
    #draws the cross in the middle of the windowframe
    turtle.forward(x / 2)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x / 2)
    turtle.left(90)
    turtle.forward(y / 2)
    turtle.left(90)
    turtle.forward(x)
#function that draws a house
def house ():
    #draws the main base of the house
    rectangle(100, 130)
    turtle.forward(-25)
    #draws the roof of the house
    triangle(150)
    turtle.forward(50)
    turtle.left(90)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()
    #makes the attic window
    window(50, 50)
    turtle.penup()
    turtle.forward(-30)
    turtle.right(90)
    turtle.forward(165)
    turtle.pendown()
    turtle.left(90)
    #draws the the door
    turtle.begin_fill()
    rectangle(10, 30)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(-25)
    turtle.left(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.pendown()
    #draws the chimney
    turtle.begin_fill()
    rectangle(10, 30)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(-160)
    turtle.right(90)
    turtle.pendown()
    #draws the bedroom window
    window(30, 30)
    turtle.penup()
   # turtle.forward(-20)
    turtle.left(90)
    turtle.forward(-105)
    turtle.right(90)
    turtle.pendown()
    turtle.color("#88d13f")
    bush(1, 1)
    turtle.penup()
    turtle.forward(-50)
    turtle.pendown()
    bush(1, 1)
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)

#runs the function to draw a house
house()
#makes the turtle chill
turtle.color("#88d13f")
#waits for input to end the script
input("Press Enter to continue...")
