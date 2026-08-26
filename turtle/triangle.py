import turtle

def triangle(side):
    turtle.showturtle()
    turtle.forward(side)
    turtle.setheading(120)

    turtle.forward(side)
    turtle.setheading(240)

    turtle.forward(side)

triangle(100)