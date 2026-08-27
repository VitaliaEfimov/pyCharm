import turtle as t
t.showturtle()

t.fillcolor('blue')
t.begin_fill()
for _ in range(4):
    t.left(90)
    t.forward(100)
t.end_fill()

t.up()
t.goto(20, 100)
t.down()
t.fillcolor('brown')
t.begin_fill()
t.goto(-50, 180)
t.goto(-120, 100)
t.goto(20, 100)
t.end_fill()

t.done() # Окно останется открытым до его закрытия пользователем