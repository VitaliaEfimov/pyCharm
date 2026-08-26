"""
✅ Команда turtle.penup() поднимает перо, а команда turtle.pendown() – опускает.

✅ Команда turtle.circle(r) применяется для рисования круга радиусом r.

✅ Команда turtle.dot() применяется для рисования точки.

✅ Команда turtle.pensize(width) устанавливает ширину пера в width пикселей.

✅ Команда turtle.pencolor() применяется для изменения цвета линий. В качестве аргумента можно передать название цвета строкой или цвет в формате RGB — кортеж из трёх чисел или три отдельных числа.

✅ Команда turtle.Screen().bgcolor() применяется для изменения цвета фона. В качестве аргумента можно передать название цвета строкой или цвет в формате RGB — кортеж из трёх чисел или три отдельных числа.

✅ Команда turtle.Screen().bgpic(filename) применяется для установки фонового изображения в графическом окне.

✅ Команда turtle.stamp() оставляет штамп черепашки.

✅ Команда turtle.clear() стирает все рисунки в графическом окне. Но не меняет положение черепашки, цвет рисунка и цвет фона графического окна.

✅ Команда turtle.reset() стирает все рисунки, имеющиеся в графическом окне, задает черный цвет рисунка и возвращает черепашку в исходное положение в центре экрана. Эта команда не переустанавливает цвет фона графического окна.

✅ Команда turtle.clearscreen() стирает все рисунки в графическом окне, меняет цвет рисунка на черный, а цвет фона на белый, и возвращает черепашку в исходное положение в центре графического окна.

✅ Команда turtle.Screen().setup(a, b) устанавливает размер графического окна a × b пикселей.
"""

import turtle

turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)
turtle.penup() # Поднять перо
turtle.forward(25)
turtle.pendown() # Опустить перо
turtle.forward(50)

turtle.circle(80)

turtle.dot() # Поставить точку
turtle.forward(50)

turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.forward(50)

turtle.pensize(5)
turtle.circle(80)

turtle.forward(100)

turtle.pencolor('red')
turtle.circle(80)

turtle.forward(100)

turtle.Screen().colormode(255)
turtle.pencolor(13, 56, 240)  #  кортеж в качестве аргумента
turtle.circle(80)

turtle.pencolor(
    130, 240, 200
)  #  значения r, g, b в качестве аргументов
turtle.circle(50)

turtle.Screen().bgcolor('gray')
turtle.pencolor('green')
turtle.circle(20)

turtle.done() # Окно останется открытым до его закрытия пользователем