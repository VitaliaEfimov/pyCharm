
import turtle
colors = ('deepskyblue', 'yellow', 'black', 'green', 'red')
step = 52
turtle.pensize(5)
x, y = 0, 0

for i in range(5):
    turtle.up()
    turtle.goto(x, (0, -step)[i % 2])
    turtle.down()
    turtle.pencolor(colors[i])
    turtle.circle(50)
    x += step

turtle.done() # Окно останется открытым до его закрытия пользователем