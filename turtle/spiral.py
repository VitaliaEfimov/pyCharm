import turtle

turtle.showturtle()
w = 10
u = 90
for i in range(100):
    turtle.setheading(u)
    turtle.forward(w)
    w += 10
    u +=90
