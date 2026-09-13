"""
✅ Парадигма программирования (подход к программированию) — совокупность идей и понятий, определяющих стиль написания компьютерных программ.

✅ Парадигма программирования определяется:

вычислительной моделью;
базовой программной единицей (-ами);
методами разделения абстракций.
✅ Язык программирования Python – мультипарадигменный.

✅ Основные парадигмы программирования:

императивное программирование;
структурное программирование;
объектно-ориентированное программирование;
функциональное программирование;
логическое программирование.

✅ Любая функция в языке Python — объект типа function.

✅ Работать с функциями можно как и с другими объектами: записывать их в переменные, передавать в качестве аргументов другим функциям, возвращать из функций и т.д.

✅ Функции высшего порядка – это функции, которые принимают другие функции в качестве аргументов и/или возвращают функции в качестве результата.

✅ Встроенные функции min(), max(), sorted() могут принимать необязательный аргумент key – функцию, определяющую условия сравнения элементов. Другими словами, значение key должно быть функцией, принимающей один аргумент и возвращающей на его основе ключ для сравнения.

✅ Функция, определяющая условия сравнения элементов, называется компаратор (compare – сравнивать).

✅ Замыкания – вложенные функции, ссылающиеся на переменные, объявленные вне определения этой функции, и не являющиеся её параметрами.
"""
num = 17
numbers = [1, 2, 3]
colors = (1, 2, 3)
name = 'Python'

print(type(num)) # <class 'int'>
print(type(numbers)) # <class 'list'>
print(type(colors)) # <class 'tuple'>
print(type(name)) # <class 'str'>
print()

print(type(print)) # <class 'builtin_function_or_method'>
print(type(sum)) # <class 'builtin_function_or_method'>
print(type(abs)) # <class 'builtin_function_or_method'>
print()

def hello():
    print('Hello from function')

print(type(hello)) # <class 'function'>
print()

func = hello     #  присваиваем переменной func функцию hello
func()           #  Hello from function - вызываем функцию
print()

writeln = print            # как в языке Pascal 😀

writeln('Hello world!') # Hello world!
writeln('Python') # Python
print()

def start():
    print('start function')
    pass


def stop():
    print('stop function')
    pass


def pause():
    print('pause function')
    pass


commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция

command = 'start'  # считываем название команды

commands[command]()  # вызываем нужную функцию через словарь по ключу
print()

numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(max(numbers, key=abs))        # -210 указываем функцию abs в качестве компаратора
print(min(numbers, key=abs))        # -7 указываем функцию abs в качестве компаратора
print(sorted(numbers, key=abs))     # [-7, 8, 10, 32, -50, 87, -100, 117, -210] указываем функцию abs в качестве компаратора
print()

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
points.sort()    #  сортируем список точек на месте

print(points) # [(-10, 15), (1, -1), (1, 5), (2, -4), (2, 3), (7, 18), (10, 9)]
print()

def compare_by_second(point):
    return point[1]


def compare_by_sum(point):
    return point[0] + point[1]


points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))   # [(2, -4), (1, -1), (2, 3), (1, 5), (10, 9), (-10, 15), (7, 18)] сортируем по второму значению кортежа
print(sorted(points, key=compare_by_sum))      # [(2, -4), (1, -1), (2, 3), (-10, 15), (1, 5), (10, 9), (7, 18)] сортируем по сумме кортежа
print()

def generator():
    def hello():
        print('Hello from function!')
    return hello

func = generator()
func() # Hello from function!
print()

def generator_square_polynom(a, b, c):
    def square_polynom(x): # замыкание - вложенная функция, ссылающиеся на переменные, объявленные вне определения этой функции, и не являющиеся её параметрами.
        return a * x**2 + b * x + c

    return square_polynom # мы создали функцию по входящим параметрам внешнего метода

f = generator_square_polynom(a=1, b=2, c=1)
g = generator_square_polynom(a=2, b=0, c=-3)
h = generator_square_polynom(a=-3, b=-10, c=50)

print(f(1)) # 4
print(g(2)) # 5
print(h(-1)) # 57
print()

def comparator(item):
    return item[0]

data = [('red', 1), ('blue', 2), ('green', 5), ('blue', 1)]
data.sort(key=comparator)   # сортируем по первому полю

print(data) # [('blue', 2), ('blue', 1), ('green', 5), ('red', 1)]
data1 = [('red', 1), ('blue', 2), ('green', 5), ('blue', 1)]
data1.sort()
print(data1) # [('blue', 1), ('blue', 2), ('green', 5), ('red', 1)]
print()

print(input) # <built-in function input>


