import turtle

def rectangle(width, height):

    turtle.forward(width)
    turtle.setheading(90)

    turtle.forward(height)
    turtle.setheading(180)

    turtle.forward(width)
    turtle.setheading(270)

    turtle.forward(height)

turtle.showturtle()
rectangle(200, 100)