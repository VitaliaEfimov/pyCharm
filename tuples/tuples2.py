"""
Перебор элементов кортежа осуществляется точно так же, как и перебор элементов списка, то есть с помощью цикла for.

✅ Кортежи можно сравнивать между собой. При этом операции <, >, <=, >= применимы только в том случае,
если соответствующие элементы кортежей имеют один тип. Операции == и != применимы к любым кортежам, независимо от типов элементов.
Сравнение кортежей происходит последовательно элемент за элементом, а если элементы равны — просматривается следующий элемент.

✅ Кортеж можно преобразовать в список с помощью функции list().

✅ Список можно преобразовать в кортеж с помощью функции tuple().

✅ Кортеж можно преобразовать в строку с помощью строкового метода join().

✅ Строку можно преобразовать в кортеж с помощью функции tuple().

✅ Упаковкой кортежа называют присваивание его какой-либо переменной.

✅ Распаковкой кортежа называют присвоение значений элементов кортежа отдельным переменным.
Количество переменных должно совпадать с числом элементов в кортеже. Распаковывать можно не только кортеж,
правая сторона может быть любой последовательностью (кортеж, строка или список).

✅ Звёздочка * перед именем переменной позволяет собрать в неё несколько значений при распаковке кортежа.
Она может использоваться только у одной переменной в выражении. В такую переменную всегда записывается список,
даже если в него попадает всего один элемент или ни одного.
"""
print((1, 8) == (1, 8)) # True
print((1, 8) != (1, 10)) # True
print((1, 9) < (1, 2)) # False
print((2, 5) < (6,)) # True
print(('a', 'bc') > ('a', 'de')) # False
#print((7, 5) < ('java', 'python')) # TypeError: '<' not supported between instances of 'int' and 'str'
not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
print(not_sorted_tuple)
sorted_tuple = tuple(sorted(not_sorted_tuple)) # Метод sorted возвращает лист - необходимо явное преобразование к tuple
print(sorted_tuple)

notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
string1 = ''.join(notes) # Работает только на строковых элементах, если другой тип, нужно явное преобразование
string2 = '.'.join(notes)

print(string1) # DoReMiFaSolLaSi
print(string2) # Do.Re.Mi.Fa.Sol.La.Si

letters = 'abcdefghijkl'
tpl = tuple(letters)
print(tpl) # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')

number = 12345
# tpl = tuple(number) # TypeError: 'int' object is not iterable
# print(tpl)

poets = [
    ('Есенин', 13),
    ('Тургенев', 14),
    ('Маяковский', 28),
    ('Лермонтов', 20),
    ('Фет', 15),
]

for i in range(len(poets)):
    for j in range(i + 1, len(poets)):
        if poets[i][1] > poets[j][1]:
            poets[i], poets[j] = poets[j], poets[i]
print(poets) # [('Есенин', 13), ('Тургенев', 14), ('Фет', 15), ('Лермонтов', 20), ('Маяковский', 28)]
print(poets[0]) # ('Есенин', 13)
print(poets[-1]) # ('Маяковский', 28)

poets = [
    ('Тургенев', 14),
    ('Есенин', 13),
    ('Маяковский', 28),
    ('Фет', 15),
    ('Лермонтов', 20),
]

for i in range(len(poets)):
    for j in range(i + 1, len(poets)):
        if poets[i] > poets[j]:
            poets[i], poets[j] = poets[j], poets[i]
print(poets) # [('Есенин', 13), ('Лермонтов', 20), ('Маяковский', 28), ('Тургенев', 14), ('Фет', 15)]
print(poets[0]) # ('Есенин', 13)
print(poets[-1]) # ('Фет', 15)

# raw_input = input("Введите строку и число через пробел: ")
# string_part, number_part = raw_input.split()
# result_tuple = (string_part, int(number_part))
# print(result_tuple)

tuple1 = 1, 2, 3
tuple2 = 'a', 'b'

print(type(tuple1)) # Автоупаковка в кортеж
print(type(tuple2))

colors = ('red', 'green', 'blue', 'cyan')

a, b, c, d = colors # Количество элементов в кортеже должно совпадать с количеством переменных
# a, b = colors # ValueError: too many values to unpack (expected 2, got 4)
print(a) # red Распаковка кортежа
print(b) # green
print(c) # blue
print(d) # cyan

colors = ('red', 'green', 'blue')
a, b, _ = colors # Для простоты используют нижнее подчеркивание, если нужно пометить им не нужный элемент

print(a) # red
print(b) # green

a, b, c = 3, 2, 1
b, a, c = c, a, b

print(b, c, a) # 1 2 3

a, b, *tail = 1, 2, 3, 4, 5, 6 # Так же можно пометить список оставшихся элементов для упаковки в конце
print(a) # 1
print(b) # 2
print(tail) # [3, 4, 5, 6] - УПАКОВКА В ЛИСТ!

*names, surname = ('Стефани', 'Джоанн', 'Анджелина', 'Джерманотта') # В начале

print(names) # ['Стефани', 'Джоанн', 'Анджелина']
print(surname) # Джерманотта

singer = ('Freddie', 'Bohemian Rhapsody', 'Killer Queen', 'Love of my life', 'Mercury')

name, *songs, surname = singer # В середине

print(name) # Freddie
print(songs) # ['Bohemian Rhapsody', 'Killer Queen', 'Love of my life']
print(surname) # Mercury

a = 1,      # не распаковка, а просто присвоение
b, = 1,     # распаковка

print(a) # (1,)
print(b) # 1

info = ['timur', 'beegeek.org']
user, domain = info    # распаковка списка

print(user) # timur
print(domain) # beegeek.org

a, b, c, d = 'math'    # распаковка строки

print(a) # m
print(b) # a
print(c) # t
print(d) # h
"""
Помимо метода split() строковый тип данных содержит метод partition(). 
Метод partition() принимает на вход один аргумент sep, разделяет строку 
при первом появлении sep и возвращает кортеж, состоящий из трех элементов: 
часть перед разделителем, сам разделитель и часть после разделителя. 
Если разделитель не найден, то кортеж содержит саму строку, за которой следуют 
две пустые строки.
"""
s1 = 'abc-de'.partition('-')
s2 = 'abc-de'.partition('.')
s3 = 'abc-de-fgh'.partition('-')

print(s1) # ('abc', '-', 'de')
print(s2) # ('abc-de', '', '')
print(s3) # ('abc', '-', 'de-fgh')
"""
https://habr.com/ru/post/319164/
"""