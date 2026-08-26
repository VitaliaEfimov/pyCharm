import turtle

turtle.penup()
turtle.backward(190)
for _ in range(4):
    turtle.dot(50)
    turtle.forward(60)

def rectangle(width, height):
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(width)
        else:
            turtle.forward(height)
        turtle.right(90)
        turtle.dot(10)

rectangle(100, 20)

turtle.done() # Окно останется открытым до его закрытия пользователем