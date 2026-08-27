import turtle


def circle(r, color):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def figure(r):
    turtle.Screen().setup(600, 600)
    turtle.Screen().bgcolor('MediumBlue')
    step = r / 4
    circle(r, 'Gold')
    turtle.penup()
    turtle.goto(step, 0)
    turtle.pendown()
    circle(r, 'MediumBlue')


r = int(100)
figure(r)