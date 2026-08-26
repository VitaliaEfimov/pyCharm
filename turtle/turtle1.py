"""
✅ Модуль turtle — стандартный модуль Python для создания черепашьей графики.

✅ Команда turtle.showturtle() показывает черепашку (курсор) в графическом окне.

✅ Команда turtle.forward(n) перемещает черепашку вперед на n пикселей.

✅ Команда turtle.backward(n) перемещает черепашку назад на n пикселей.

✅ Команда turtle.right(angle) поворачивает черепашку вправо на angle градусов.

✅ Команда turtle.left(angle) поворачивает черепашку влево на angle градусов.

✅ Команда turtle.setheading(angle) устанавливает угловое направление черепашки на angle градусов.

✅ Команда turtle.heading() применяется для определения текущего углового направления черепашки.

✅ Команда turtle.shape() применяется для изменения внешнего вида черепашки. Команда принимает в качестве аргумента строковое название фигуры, определяющей форму черепашки. Доступные фигуры:

square (квадрат);
arrow (стрелка);
circle (круг);
turtle (черепашка);
triangle (треугольник);
classic (классическая стрелка).
"""
import turtle

turtle.showturtle()
turtle.forward(100)
turtle.backward(250)
turtle.forward(250)
turtle.right(90)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.forward(50)
turtle.left(45)

turtle.forward(50)
turtle.left(45)

turtle.forward(50)
turtle.left(45)

turtle.forward(50)
turtle.forward(100)
turtle.setheading(0)

turtle.forward(100)
turtle.setheading(90)

turtle.forward(100)
turtle.setheading(180)

turtle.forward(100)
turtle.setheading(270)

turtle.forward(100)

print(turtle.heading())
turtle.setheading(180)
print(turtle.heading())

turtle.shape('square') # Квадрат
turtle.forward(100)
turtle.setheading(90)

turtle.shape('arrow') # Стрелка
turtle.forward(100)
turtle.setheading(180)

turtle.shape('turtle') # Черепашка
turtle.forward(100)
turtle.setheading(270)

turtle.shape('circle') # Круг
turtle.forward(100)
turtle.setheading(0)

turtle.shape('triangle') # Треугольник
turtle.forward(100)
turtle.setheading(90)

turtle.shape('classic') # Треугольник
turtle.forward(100)
turtle.setheading(180)

# картинка находится в той же папке, что и исполняемая программа
picture_path = 'rocketship.gif'
turtle.Screen().addshape(picture_path)
turtle.shape(picture_path)

for _ in range(4):
    turtle.forward(150)
    turtle.left(270)