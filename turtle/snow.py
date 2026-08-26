import turtle
from random import *

turtle.speed(10)
turtle.Screen().bgcolor('cyan')
def create_snow(size):
    for _ in range(8):
        for _ in range(3):
            turtle.forward(size/4)
            turtle.left(45)
            turtle.forward(size/4)
            turtle.backward(size/4)
            turtle.right(90)
            turtle.forward(size/4)
            turtle.backward(size/4)
            turtle.left(45)
        turtle.forward(size/4)
        turtle.backward(size)
        turtle.left(45)

count = randint(1, 10)
colors = ['red',
'blue',
'yellow',
'green',
'purple',
'orange']

def get_snow(count):
    turtle.penup()
    for _ in range(count):
        coor_x = randint(-100, 100)
        coor_y = randint(-100, 100)
        turtle.pencolor(choice(colors))
        turtle.goto(coor_x, coor_y)
        turtle.pendown()
        create_snow(randint(10, 100))
        turtle.penup()
get_snow(count)

turtle.done() # Окно останется открытым до его закрытия пользователем