import turtle

turtle.shape('turtle')
turtle.pensize(5)
turtle.stamp()
for _ in range(12):
    turtle.penup()
    turtle.forward(110)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.stamp()
    turtle.penup()
    turtle.backward(145)
    turtle.right(30)

turtle.setheading(0)

turtle.done() # Окно останется открытым до его закрытия пользователем