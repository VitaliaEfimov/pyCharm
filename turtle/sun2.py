import turtle

def web(side, n):
    for _ in range(n):
        turtle.forward(side)

        turtle.stamp()

        turtle.backward(side)

        turtle.left(360 / n)

    turtle.hideturtle()


web(100, 360)

turtle.done() # Окно останется открытым до его закрытия пользователем