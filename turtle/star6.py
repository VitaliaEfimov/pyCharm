import math
import turtle

side = 100
u = 120
for _ in range(3):
    turtle.forward(side)
    turtle.left(u)

turtle.up()
turtle.goto(0, side / math.sqrt(3))
turtle.down()

for _ in range(3):
    turtle.forward(side)
    turtle.right(u)

turtle.done() # Окно останется открытым до его закрытия пользователем