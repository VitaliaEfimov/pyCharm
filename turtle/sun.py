import turtle

turtle.showturtle()
side = 100
u = 0
for i in range(12):
    turtle.forward(side)
    turtle.backward(side)
    u += 30
    turtle.setheading(u)