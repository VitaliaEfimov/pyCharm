import turtle

colors = ('blue', 'yellow', 'green', 'purple', 'orange', 'red')

def octagon(start, step, n):
    size = 1
    for _ in range(n):
        for i in range(6):
            turtle.pencolor(colors[i])
            turtle.pensize(size)
            turtle.left(45)
            turtle.forward(start)
            start += step
            size += 1

octagon(10, 7, 10)

turtle.done() # Окно останется открытым до его закрытия пользователем