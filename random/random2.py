"""
✅ Метод shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.

✅ Метод choice() принимает список (строку, кортеж) в качестве обязательного аргумента и возвращает один случайный элемент.

✅ Метод sample() принимает два обязательных аргумента: первый – коллекция (последовательность), которая поддерживает индексацию (список, строка, кортеж), второй – количество случайных элементов. Возвращает список из указанного количества уникальных (имеющих разные индексы) случайных элементов.

✅ Модуль string содержит полезные константные строки, которые представляют часто используемые наборы символов: буквы, цифры, знаки препинания и др.
"""
import string
from random import *

print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print(string.digits) # 0123456789
print(string.hexdigits) # 0123456789abcdefABCDEF
print(string.octdigits) # 01234567
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.printable) # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(numbers) # Перемешивание списка случайным образом, метод возвращает None
print(numbers) # [8, 2, 5, 1, 6, 7, 4, 3]

print(choice('BEEGEEK')) # Выводит рандомно один элемент
print(choice([1, 2, 3, 4]))
print(choice(('a', 'b', 'c', 'd')))
print()

print(sample(numbers, 1)) # Возвращает переданное количество случайных элементов списка
print(sample(numbers, 2))
print(sample(numbers, 3))
print(sample(numbers, 5)) # [8, 4, 2, 6, 1]
# print(sample(numbers, 9)) # ValueError: Sample larger than population or is negative
print()

def generate_ip_address():
    l = []
    for i in range(4):
        r = randint(0, 255)
        l.append(str(r))
    return '.'.join(l)

print(generate_ip_address())
print(generate_ip_address())
print(generate_ip_address())
print(generate_ip_address())
print()

def generate_index():
    return choice(string.ascii_uppercase) + choice(string.ascii_uppercase) + str(randint(0, 99)) + '_' + str(randint(0, 99)) + choice(string.ascii_uppercase) + choice(string.ascii_uppercase)

print(generate_index())
print()

def get_anagram(text):
    l = [c for c in text]
    shuffle(l)
    return ''.join(l)

print(get_anagram('топорик'))
print(get_anagram('корабль'))
print(get_anagram('барсучка'))
print(get_anagram('математика'))

def generate_bingo():
    s = set()
    r = []
    for i in range(5):
        l = []
        for j in range(5):
            if i == 2 and j == 2:
                l.append(0)
            else:
                n = randint(1, 75)
                while n in s:
                    n = randint(1, 75)
                s.add(n)
                l.append(n)
        r.append(l)
    return r

print(generate_bingo())
print(generate_bingo())
print(generate_bingo())
for row in generate_bingo():
    for number in row:
        print(str(number).ljust(3), end='')
    print()

print()

students = ('Владимир', 'Тагир', 'Давид', 'Арина', 'Глеб')

def get_secret_friend(students):
    s = set()
    l = [i for i in students]
    m = {}
    for i in students:
        k = choice(l)
        while k == i or k in s:
            k = choice(l)
        l.remove(k)
        s.add(k)
        m[i] = k
    return m

print(get_secret_friend(students)) # {'Владимир': 'Арина', 'Тагир': 'Глеб', 'Давид': 'Владимир', 'Арина': 'Тагир', 'Глеб': 'Давид'}

for name, friend in get_secret_friend(students).items():
    print(name, '-', friend)
"""
Владимир - Глеб
Тагир - Арина
Давид - Тагир
Арина - Владимир
Глеб - Давид
"""
print()

n = int(7)
m = int(8)
z = 'lI10oO'

def generate_password(length):
    s = ''
    while len(s) < length:
        k = ''
        if random()>0.5:
            k = choice(string.ascii_letters)
        else:
            k = choice(string.digits)
        if k in z:
            continue
        s += k
    return s

def generate_passwords(count, length):
    l = []
    for i in range(count):
        l.append(generate_password(length))
    return l

print(*generate_passwords(n, m), sep='\n')

"""
hg82338Z
NUsZW267
GSGgdEB7
5P53692R
R8k7UP3W
5Z78V8Ms
bxEx87LS
"""
print()

def generate_password(length):
    s = ''
    for i in range(length):
        k = ''
        while k in z:
            if i % 3 == 0:
                k = choice(string.ascii_uppercase)
            elif i % 3 == 1:
                k = choice(string.ascii_lowercase)
            else:
                k = choice(string.digits)
        s += k
    return s

def generate_passwords(count, length):
    l = []
    for i in range(count):
        l.append(generate_password(length))
    return l

print(*generate_passwords(n, m), sep='\n')

