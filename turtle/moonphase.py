from turtle import *

Screen().bgcolor("blue")
hideturtle()

lst_t = [Turtle() for _ in range(2)]

for t in lst_t:
    t.penup()
    t.forward(200)
    t.hideturtle()

tracer(1, 0)

dot(200, "yellow")
for _ in range(800):
    for t in lst_t:
        t.backward(0.5)
        t.clear()
        t.dot(200, "blue")

done()