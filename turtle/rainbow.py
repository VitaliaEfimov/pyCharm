import turtle as t

colors = ['red', 'orange', 'yellow', 'green', 'LightGreen','cyan', 'DeepSkyBlue','blue','purple', 'DeepPink']

def rainbow(r, step):
    x, y = 0, 0
    for i in range(len(colors)):
        t.fillcolor(colors[i])
        t.begin_fill()
        t.circle(r - step * i)
        t.end_fill()
        t.up()
        y = t.ycor() + step
        t.goto(x, y)

rainbow(100, 10)
t.done()