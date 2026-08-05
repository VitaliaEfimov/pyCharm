"""
Объединение множеств – это множество, состоящее из элементов, принадлежащих хотя бы одному из объединяемых множеств. Для этой операции существует метод union(). Для объединения двух множеств можно также использовать оператор |.

✅ Пересечение множеств – это множество, состоящее из элементов, принадлежащих одновременно каждому из пересекающихся множеств. Для этой операции существует метод intersection(). Для пересечения двух множеств можно также использовать оператор &.

✅ Разность множеств – это множество, в которое входят все элементы первого множества, не входящие во второе множество. Для этой операции существует метод difference(). Для разности двух множеств можно также использовать оператор -.

✅ Симметрическая разность множеств – это множество, включающее все элементы исходных множеств, не принадлежащие одновременно обоим исходным множествам. Для этой операции существует метод symmetric_difference(). Для симметрической разности двух множеств можно также использовать оператор ^.

✅ Методы union(), intersection(), difference(), symmetric_difference() не изменяют исходные множества, а возвращают новые.

✅ Метод update() изменяет исходное множество по объединению. Аналогичный результат даёт использование оператора |=.

✅ Метод intersection_update() изменяет исходное множество по пересечению. Аналогичный результат даёт использование оператора &=.

✅ Метод difference_update() изменяет исходное множество по разности. Аналогичный результат даёт использование оператора -=.

✅ Метод symmetric_difference_update() изменяет исходное множество по симметрической разности. Аналогичный результат даёт использование оператора ^=.

Таблица соответствия методов и операторов над множествами
✅ Приоритет операторов в порядке убывания (верхние операторы имеют более высокий приоритет, чем нижние) имеет вид:

Оператор	Описание
-	        разность
&	        пересечение
^	        симметрическая разность
|	        объединение

A | B
A.union(B)

Возвращает множество, являющееся объединением множеств A и B
A |= B
A.update(B)

Добавляет в множество A все элементы из множества B
A & B
A.intersection(B)

Возвращает множество, являющееся пересечением множеств A и B
A &= B
A.intersection_update(B)

Оставляет в множестве A только те элементы, которые есть в множестве B
A - B
A.difference(B)

Возвращает разность множеств A и B
A -= B
A.difference_update(B)

Удаляет из множества A все элементы, входящие в B
A ^ B
A.symmetric_difference(B)

Возвращает симметрическую разность множеств A и B
A ^= B
A.symmetric_difference_update(B)

Записывает в A симметрическую разность множеств A и B
"""
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1.union(myset2)
print(myset3) # {1, 2, 3, 4, 5, 6, 7, 8}
myset3 = myset1 | myset2
print(myset3) # {1, 2, 3, 4, 5, 6, 7, 8}

myset3 = myset1.intersection(myset2)
print(myset3) # {3, 4}
myset3 = myset1 & myset2
print(myset3) # {3, 4}

myset3 = myset1.difference(myset2)
print(myset3) # {1, 2, 5}
myset3 = myset1 - myset2
print(myset3) # {1, 2, 5}
myset3 = myset2.difference(myset1)
print(myset3) # {8, 6, 7}

myset3 = myset1.symmetric_difference(myset2)
print(myset3) # {1, 2, 5, 6, 7, 8}
myset3 = myset1 ^ myset2
print(myset3) # {1, 2, 5, 6, 7, 8}

myset1.update(myset2)  # изменяем множество myset1
print(myset1) # {1, 2, 3, 4, 5, 6, 7, 8}

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset1 |= myset2
print(myset1) # {1, 2, 3, 4, 5, 6, 7, 8}

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset1.intersection_update(myset2)  # изменяем множество myset1
print(myset1) # {3, 4}

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset1 &= myset2
print(myset1) # {3, 4}

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset1.difference_update(myset2)  # изменяем множество myset1
print(myset1) # {1, 2, 5}

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset1 -= myset2
print(myset1) # {1, 2, 5}

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset1.symmetric_difference_update(myset2)  # изменяем множество myset1
print(myset1) # {1, 2, 5, 6, 7, 8}

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset1 ^= myset2
print(myset1) # {1, 2, 5, 6, 7, 8}

mylist = [2021, 2020, 2019, 2018, 2017, 2016]
mytuple = (2021, 2020, 2016)
mystr = 'abcd'

myset = {2009, 2010, 2016}
# Использование методов более безопасно, потому что при использовании операторов можем ловить ошибку
print(myset.union(mystr))                      # объединяем со строкой
print(myset.intersection(mylist))              # пересекаем со списком
print(myset.difference(mytuple))               # находим разность с кортежем
# print(myset | mystr) # TypeError: unsupported operand type(s) for |: 'set' and 'str'
# print(myset & mylist) # TypeError: unsupported operand type(s) for &: 'set' and 'list'
# print(myset - mytuple) # TypeError: unsupported operand type(s) for -: 'set' and 'tuple'

myset1 = {1, 2, 3, 4, 5, 6}
myset2 = {2, 3, 4, 5}
myset3 = {5, 6, 7, 8}

union1 = myset1.union(myset2, myset3)
union2 = myset1 | myset2 | myset3

difference1 = myset1.difference(myset2, myset3)
difference2 = myset1 - myset2 - myset3           # порядок выполнения слева-направо

print(union1 == union2) # True
print(difference1 == difference2) # True

myset1 = {1, 2, 3, 4, 5, 6}
myset2 = {2, 3, 4, 7}
myset3 = {6, 20, 30}

# symdifference = myset1.symmetric_difference(myset2, myset3) # TypeError: set.symmetric_difference() takes exactly one argument (2 given)
symdifference = myset1 ^ myset2 ^ myset3  # порядок выполнения слева-направо

print(symdifference) # {1, 5, 7, 20, 30}