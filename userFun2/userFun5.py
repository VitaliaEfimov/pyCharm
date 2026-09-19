"""
✅ Встроенная функция map(func, iterable, *iterables) возвращает итератор с результатами применения функции func к
элементам итерируемого объекта iterable. Если передано несколько итерируемых объектов, в функцию func будут передаваться
сразу несколько элементов, расположенных на одинаковых позициях.

✅ Встроенная функция filter(func, iterable) возвращает итератор, содержащий только те элементы итерируемого объекта
iterable, для которых функция func возвращает True. Если вместо func указать None, каждый элемент будет проверен на
соответствие значению True.

✅ Функция reduce(func, iterable, initializer=None) из модуля functools последовательно применяет функцию func к
элементам итерируемого объекта iterable слева направо, сводя его к одному значению. Начальное значение задаётся через
initializer. Если начальное значение не установлено, то в его качестве используется первое значение iterable.

✅ Итераторы – важная концепция языка Python. Нужно помнить:
итераторы можно обойти циклом for;
итератор можно преобразовать в список или кортеж, с помощью функций list() и tuple();
итератор можно распаковать с помощью *.
✅ Список некоторых функций из модуля operator:
Операция	        Синтаксис	        Функция
Addition	        a + b	            add(a, b)
Containment Test	obj in seq	        contains(seq, obj)
Division	        a / b	            truediv(a, b)
Division	        a // b	            floordiv(a, b)
Exponentiation	    a ** b	            pow(a, b)
Modulo	            a % b	            mod(a, b)
Multiplication	    a * b	            mul(a, b)
Negation (Arithmetic)-a	                neg(a)
Subtraction	        a - b	            sub(a, b)
Ordering	        a < b	            lt(a, b)
Ordering	        a <= b	            le(a, b)
Equality	        a == b	            eq(a, b)
Difference	        a != b	            ne(a, b)
Ordering	        a >= b	            ge(a, b)
Ordering	        a > b	            gt(a, b)
"""
iterable = ['1', '2', '3']
result = list(map(len, iterable))
print(result) # [1, 1, 1]
print()

iterable = [[1], [2], [3]]
result = list(map(len, iterable))
print(result) # [1, 1, 1]
print()

list1 = list(map(len, ['this', 'is', 'a', 'test']))
list2 = [len(word) for word in ['this', 'is', 'a', 'test']]

print(list1 == list2) # True
print()

iterable = [1, 2, 3]
# result = list(map(len, iterable)) # TypeError: object of type 'int' has no len()
# print(result)

def is_a_student(score):
    return score > 75


scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 75]
over_75 = list(filter(is_a_student, scores))

print(over_75) # [90, 76, 88, 81]
print()

def filter_vowels(letter):
    return letter in 'aeiou'


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

filtered_vowels = filter(filter_vowels, letters)

print(*filtered_vowels) # a e i o
print()

random_list = [1, 'a', 0, False, True, '0', 7, '']
filtered_list = list(filter(None, random_list))
print(filtered_list) # [1, 'a', True, '0', 7]
print()

listA = [2, 3, 4]
listB = [3, 2, 1]

result = sum(map(pow, listA, listB))
print(result) # 21
print()

from operator import mul
from functools import reduce

result = reduce(mul, range(1, 6))
print(result) # 120
print()

from functools import reduce
from operator import add
# range(1, 6) создает [1, 2, 3, 4, 5]
result = reduce(add, range(1, 6))
print(result) # 15
print()

from operator import add

result = list(map(add, 'abc', '1234'))
print(result) # ['a1', 'b2', 'c3']
print()

from operator import mul

result = list(map(mul, ['a', 'b', 'c'], [1, 2, 3]))
print(result) # ['a', 'bb', 'ccc']
print()

from operator import add
from functools import reduce

result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


