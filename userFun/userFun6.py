from math import pi

def get_powers(num):
    return num**2, num**3, num**4

def f():
    return 1, 2

def get_circle(radius):
    return 2 * pi * radius, pi * radius ** 2

# Построение равнобедренного треугольника
def draw_triangle():
    h = 8
    a = 15
    for i in range(h):
        print(' '*(a//2 - i) + '*' + '*' * (i*2) + ' '*(a//2 - i))

draw_triangle()

a = f() # Можно получить все элементы одним кортежем
print(a)
print(type(a))  # <class 'tuple'>

a, b, c = get_powers(2)
print(a)
print(b)
print(c)

# a, b = get_powers() # TypeError: get_powers() missing 1 required positional argument: 'num'
# a, b = get_powers(3) # ValueError: too many values to unpack (expected 2)
# a, b, c, d = get_powers(3) # ValueError: not enough values to unpack (expected 4, got 3)

print(get_circle(1))