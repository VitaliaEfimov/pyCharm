"""
✅Изменение и добавление элемента словаря выполняется через индексацию:

dct[key] = value


✅ Словарный метод get() возвращает значение по ключу или значение по умолчанию, если ключ не найден:

dct.get(key, default)


Когда второй аргумент не указан, то метод в случае отсутствия ключа возвращает None.

✅ Метод update() объединяет ключи и значения одного словаря с ключами и значениями другого. При совпадении ключей в итоге сохранится значение словаря, указанного в качестве аргумента метода update():

dct1.update(dct2)


✅ Метод setdefault() позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря, если он отсутствует:

dct.setdefault(key, default)


Если значение default не передано в метод, то вставится значение None.

✅ Оператор del удаляет из словаря элемент по заданному ключу вместе с его значением:

del dct[key]


Если удаляемого ключа в словаре нет, возникнет ошибка KeyError.

✅ Метод pop() удаляет элемент по ключу и возвращает его значение:

dct.pop(key)


Если удаляемого ключа в словаре нет, возникнет ошибка KeyError. ​Чтобы ошибка не появлялась, этому методу можно передать второй аргумент. Он будет возвращен, если указанного ключа в словаре нет.

✅ Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение):

dct.popitem()


✅ Метод clear() удаляет все элементы из словаря:

dct.clear()


✅ Метод copy() создает поверхностную копию словаря:

dct_copy = dct.copy()
"""

info = {
    'name': 'Sam',
    'age': 28,
    'job': 'Teacher',
}

info['name'] = 'Timur'                  # изменяем значение по ключу name
info['email'] = 'timyr-guev@yandex.ru'  # добавляем в словарь элемент с ключом email

print(info) # {'name': 'Timur', 'age': 28, 'job': 'Teacher', 'email': 'timyr-guev@yandex.ru'}

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

# print(info['salary']) # KeyError: 'salary'
print(info.get('salary')) # None
item2 = info.get('salary', 'Информации о зарплате нет')
print(item2) # Информации о зарплате нет

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1
print(result) # {9: 1, 8: 1, 32: 2, 1: 5, 10: 4, 23: 3, 4: 2, 2: 6}

info1 = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev',
}

info2 = {
    'age': 30,
    'city': 'New York',
    'email': 'bob@web.com',
}

info1.update(info2)

print(info1) # {'name': 'Bob', 'age': 30, 'job': 'Dev', 'city': 'New York', 'email': 'bob@web.com'} общий ключ age берет значение из аргумента метода
info1 |= info2

print(info1) # {'name': 'Bob', 'age': 30, 'job': 'Dev', 'city': 'New York', 'email': 'bob@web.com'}

info = {
    'name': 'Bob',
    'age': 25,
}

name1 = info.setdefault('name')           # параметр default не задан
name2 = info.setdefault('name', 'Max')    # параметр default задан

print(name1) # Bob
print(name2) # Bob

job = info.setdefault('job', 'Dev')

print(info) # {'name': 'Bob', 'age': 25, 'job': 'Dev'}
print(job) # Dev

salary = info.setdefault('salary')
print(info) # {'name': 'Bob', 'age': 25, 'job': 'Dev', 'salary': None}
print(salary) # None

info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

del info['email']    # удаляем элемент имеющий ключ email
del info['job']      # удаляем элемент имеющий ключ job

print(info) # {'name': 'Sam', 'age': 28}

info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

email = info.pop('email')          # удаляем элемент по ключу email, возвращая его значение
job = info.pop('job')              # удаляем элемент по ключу job, возвращая его значение
# surname = info.pop('surname') # KeyError: 'surname'
surname = info.pop('surname', None)

print(email) # timyr-guev@yandex.ru
print(job) # Teacher
print(surname) # None
print(info) # {'name': 'Sam', 'age': 28}

info = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev',
}

info['surname'] = 'Sinclar'
item = info.popitem() # Удаляем последний добавленный элемент и возвращаем кортеж

print(item) # ('surname', 'Sinclar')
print(info) # {'name': 'Bob', 'age': 25, 'job': 'Dev'}

info = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev',
}

info.clear() # Очищаем весь словарь

print(info) # {}

info = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev',
}

info_copy = info.copy()

print(info_copy) # {'name': 'Bob', 'age': 25, 'job': 'Dev'}

info = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev',
}

new_info = info
new_info['name'] = 'Tim'

print(info) # {'name': 'Tim', 'age': 25, 'job': 'Dev'} ! Внесены изменения в основной словарь! Оператор присваивания (=) не копирует словарь, а лишь присваивает ссылку на старый словарь новой переменной.

info = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev'
}

new_info = info.copy()
new_info['name'] = 'Tim'

print(info) # {'name': 'Bob', 'age': 25, 'job': 'Dev'}
print(new_info) # {'name': 'Tim', 'age': 25, 'job': 'Dev'}

dict1 = {'pen': 2, 'pencil': 1, 'notebook': 1, 'eraser': 1}
dict2 = {'ruler': 1, 'pen': 5, 'compass': 1, 'notebook': 5}

keys = set(dict1.keys()) | set(dict2.keys())
result = {}
for key in keys:
    result[key] = dict1.get(key, 0) + dict2.get(key, 0)

print(result) # {'notebook': 6, 'eraser': 1, 'ruler': 1, 'pencil': 1, 'pen': 7, 'compass': 1}

text = "TheyDon'tKnowThatWeKnowTheyKnowWeKnow"
result = {}
for c in text:
    result[c] = result.setdefault(c, 0) + 1

print(result) # {'T': 3, 'h': 3, 'e': 4, 'y': 2, 'D': 1, 'o': 5, 'n': 5, "'": 1, 't': 2, 'K': 4, 'w': 4, 'a': 1, 'W': 2}

pets = [
    ('Барсик', 'Маша', 'Петрова', 17),
    ('Джек', 'Галина', 'Лагунова', 45),
    ('Муся', 'Александр', 'Каракулов', 28),
    ('Буся', 'Маша', 'Петрова', 17),
    ('Кира', 'Вова', 'Пухарев', 54),
]
d = {}
for p in pets:
    t = (p[1], p[2], p[3])
    d.setdefault(t, []).append(p[0])
print(d) # {('Маша', 'Петрова', 17): ['Барсик', 'Буся'], ('Галина', 'Лагунова', 45): ['Джек'], ('Александр', 'Каракулов', 28): ['Муся'], ('Вова', 'Пухарев', 54): ['Кира']}