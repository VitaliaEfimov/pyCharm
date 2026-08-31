"""
✅ Позиционными называются аргументы, передаваемые без указания имён. Их значения сопоставляется с параметрами
функции по позиции.

✅ Именованными называются аргументы, передаваемые с указанием имени параметра. Порядок упоминания именованных
аргументов не имеет значения.

✅ Позиционные аргументы должны быть указаны до любых именованных.

✅ Необязательными называются параметры, имеющие значения по умолчанию.

✅ Значение по умолчанию для параметра создается единожды при определении функции (обычно при загрузке модуля)
и становится атрибутом (свойством) функции. Поэтому, если значение по умолчанию изменяемый объект, то его изменение
повлияет на каждый следующий вызов функции.
"""

def diff(x, y):
    return x - y


res = diff(10, 3)    # используем позиционные аргументы
print(res) # 7
res = diff(x=10, y=3)   # используем именованные аргументы
print(res) # 7
res = diff(y=3, x=10) # Порядок в случае именованных аргументов не важен
print(res) # 7

print('aaaa', 'bbbbb', sep='*', end='##')
print('cccc', 'dddd', sep='()')
print('eeee', 'ffff', sep='123', end='python')
"""
aaaa*bbbbb##cccc()dddd
eeee123ffffpython
"""
res = diff(10, y=3)   # используем позиционный и именованный аргумент
print(res)
# res = diff(x=10, 3)   # используем позиционный и именованный аргумент SyntaxError: positional argument follows keyword argument

num = int('101', 2)     # аргумент 2 указывает на то, что число 101 записано в двоичной системе
print(num)
print()

def increment(n, i=1):
    return n + i
print(increment(3)) # 4
print(increment(3, 2)) # 5
print()

def append(element, seq=[]):
    seq.append(element)
    return seq

print(append(10, [1, 2, 3])) # [1, 2, 3, 10]
print(append(5, [1])) # [1, 5]
print(append(1, [])) # [1]
print(append(3, [4, 5])) # [4, 5, 3]
print()

print(append(10)) # [10]
print(append(5)) # [10, 5]
print(append(1)) # [10, 5, 1]
print()
"""
Значение по умолчанию для параметра создается единожды при определении функции (обычно при загрузке модуля) и 
становится атрибутом (свойством) функции. Поэтому, если значение по умолчанию изменяемый объект, то 
го изменение повлияет на каждый следующий вызов функции.
"""
print('Значение по умолчанию', append.__defaults__) # Значение по умолчанию ([10, 5, 1],)
print(append(10)) # [10, 5, 1, 10]
print('Значение по умолчанию', append.__defaults__) # Значение по умолчанию ([10, 5, 1, 10],)
print(append(5)) # [10, 5, 1, 10, 5]
print('Значение по умолчанию', append.__defaults__) # Значение по умолчанию ([10, 5, 1, 10, 5],)
print(append(1)) # [10, 5, 1, 10, 5, 1]
print('Значение по умолчанию', append.__defaults__) # Значение по умолчанию ([10, 5, 1, 10, 5, 1],)
print()

def append(element, seq=None):
    if seq is None:
        seq = []
    seq.append(element)
    return seq

print(append(10)) # [10]
print(append(5)) # [5]
print(append(1)) # [1]
print()

def fancy(length, char1, char2):
    return (char1 + char2) * length + char1

print(fancy(5, '-', '*')) # -*-*-*-*-*-
print()

def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1

print(fancy(3)) # -*-*-*-
print()

print(fancy(3, '.')) # .*.*.*.
print(fancy(2, ':', '|')) # :|:|:
print(fancy(4, char2='#')) # -#-#-#-#-
print(fancy(char2='$', length=3)) # -$-$-$-
print(fancy(char2='!'))