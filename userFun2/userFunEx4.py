numbers = [4.12, 1.3257, 9.37037, 4.552, 3.186]

def map(f, l):
    r = []
    for i in l:
        x = f(i, 2)
        r.append(x)
    return r
for i in map(round, numbers):
    print(i)

print()
"""
4.12
1.33
9.37
4.55
3.19
"""

numbers = [854, 10, 5, 452, 478, 236, 202, 41]

def predicate(x):
    return 99 < x < 1000 and x % 5 == 2

def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)

    return result

def f(x):
    return x**3

filtered = filter(predicate, numbers)
mapped = map(f, filtered)
for i in mapped:
    print(i)
"""
92345408
8242408
"""
print()

numbers = [7, 5, -4, 0, 3, -5, 6, 7, 15]

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)

    return acc

def square_add(cur_sum, num):
    return cur_sum + num**2

square_sum = reduce(square_add, numbers, 0)
print(square_sum) # 434
print()

numbers = [14, 15, -1, 2, 0, -42, 36, 2]

def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)

    return result

def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)

    return result

def check(num):
    return 10 <= abs(num) <= 99 and num % 7 == 0

def square(num):
    return num**2

new_numbers = map(square, filter(check, numbers))
print(sum(new_numbers)) # 1960
print()

def func_apply(f, l):
    r = []
    for i in l:
        r.append(f(i))
    return r

print(func_apply(int, ['1', '2', '10'])) # [1, 2, 10]

