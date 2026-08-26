import turtle

turtle.Screen().setup(400, 400)             # устанавливаем размер граф. окна
turtle.Screen().addshape('rocketship.gif')  # добавляем форму черепашки

turtle.Screen().bgpic('space.png')          # устанавливаем фоновое изображение
turtle.shape('rocketship.gif')              # устанавливаем форму черепашки
turtle.pencolor('green')
turtle.pensize(5)

for _ in range(4):
    turtle.forward(150)
    turtle.left(90)

turtle.shape('turtle')

for i in range(3):
    turtle.forward(50)
    turtle.stamp()

turtle.clear() # стирает все рисунки в графическом окне. Но не меняет положение черепашки, цвет рисунка и цвет фона графического окна.
turtle.forward(100)
turtle.reset() # стирает все рисунки, имеющиеся в графическом окне, задает черный цвет рисунка и возвращает черепашку в исходное положение в центре экрана. Эта команда не переустанавливает цвет фона графического окна.
turtle.forward(100)
turtle.clearscreen() # стирает все рисунки в графическом окне, меняет цвет рисунка на черный, а цвет фона на белый, и возвращает черепашку в исходное положение в центре графического окна.

turtle.done() # Окно останется открытым до его закрытия пользователем