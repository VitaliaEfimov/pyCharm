"""
✅ Позиционные аргументы можно получать в виде *args. Аргументы собираются в кортеж от текущей позиции до конца.
Позволяет передавать функции переменное количество позиционных аргументов.

✅ Именованные аргументы можно получать в виде **kwargs. Аргументы собираются в словарь, где ключ — имя, а значение —
переданный аргумент. Позволяет передавать функции переменное количество именованных аргументов.

✅Keyword-only аргументы — это аргументы, которые можно передавать только по имени. Чтобы задать их, в определении
функции используют символ * как разделитель: он отделяет обычные аргументы (их можно указывать по имени и позиционно)
от строго именованных.
"""
print('a') # a
print('a', 'b') # a b
print('a', 'b', 'c') # a b c
print('a', 'b', 'c', 'd') # a b c d

def my_func(*args):
    print(type(args))
    print(args)
print()

my_func() # <class 'tuple'> \n ()
my_func(1, 2, 3) # <class 'tuple'> \n (1, 2, 3)
my_func('a', 'b') # <class 'tuple'> \n ('a', 'b')
print()

# print()
# def my_func(*args, num):
#     print(args)
#     print(num)

# my_func(1, 2, 3) # TypeError: my_func() missing 1 required keyword-only argument: 'num'

def my_func(num, *args):
    print(args)
    print(num)


my_func(17, 'Python', 2, 'C#') # ('Python', 2, 'C#') \n 17
print()
my_func(17) # () \n 17
print()

sum1 = sum([1, 2, 3, 4])        # считаем сумму чисел в списке
sum2 = sum((10, 20, 30, 40))    # считаем сумму чисел в кортеже

print(sum((10, 20, 30, 40), 1)) # 101, 1 - стартовый элемент, к нему добавляется сумма
print(sum1, sum2) # 10 100
print()

# sum1 = sum(1, 2, 3, 4) # TypeError: sum() takes at most 2 arguments (4 given)

def my_sum(*args):
    return sum(args)    # args - это кортеж

print(my_sum()) # 0
print(my_sum(1)) # 1
print(my_sum(1, 2)) # 3
print(my_sum(1, 2, 3)) # 6
print(my_sum(1, 2, 3, 4)) # 10
print()
print(my_sum(*[1, 2, 3, 4, 5]))   # 15 распаковка списка
print(my_sum(*(1, 2, 3)))         # 6 распаковка кортежа
print(my_sum(1, 2, *[3, 4, 5], *(7, 8, 9), 10)) # 49 распаковка вместе с аргументами
print()

def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)

my_func()
my_func(a=1, b=2)
my_func(name='Timur', job='Teacher')
"""
<class 'dict'>
{}
<class 'dict'>
{'a': 1, 'b': 2}
<class 'dict'>
{'name': 'Timur', 'job': 'Teacher'}
"""
print()

def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
    print(a, b)
    print(args)
    print(name, age)
    print(kwargs)

my_func(1, 2, 3, 4, name='Timur', age=28, job='Teacher', language='Python')
my_func(1, 2, name='Timur', age=28, job='Teacher', language='Python')
my_func(1, 2, 3, 4, job='Teacher', language='Python')
"""
1 2
(3, 4)
Timur 28
{'job': 'Teacher', 'language': 'Python'}

1 2
()
Timur 28
{'job': 'Teacher', 'language': 'Python'}

1 2
(3, 4)
Gvido 17
{'job': 'Teacher', 'language': 'Python'}
"""
print()

def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)

info = {'name':'Timur', 'age':'28', 'job':'teacher'}

my_func(**info)
print()

def print_info(name, surname, age, city, *children, **additional_info):
    print('Имя:', name)
    print('Фамилия:', surname)
    print('Возраст:', age)
    print('Город проживания:', city)
    if len(children) > 0:
        print('Дети:', ', '.join(children))
    if len(additional_info) > 0:
        print(additional_info)

children = ['Бодхи Рансом Грин', 'Ноа Шэннон Грин', 'Джорни Ривер Грин']
additional_info = {'height':163, 'job':'actress'}

print_info('Меган', 'Фокс', 34, 'Ок-Ридж', *children, **additional_info) # порядок *args **kwargs
"""
Имя: Меган
Фамилия: Фокс
Возраст: 34
Город проживания: Ок-Ридж
Дети: Бодхи Рансом Грин, Ноа Шэннон Грин, Джорни Ривер Грин
{'height': 163, 'job': 'actress'}
"""
def make_circle(x, y, radius, *, line_width=1, fill=True):
    pass
make_circle(10, 20, 5)                                     # x=10, y=20, radius=5,  line_width=1, fill=True
make_circle(x=10, y=20, radius=7)                          # x=10, y=20, radius=7,  line_width=1, fill=True
make_circle(10, 20, radius=10, line_width=2, fill=False)   # x=10, y=20, radius=10, line_width=2, fill=False
make_circle(x=10, y=20, radius=17, line_width=3)           # x=10, y=20, radius=17, line_width=3, fill=True

# make_circle(10, 20, 15, 20) # SyntaxError: positional argument follows keyword argument
# make_circle(x=10, y=20, 15, True) # SyntaxError: positional argument follows keyword argument
# make_circle(10, 20, 10, 2, False) # SyntaxError: positional argument follows keyword argument

def make_circle(*, x, y, radius, line_width=1, fill=True):
    pass

make_circle(x=10, y=20, radius=15)                              # line_width=1, fill=True
make_circle(x=10, y=20, radius=15, line_width=4, fill=False) # Такой разделитель можно использовать только один раз в определении функции