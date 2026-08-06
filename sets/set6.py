"""
✅ Общий вид генератора множеств следующий:

{выражение for переменная in последовательность if условие},


где выражение – некоторое выражение, как правило, зависящее от использованной в генераторе множеств переменной,
которым будут заполнены элементы множества, переменная – имя некоторой переменной, последовательность –
последовательность значений, которые она принимает (любой итерируемый объект), условие (необязательное) –
в множество попадут элементы, для которых условие истинно.

✅ Замороженное множество (frozenset) также является встроенной коллекцией в Python. Обладая характеристиками обычного множества, замороженное множество не может быть изменено после создания.

✅ Функция frozenset() используется для создания замороженного множества. Она принимает в качестве аргумента другую коллекцию.

✅ Над замороженными множествами можно производить все операции, которые можно производить над обычными множествами:

Объединение множеств: метод union() или оператор |;
пересечение множеств: метод intersection() или оператор &;
разность множеств: метод difference() или оператор -;
симметрическая разность множеств: метод symmetric_difference() или оператор ^.
✅ Отсутствующие методы у замороженных множеств: add(), remove(), discard(), pop(), clear(), update(), intersection_update(), difference_update(), symmetric_difference_update()
✅ Результатом операций над замороженными множествами будут замороженные множества.

✅ Методы, изменяющие множество, отсутствуют у замороженных множеств.
"""
digits = {int(c) for c in '12345'}
print(type(digits)) # <class 'set'>
print(digits) # {1, 2, 3, 4, 5}
squares = {i ** 2 for i in range(10)}
cubes = {i ** 3 for i in range(10)}
chars = {c for c in 'abcdefg'}
print(type(squares)) # <class 'set'>
print(type(cubes)) # <class 'set'>
print(type(chars)) # <class 'set'>
print(digits) # {1, 2, 3, 4, 5}
print(squares) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(cubes) # {0, 1, 64, 512, 8, 343, 216, 729, 27, 125}
print(chars) # {'e', 'a', 'f', 'c', 'd', 'b', 'g'}
digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}
print(type(digits)) # <class 'set'>
print(digits) # {0, 1, 2, 7, 8, 9}
sentence = 'Очевидно, он вылетел до начала урагана, но первые предвестники его появились еще восемнадцатого марта; следовательно, шар, мчавшийся со скоростью не менее двух тысяч миль в сутки, должен был прилететь из очень далеких краев.'
def exlsymb(s):
    return ''.join([a for a in s if a.isalpha()]) # был в до его еще из не но он со шар

print(*sorted({exlsymb(w.lower()) for w in sentence.split() if len(exlsymb(w)) < 4}))

myset1 = frozenset({1, 2, 3})                         # на основе множества
myset2 = frozenset([1, 1, 2, 3, 4, 4, 4, 5, 6, 6])    # на основе списка
myset3 = frozenset('aabcccddee')                      # на основе строки

print(myset1) # frozenset({1, 2, 3})
print(myset2) # frozenset({1, 2, 3, 4, 5, 6})
print(myset3) # frozenset({'b', 'e', 'd', 'a', 'c'})

myset1 = frozenset('hello')
myset2 = frozenset('world')

print(myset1 | myset2) # frozenset({'l', 'd', 'w', 'e', 'h', 'o', 'r'}) Результатом операций над замороженными множествами будут тоже замороженные множества.
print(myset1 & myset2) # frozenset({'o', 'l'})
print(myset1 ^ myset2) # frozenset({'e', 'd', 'w', 'r', 'h'})

sentence = 'The cat in the hat had two sidekicks, thing one and thing two.'

words = sentence.lower().replace('.', '').replace(',', '').split()

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}
# Будучи изменяемыми, обычные множества не могут быть элементами других множеств. Замороженные множества являются неизменяемыми, а значит могут быть элементами других множеств.
print(consonants) # {frozenset({'h', 'd'}), frozenset({'n', 'd'}), frozenset({'s', 'c', 'k', 'd'}), frozenset({'t', 'h'}), frozenset({'n'}), frozenset({'n', 't', 'h', 'g'}), frozenset({'w', 't'}), frozenset({'c', 't'})}

myset1 = set('qwerty')
myset2 = frozenset('qwerty')

print(myset1 == myset2) # True Мы можем сравнивать простые (тип set) и замороженные множества (тип frozenset).