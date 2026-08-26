import turtle

def turtles(side, n):
    turtle.shape('turtle')
    turtle.stamp()
    turtle.penup()

    for _ in range(n):
        turtle.forward(side)
        turtle.stamp()
        turtle.backward(side)
        turtle.left(360 / n)

turtles(100, 6)

turtle.done() # Окно останется открытым до его закрытия пользователем