import turtle
from random import randrange

turtle.Screen().setup(1600, 800)
turtle.Screen().bgcolor('yellow')  #  устанавливаем цвет фона

tim = turtle.Turtle()    # создаем первую черепашку и устанавливаем ее свойства
tim.color('red')
tim.pensize(3)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.right(180)
tim.forward(80)

alex = turtle.Turtle()    # создаем вторую черепашку и устанавливаем ее свойства
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

def move_turtles(turtles, dist, angle):
    for turtle in turtles:    # все черепашки из списка делают одни и те же действия
        turtle.forward(dist)
        turtle.right(angle)


turtles = []                   # список черепашек
head = 0
num_turtles = 10               # количество череашек
turtle.colormode(255) # <-- Эта строка включает режим 0-255
turtle.tracer(1, 0)
for i in range(num_turtles):
    turt = turtle.Turtle()     # создаем черепашку и устанавливаем ее свойства
    turt.setheading(head)
    turt.pensize(2)
    turt.color(randrange(256), randrange(256), randrange(256))
    turt.speed(5)
    turtles.append(turt)       # добавляем черепашку в список
    head = head + 360/num_turtles

for i in range(70):
    move_turtles(turtles, 10, i)

turtle.done() # Окно останется открытым до его закрытия пользователем