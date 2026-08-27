import turtle as t

def rectangle(width, height):
    t.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            t.forward(width)
        else:
            t.forward(height)
        t.right(90)
    t.end_fill()

def traffic_lights(width, height, r):
    colors = ['red', 'yellow', 'green']

    rectangle(width, height)

    x = width / 2
    step = -(height + 2 * r) / 4
    y = step

    for color in colors:
        t.goto(x, y)
        t.down()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.up()
        y += step

traffic_lights(100, 300, 25)