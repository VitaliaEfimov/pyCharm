from math import cos, sin
from turtle import *

begin_fill()
fillcolor('#FF2600')
for i in range(628):
    t = i / 100
    x = 128*sin(t)**3
    y = 8*(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t) - 5)
    goto(x, y)
end_fill()
done()