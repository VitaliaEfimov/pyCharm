"""
✅ Функции высшего порядка — это функции, которые принимают другие функции в качестве аргументов и/или возвращают функции в качестве результата.

✅ Предикат — это функция-критерий, которая возвращает значение True или False.

✅ Агрегация результата — формирование одного результирующего значения при комбинации элементов с использованием аргумента-аккумулятора.
"""
def high_order_function(func):     # функция высшего порядка, так как принимает функцию
    return func(3)

def double(x):                     # обычная функция = функция первого порядка
    return 2*x

def add_one(x):                    # обычная функция = функция первого порядка
    return x + 1

print(high_order_function(double)) # 6
print(high_order_function(add_one)) # 4
print()

def f(x):
    return x**2     # тело функции, которая преобразует аргумент x

old_list = [1, 2, 4, 9, 10, 25]
new_list = []
for item in old_list:
    new_item = f(item)
    new_list.append(new_item)

print(old_list) # [1, 2, 4, 9, 10, 25]
print(new_list) # [1, 4, 16, 81, 100, 625]
print()

def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)

    return result

def square(x):
    return x**2

def cube(x):
    return x**3

numbers = [1, 2, -3, 4, -5, 6, -9, 0]

strings = map(str, numbers)        # используем в качестве преобразователя - функцию str
abs_numbers = map(abs, numbers)    # используем в качестве преобразователя - функцию abs
squares = map(square, numbers)     # используем в качестве преобразователя - функцию square
cubes = map(cube, numbers)         # используем в качестве преобразователя - функцию cube

print(strings) # ['1', '2', '-3', '4', '-5', '6', '-9', '0']
print(abs_numbers) # [1, 2, 3, 4, 5, 6, 9, 0]
print(squares) # [1, 4, 9, 16, 25, 36, 81, 0]
print(cubes) # [1, 8, -27, 64, -125, 216, -729, 0]
print()

strings = ['10', '12', '-4', '-9', '0', '1', '23', '100', '99']

numbers1 = [int(c) for c in strings]  # используем списочное выражение для преобразования
numbers2 = map(int, strings)          # используем функцию map() для преобразования

print(numbers1) # [10, 12, -4, -9, 0, 1, 23, 100, 99]
print(numbers2) # [10, 12, -4, -9, 0, 1, 23, 100, 99]
print()

numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']

new_numbers = map(abs, map(int, numbers))

print(new_numbers) # [1, 20, 3, 94, 65, 6, 970, 8]
print()

def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)  # добавляем элемент item если функция function вернула значение True

    return result

def is_greater10(num):  # функция возвращает значение True если число больше 10 и False в противном случае
    return num > 10

numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]

large_numbers = filter(is_greater10, numbers)  #  список large_numbers содержит элементы, большие 10

print(large_numbers) # [12, 48, 51, 19, 13]
print()

def is_odd(num):
    return num % 2

def is_word_long(word):
    return len(word) > 6

numbers = list(range(15))
words = ['В', 'новом', 'списке', 'останутся', 'только', 'длинные', 'слова']

odd_numbers = filter(is_odd, numbers)
large_words = filter(is_word_long, words)

print(odd_numbers) # [1, 3, 5, 7, 9, 11, 13]
print(large_words) # ['останутся', 'длинные']
print()

numbers = [1, 2, 3, 4, 5]

total = 0
product = 1

for num in numbers:
    total += num
    product *= num

print(total) # 15
print(product) # 120
print()

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)

    return acc

def add(x, y):
    return x+y

def mult(x, y):
    return x*y

numbers = [1, 2, 3, 4, 5]

total = reduce(add, numbers, 0)
product = reduce(mult, numbers, 1)

print(total) # 15
print(product) # 120
print()

def predicate(word):
    return word == word[::-1]

def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
filtered = filter(predicate, words)
print(filtered) # ['abba', 'a', 'deed', 'nun', 'level', 'deified', 'bbbbb', '1234321']
print(len(filtered)) # 8
print()

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

words_len = map(len, words)
print(words_len) # [4, 6, 6, 1, 4, 3, 5, 8, 7, 5, 6, 6, 7, 7]
print(max(words_len)) # 8
print()

def high_order_function(func):
    return func(10)

def square(x):
    return x**2

def minus_one(x):
    return x - 1

num1 = high_order_function(square)
num2 = high_order_function(minus_one)

print(num1*num2) # 900
print()

numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

var1 = max(numbers, key=abs)
print(var1) # -99
var2 = min(map(abs, numbers))
print(var2) # 2

print(var1 + var2) # -97