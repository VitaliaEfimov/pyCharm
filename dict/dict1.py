"""
 Словарь – изменяемая коллекция пар ключ–значение, в которой каждый ключ уникален.

✅ Создание словаря:

с помощью фигурных скобок:
empty_dict = {}
info_dict = {'name': 'Timur', 'age': 28}


с помощью функции dict():

empty_dict = dict()
info_dict1 = dict(name='Timur', age=28)
info_dict2 = dict([('name', 'Timur'), ('age', 28)])
info_dict3 = dict((['name', 'Timur'], ['age', 28]))


✅ Метод dict.fromkeys() создает словарь с заданными ключами и одинаковыми значениями:

info_dict = dict.fromkeys(['name', 'age'], 'Missed information')


Если методу fromkeys() не передать второй параметр, то по умолчанию присваивается значение None.

✅ Извлечь значение элемента словаря можно, обратившись к нему по его ключу. Чтобы получить значение по заданному ключу, как и в списках, используем квадратные скобки [] , индексируем по ключу.

✅ Ключом словаря могут быть данные любого неизменяемого типа:

число;
строка;
булево значение;
кортеж;
замороженное множество (frozenset);
✅ Ключ словаря не может относиться к изменяемому типу данных:

список;
множество;
словарь;
✅ Значения словаря могут относиться к любому типу данных.

Начиная с версии Python 3.6, словари являются упорядоченными, то есть сохраняют порядок следования ключей в порядке их внесения в словарь.
"""
languages = {'Python': 'Гвидо ван Россум',
             'C#': 'Андерс Хейлсберг',
             'Java': 'Джеймс Гослинг',
             'C++': 'Бьёрн Страуструп'}
# print('Создателем языка C# является', languages[1]) # KeyError: 1
print('Создателем языка C# является', languages['C#'])
print('Создателем языка C# является', languages['C' + '#']) # Можно указать выражение

info = dict(name='Timur', age=28, job='Teacher') # Создание словаря, ключи - строки
print(info) # {'name': 'Timur', 'age': 28, 'job': 'Teacher'}
print(info['name']) # Timur
print(info['age']) # 28
print(info['job']) # Teacher

info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
info_dict = dict(info_list)  # создаем словарь на основе списка кортежей
print(info_dict) # {'name': 'Timur', 'age': 28, 'job': 'Teacher'}

info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])  # кортеж списков
info_dict = dict(info_tuple)  # создаем словарь на основе кортежа списков
print(info_dict) # {'name': 'Timur', 'age': 28, 'job': 'Teacher'}

dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information') # У разных ключей одно значение
print(dict1) # {'name': 'Missed information', 'age': 'Missed information', 'job': 'Missed information'}

dict2 = dict.fromkeys(['name', 'age', 'job']) # Можно не указывать значение, оно по дефолту будет None
print(dict2) # {'name': None, 'age': None, 'job': None}

dict1 = {}
dict2 = dict()

print(dict1) # {}
print(dict2) # {}
print(type(dict1)) # <class 'dict'>
print(type(dict2)) # <class 'dict'>

languages = {'Python': 'Гвидо ван Россум',
             'C#': 'Андерс Хейлсберг',
             'Java': 'Джеймс Гослинг'}

info = dict(name = 'Timur', age = 28, job = 'Teacher')

print(languages) # {'Python': 'Гвидо ван Россум', 'C#': 'Андерс Хейлсберг', 'Java': 'Джеймс Гослинг'}
print(info) # {'name': 'Timur', 'age': 28, 'job': 'Teacher'}

keys = ['name', 'age', 'job']
values = ['Timur', 28, 'Teacher']

info = dict(zip(keys, values))

print(info) # {'name': 'Timur', 'age': 28, 'job': 'Teacher'}

info = {'name': 'Ruslan', 'age': 28, 'name': 'Timur'}

print(info['name']) # Timur При указании 2 одинаковых ключей сохраняется последнее указанное значение

my_dict = {198: 'beegeek', 'name': 'Bob', True: 'a', (2, 2): 25} # Ключи могут быть только неизменяемые типы данных

# my_dict = {[2, 2]: 25, {1, 2}: 'python', 'name': 'Bob'} # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

my_dict1 = {'a': [1, 2, 3], 'b': {1, 2, 3}}           # значения – изменяемый тип данных

my_dict2 = {'a': [1, 2], 'b': [1, 2], 'c': [1, 2]}    # значения повторяются