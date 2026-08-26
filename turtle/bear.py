import math
import turtle

def bear(r):
    turtle.circle(r)
    rt = r * math.sqrt(3)
    turtle.circle(rt)

    turtle.up()
    turtle.goto(0, r // 2.5)
    turtle.down()
    turtle.left(90)
    turtle.forward(r)
    turtle.right(90)
    turtle.circle(r // 6)

    bear_ears(r)
    bear_eyes(r)
    turtle.hideturtle()

def bear_eyes(r):
    for x in (-r, r):
        turtle.up()
        turtle.goto(x, r * 2)
        turtle.down()
        turtle.dot(r / 3)

def bear_ears(r):
    rt = r * math.sqrt(3)
    pos_x = rt * math.sqrt(2) / 2

    for x in (-pos_x, pos_x):
        turtle.up()
        turtle.goto(x, rt + pos_x)
        turtle.down()
        if x > 0:
            turtle.setheading(-45)
        else:
            turtle.setheading(45)
        turtle.circle(r / 2)

bear(100)

turtle.done() # Окно останется открытым до его закрытия пользователем