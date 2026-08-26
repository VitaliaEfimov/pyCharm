import turtle


turtle.goto(0, 100)
turtle.goto(-100, 0)
turtle.goto(0, 0)

turtle.goto(100, 150)
position = turtle.pos()
print(position)

turtle.goto(200, -150)
x = turtle.xcor()
y = turtle.ycor()
print(x)
print(y)

turtle.hideturtle() # Скрыть
turtle.speed(0) # Отключить анимацию
turtle.circle(200)
for i in range(1, 11):
    turtle.speed(i) # Установка скорости от 1 - самая медленная, 10 - самая быстрая
    turtle.circle(100 - 10*i)
# turtle.showturtle() # Отобразить

turtle.done() # Окно останется открытым до его закрытия пользователем