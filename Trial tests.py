# Created by Suraj Powar.
# Date: 25th December 2019.

import turtle
from random import randint

background = turtle.Screen()
background.bgcolor('light salmon')

def draw_circle(turtle, color, size, x,y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

c_tree = turtle.Turtle()
c_tree.speed(-200)

c_tree.penup()
c_tree.position()
c_tree.circle(50)


# First Triangle
c_tree.goto(0,0)
c_tree.color('green')
c_tree.begin_fill()
c_tree.fillcolor("green")
c_tree.pensize(8)
c_tree.pendown()
c_tree.goto(100,0)
c_tree.penup()
c_tree.end_fill()

# Second triangle
c_tree.goto(100,0)
c_tree.pendown()
c_tree.color("green")
c_tree.begin_fill()
c_tree.fillcolor("green")
c_tree.goto(0,75)
c_tree.goto(-100,0)
c_tree.forward(100)
c_tree.goto(125,-65)
c_tree.goto(-125,-65)
c_tree.goto(0,0)
c_tree.penup()
c_tree.end_fill()

# Third triangle
c_tree.goto(0,75)
c_tree.pendown()
c_tree.color("green")
c_tree.begin_fill()
c_tree.fillcolor("green")
c_tree.goto(50,75)
c_tree.goto(0,120)
c_tree.goto(-50,75)
c_tree.goto(0,75)
c_tree.penup()
c_tree.end_fill()

# Trunk of tree
c_tree.goto(0,-90)
c_tree.pendown()
c_tree.color("brown")
c_tree.begin_fill()
c_tree.fillcolor("brown")
c_tree.goto(20,-90)
c_tree.left(90)
c_tree.forward(20)
c_tree.left(90)
c_tree.forward(40)
c_tree.left(90)
c_tree.forward(20)
c_tree.left(90)
c_tree.forward(20)
c_tree.penup()
c_tree.end_fill()

# Generic message
c_tree.goto(-200,200)
c_tree.color('Red')
c_tree.write('Merry Christmas to you!', 'right', font=('Arial', 30, 'normal'))
c_tree.goto(-90,-200)
c_tree.color('Black')
c_tree.write('Name of reciever', 'centre', font=('Comic sans MS', 32, 'italic', 'bold'))


#Star
turns = 5
c_tree.begin_fill()
c_tree.color('yellow')

while turns>0:
    #c_tree.penup()
    c_tree.goto(0,120)
    c_tree.pendown()
    c_tree.forward(25)
    c_tree.left(145)
    turns = turns - 1
    #c_tree.end_fill()

# Snow
def snow():
    c_tree.begin_fill()
    c_tree.color('white')
    c_tree.penup()
    #c_tree.goto(0,160)
    c_tree.pendown()
    c_tree.circle(5)
    c_tree.end_fill()

num_snow = 0
while num_snow < 50:
    x = randint(-300,300)
    y = randint(-300,170)
    snow()
    c_tree.penup()
    c_tree.goto(x,y)
    c_tree.pendown()
    num_snow = num_snow + 1

turtle.exitonclick()
