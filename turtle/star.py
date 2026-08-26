import turtle

turtle.showturtle()
side = 100
u = 0
for i in range(5):
    turtle.forward(side)
    u += 216
    turtle.setheading(u)