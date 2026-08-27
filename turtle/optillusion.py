import turtle as t
import math

def triangle(side):
    for _ in range(3):
        t.left(120)
        t.forward(side)

def white_triangle(side):
    t.fillcolor('white')
    t.pencolor('white')
    t.begin_fill()
    for _ in range(3):
        t.right(120)
        t.forward(side)
    t.end_fill()

def circles(side, r):
    for i in range(1, 4):
        t.down()
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.up()
        t.right(120 * i)
        t.forward(side)
        t.setheading(0)

def illusion(side, r):
    triangle(side)
    x = 0
    y = side * math.sqrt(3) / 3 - r
    t.up()
    t.goto(x, y)
    circles(side, r)

    t.up()
    y = t.ycor() + r
    t.goto(x, y)
    white_triangle(side)
    t.hideturtle()

illusion(200, 25)

t.done()