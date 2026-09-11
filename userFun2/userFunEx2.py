def count_args(*args):
    return len(args)

print(count_args([], (''), 'a', 12, False)) # 5
print()

def sq_sum(*args):
    return sum([i**2 for i in args])

print(sq_sum(4, 5, 6, 7)) # 126
print()

def mean(*args):
    c = 0
    s = 0
    for i in args:
        if type(i) in (int, float):
            c+=1
            s+=i
    if s == 0:
        return 0
    else:
        return s/c

print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2))) # 2.0
print()

def greet(*args):
    return 'Hello, ' + ' and '.join(args) + '!'

print(greet('Timur', 'Roman', 'Ruslan')) # Hello, Timur and Roman and Ruslan!
print()

def print_products(*args):
    prods = [s for s in args if type(s) is str and len(s) != 0]
    if prods:
        i = 1
        for p in prods:
            print(f'{i}) {p}')
            i += 1
    else:
        print('Нет продуктов')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
"""
1) Бананы
2) Яблоки
3) Макароны
"""
print()

def info_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f'{k}: {v}')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
"""
age: 28
first_name: Timur
job: teacher
last_name: Guev
"""