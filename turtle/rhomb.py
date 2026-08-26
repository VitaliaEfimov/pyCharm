import turtle

def rhomb(width, u):
    turtle.setheading(u)
    turtle.forward(width)
    turtle.setheading(u + 60)

    turtle.forward(width)
    turtle.setheading(u + 180)

    turtle.forward(width)
    turtle.setheading(u + 240)

    turtle.forward(width)

turtle.showturtle()
su = 0
w = 100
for i in range(10):
    rhomb(w, su)
    su += 36