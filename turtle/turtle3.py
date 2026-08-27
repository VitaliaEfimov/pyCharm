"""
✅ Команда write() применяется для вывода текста в графическое окно. Левый нижний угол первого символа выведенного текста будет расположен в точке с координатами черепашки. Аргументы команды:

arg – текст, который нужно вывести;
move – указывает будет ли двигаться черепашка по мере рисования надписи (по умолчанию значение False);
align – служит для выравнивания надписи относительно черепашки, может принимать три строковых значения right, center, left (по умолчанию значению right);
font – кортеж из трех значений: (название шрифта, размер шрифта, тип начертания). В качестве начертания можно использовать строковые значения: normal — обычный, bold — полужирный, italic — курсив, или объединить два последних, тогда текст будет напечатан полужирным курсивом.
✅ Команды turtle.begin_fill() и turtle.end_fill() применяются для заливки геометрической фигуры цветом. turtle.begin_fill() применяется до начертания фигуры, а после завершения начертания используется команда turtle.end_fill() и геометрическая фигура заполняется текущим цветом заливки.

✅ Команда fillcolor() меняет цвет заливки. Аргумент команды — название цвета в виде строкового литерала, либо значения трех компонентов RGB.

✅ Команда turtle.Turtle() создаёт новый экземпляр класса Turtle(). Позволяет использовать несколько черепашек в одной программе.

✅ Команда turtle.tracer(n, delay) включает/выключает анимацию черепашки и устанавливает задержку для обновления рисунков.

✅ Команда onkey(fun, key) используется для отслеживания нажатия клавиш клавиатуры. Она связывает функцию обратного вызова fun с событием нажатия клавиши key.

✅ Команда turtle.Screen().listen() устанавливает фокус на экран черепашки.

✅ Команда onclick(fun) используется для отслеживания нажатия мыши. Она связывает функцию обратного вызова fun с событием нажатия левой кнопки мыши.
"""

import turtle

turtle.Screen().setup(1600, 800)
turtle.write('Пpивeт, мир!')
turtle.hideturtle()
turtle.goto(-120, 120)
turtle.write('Сверху')
turtle.goto(50, -120)
turtle.write('Снизу')
turtle.goto(100, 20)
turtle.write('Справа')

turtle.goto(-120, 120)
turtle.write('Сверху', move=True, align='center', font=('Arial', 17, 'bold'))
turtle.goto(50, -120)
turtle.write('Снизу', move=True, align='left', font=('Times New Roman', 25, 'normal'))
turtle.goto(100, 20)
turtle.write('Справа', move=True, align='right', font=('Helvetica', 20, 'italic'))

turtle.begin_fill()     # включаем заливку
turtle.circle(80)
turtle.end_fill()       # выключаем заливку

turtle.forward(100)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.goto(-120, -120)
turtle.fillcolor('green')

turtle.begin_fill()

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()

turtle.fillcolor('blue')

turtle.goto(-200, -200)
turtle.begin_fill()

turtle.goto(-150, -200)
turtle.goto(-150, -100)
turtle.goto(-180, -100)

turtle.end_fill()

turtle.done() # Окно останется открытым до его закрытия пользователем