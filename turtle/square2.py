import turtle

def square(width):
    turtle.setheading(0)
    turtle.forward(width)
    turtle.setheading(90)

    turtle.forward(width)
    turtle.setheading(180)

    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(width)
w = 10
turtle.showturtle()
for i in range(10):
    turtle.backward(10)
    square(w)
    w += 10
    turtle.setheading(0)