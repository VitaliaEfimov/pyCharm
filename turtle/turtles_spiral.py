import turtle

turtle.Screen().bgcolor('green')
turtle.shape('turtle')
turtle.stamp()
turtle.penup()
step = 1

for _ in range(60):
    turtle.right(20)
    turtle.forward(step)
    turtle.stamp()
    step += 2

turtle.done() # Окно останется открытым до его закрытия пользователем