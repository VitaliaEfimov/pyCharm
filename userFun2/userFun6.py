"""
✅ Анонимные функции (лямбда-функции) – это короткие однострочные функции с использованием оператора lambda.
✅ Общий формат определения анонимной функции:
lambda список_параметров: выражение,
где список_параметров – список параметров через запятую, выражение – значение, либо код, дающий значение.
✅ Когда применение анонимных функций оправдано:
однократное использование функции;
передача функций в качестве аргументов другим функциям;
возвращение функции в качестве результата другой функции.
✅ В теле анонимной функции можно использовать тернарный условный оператор:
значение1 if условие else значение2
Если условие истинно, возвращается значение1, если нет – значение2.
✅ Анонимные функции поддерживают все способы передачи аргументов:
позиционные аргументы;
именованные аргументы;
переменный список позиционных аргументов (*args);
переменный список именованных аргументов (**kwargs);
обязательные аргументы (*).
✅ Особенности и ограничения анонимных функций в Python:
анонимная функция может содержать только выражение, и не может включать в свое тело операторы;
в теле анонимной функции такие операторы, как return, pass, assert или raise, вызовут исключение SyntaxError;
анонимная функция пишется как одна строка исполнения;
анонимная функция может быть немедленно вызвана.
"""
def standard_function(x):            #  стандартное объявление функции
    return x*2

lambda_function = lambda x: x*2      #  объявление анонимной функции
print(standard_function(7)) # 14
print(lambda_function(7)) # 14
print()

f1 = lambda: 10 + 20               # функция без параметров
f2 = lambda х, у: х + у            # функция с двумя параметрами
f3 = lambda х, у, z: х + у + z     # функция с тремя параметрами

print(f1()) # 30
print(f2(5, 10)) # 15
print(f3(5, 10, 30)) # 45
print()

def compare_by_second(point):
    return point[1]

def compare_by_sum(point):
    return point[0] + point[1]

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа [(2, -4), (1, -1), (2, 3), (1, 5), (10, 9), (-10, 15), (7, 18)]
print(sorted(points, key=compare_by_sum))      # сортируем по сумме кортежа [(2, -4), (1, -1), (2, 3), (1, 5), (10, 9), (-10, 15), (7, 18)]
print()

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=lambda point: point[1]))                 # сортируем по второму значению кортежа [(2, -4), (1, -1), (2, 3), (1, 5), (10, 9), (-10, 15), (7, 18)]
print(sorted(points, key=lambda point: point[0] + point[1]))      # сортируем по сумме элементов кортежа [(2, -4), (1, -1), (2, 3), (-10, 15), (1, 5), (10, 9), (7, 18)]
print()

numbers = [1, 2, 3, 4, 5, 6]

new_numbers1 = list(map(lambda x: x+1, numbers))      #  увеличиваем на 1
new_numbers2 = list(map(lambda x: x*2, numbers))      #  удваиваем
new_numbers3 = list(map(lambda x: x**2, numbers))     #  возводим в квадрат

print(new_numbers1) # [2, 3, 4, 5, 6, 7]
print(new_numbers2) # [2, 4, 6, 8, 10, 12]
print(new_numbers3) # [1, 4, 9, 16, 25, 36]
print()

strings = ['a', 'b', 'c', 'd', 'e']
numbers = [3, 2, 1, 4, 5]

new_strings = list(map(lambda x, y: x*y, strings, numbers))

print(new_strings) # ['aaa', 'bb', 'c', 'dddd', 'eeeee']
print()

numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]

positive_numbers = list(filter(lambda x: x > 0, numbers))      #  положительные числа
large_numbers = list(filter(lambda x: x > 50, numbers))        #  числа, большие 50
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))     #  четные числа

print(positive_numbers) # [2, 4, 10, 30, 50, 100, 90]
print(large_numbers) # [100, 90]
print(even_numbers) # [2, 4, 0, -20, 10, 30, -40, 50, 100, 90]
print()

words = ['python', 'stepik', 'beegeek', 'iq-option']

new_words1 = list(filter(lambda w: len(w) > 6, words))    #  слова длиною больше 6 символов
new_words2 = list(filter(lambda w: 'e' in w, words))      #  слова содержащие букву e

print(new_words1) # ['beegeek', 'iq-option']
print(new_words2) # ['stepik', 'beegeek']
print()

from functools import reduce

words = ['python', 'stepik', 'beegeek', 'iq-option']
numbers = [1, 2, 3, 4, 5, 6]

summa = reduce(lambda x, y: x + y, numbers, 0)
product = reduce(lambda x, y: x * y, numbers, 1)
sentence = reduce(lambda x, y: x + ' loves ' + y, words, 'Everyone')

print(summa) # 21
print(product) # 720
print(sentence) # Everyone loves python loves stepik loves beegeek loves iq-option
print('Everyone loves ' + ' loves '.join(words)) # Everyone loves python loves stepik loves beegeek loves iq-option
print()

def generator_square_polynom(a, b, c):
    return lambda x: a*x**2 + b*x + c

print(generator_square_polynom(3, 2, 6)(3)) # 39
print()

numbers = [-2, 0, 1, 2, 17, 4, 5, 6]

result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))

print(result) # ['even', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
print()

f1 = lambda x, y, z: x + y + z
f2 = lambda x, y, z=3: x + y + z
f3 = lambda *args: sum(args)
f4 = lambda **kwargs: sum(kwargs.values())
f5 = lambda x, *, y=0, z=0: x + y + z

print(f1(1, 2, 3)) # 6
print(f2(1, 2)) # 6
print(f2(1, y=2)) # 6
print(f3(1, 2, 3, 4, 5)) # 15
print(f4(one=1, two=2, three=3)) # 6
print(f5(1)) # 1
print(f5(1, y=2, z=3)) # 6
print()

print((lambda х, у: х + у)(5, 10))     # 15
print(1 + (lambda x: x*5)(10) + 2)     # 53
print()

f = lambda x: x + 1
print(type(f)) # <class 'function'>
print()

result = list(map(lambda x: x.split(), ['a', 'a b', 'a b c']))
print(result) # [['a'], ['a', 'b'], ['a', 'b', 'c']]
print()

is_non_negative_num = lambda x: x.count('.') < 2 and len([i for i in x if i.isalpha()]) == 0 and float(x) >= 0
print(is_non_negative_num('10.34ab')) # False
print(is_non_negative_num('10.45')) # True
print()

floats = [7.6, 15.4, 8.9, -5.6, 42.1]
words = ['pop', 'level', 'python', 'huh']
numbers = [4, -8, 5, 12, -85]

map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result) # [57.8, 237.2, 79.2, 31.4, 1772.4]
print(filter_result) # ['level']
print(reduce_result) # 163200
print()

data = [
    ['Sydney', 5367206, 'primary'], ['Perth', 2384371, 'nan'],
    ['Melbourne', 5159211, 'nan'], ['Canberra', 466566, 'admin'],
    ['Darwin', 127532, 'nan'], ['Jakarta', 41913860, 'admin'],
    ['Kolkata', 22549738, 'primary'], ['Shenzhen', 13878396, 'primary'],
]
def compare_by_sity(item):
    return item[0]
print('Cities: ' + ', '.join(i[0] for i in sorted(list(filter(lambda x: x[1] > 10000000 and x[2] == 'primary', data)), key=compare_by_sity))) # Cities: Kolkata, Shenzhen
print()

def is_num(x):
    return x.count('.') < 2 and len([i for i in x if i.isalpha()]) == 0 and ( x.count('-') ==0 or x.count('-') == 1 and x.find('-') == 0)

print(is_num('10.34ab')) # False
print(is_num('1-1')) # False
print(is_num('-34.67')) # True
print(is_num('123.122.12')) # False

words = [
    'abandon', 'besides', 'access', 'friday',
    'bestow', 'abound', 'absent', 'beware',
    'abundant', 'abnormal', 'aboard', 'about',
    'accelerate', 'abort', 'thursday', 'tuesday',
    'sunday', 'berth', 'beyond', 'benevolent',
    'abate', 'abide', 'bicycle', 'beside',
    'accept', 'berry', 'bewilder', 'abrupt',
    'saturday', 'accessory', 'absorb',
]

some_words = sorted(filter(lambda x: len(x) == 6, words))
print(*some_words) # aboard abound abrupt absent absorb accept access beside bestow beware beyond friday sunday


