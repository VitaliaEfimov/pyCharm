import turtle

def square(width, g):
    turtle.setheading(g)
    turtle.forward(width)
    turtle.setheading(90+g)

    turtle.forward(width)
    turtle.setheading(180+g)

    turtle.forward(width)
    turtle.setheading(270+g)

    turtle.forward(width)
w = 100
turtle.showturtle()
square(w, 0)
square(w, 22.5)
square(w, 45)
square(w, 67.5)
square(w, 90)
square(w, 112.5)
square(w, 135)
square(w, 157.5)
square(w, 180)
square(w, 202.5)
square(w, 225)
square(w, 247.5)
square(w, 270)
square(w, 292.5)