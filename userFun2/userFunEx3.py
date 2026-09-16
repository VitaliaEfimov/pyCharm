numbers = [(0, 0), (1, 1), (2, 2, 2), (3,)]

def comp(t):
    return sum(t)/len(t)
print(min(numbers, key=comp)) # (0, 0)
print(max(numbers, key=comp)) # (3,)
print()

from math import *

def comp(t):
    return sqrt(t[0]**2 + t[1]**2)
points = [(3, 4), (-2, 1), (0, 1), (5, 12)]
points.sort(key=comp)
print(points) # [(0, 1), (-2, 1), (3, 4), (5, 12)]
print()

numbers = [(1, 5), (0, -1, 3), (5, 7, 15)]
def comp(t):
    return min(t) + max(t)
numbers.sort(key=comp)
print(numbers) # [(0, -1, 3), (1, 5), (5, 7, 15)]
print()

def f1(t):
    return t[0]
def f2(t):
    return t[1]
def f3(t):
    return t[2]
def f4(t):
    return t[3]
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
n = 2
com = {1: f1, 2: f2, 3: f3, 4: f4}
athletes.sort(key = com[n])
for i in athletes:
    print(*i)
"""
Руслан 9 140 33
Дима 10 130 35
Рустам 10 128 30
Тимур 11 135 39
Петя 15 190 90
Амир 16 170 70
Рома 16 188 100
Матвей 17 168 68
"""
print()

from math import *
def sq(n):
    return n**2
def cub(n):
    return n**3
def sqrtx(n):
    return sqrt(n)
def absx(n):
    return abs(n)
def sinx(n):
    return sin(n)
fs = {'квадрат': sq, 'куб': cub, 'корень': sqrtx, 'модуль': absx, 'синус': sinx}
print(fs['квадрат'](2)) # 4
print(fs['куб'](2)) # 8
print(fs['корень'](4)) # 2.0
print(fs['модуль'](-20)) # 20
print(fs['синус'](64.4259)) # 0.9997297169434205
print()

def com(s):
    su = 0
    for i in s:
        su += int(i)
    return su
l = '12 14 79 7 4 123 45 90 111'.split()
l.sort(key=com)
print(*l)
print()

def com(s):
    su = 0
    for i in s:
        su += int(i)
    return (su, len(s), s)
l = '19 20 21 22 23 10 11 12 13 14 15 16 17 18'.split()
l.sort(key=com)
print(*l)