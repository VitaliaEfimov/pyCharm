numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']
print(len(numbers))      # Выводим длину списка numbers
print(len(languages))    # Выводим длину списка languages
print(len(['apple', 'banana', 'cherry']))   # Выводим длину списка, состоящего из 3 элементов
if 2 in numbers: # Проверяем есть ли в списке элемент
    print('Список numbers содержит число 2')
else:
    print('Список numbers не содержит число 2')
if 0 not in numbers: # Проверяем отсутствие элемента
    print('Список numbers не содержит нулей')
print(numbers[0], numbers[len(numbers)-1]) # Вывод первого и последнего элемента из списка
print(numbers[-1]) # Вывод последнего элемента
# print(numbers[17]) # IndexError: list index out of range Ошибка выхода индекса за допустимое значение
fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
fruits[2] = 'orange' # Меняем значение элемента
fruits[-1] = 'peach'
print(fruits)
print(numbers[1:3]) # Получение среза, второе число не включительно
print(numbers[2:5])
fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
fruits[2:5] = ['банан', 'вишня', 'киви'] # Изменение конкретных элементов списка посредством среза
print(fruits)
print([1, 2, 3, 4] + [5, 6, 7, 8]) # Конкатенация
print([7, 8] * 3) # Умножение на число
print([0] * 10)
a = [1, 2, 3, 4]
b = [7, 8]
a += b   # Добавляем к списку a список b
b *= 5   # Повторяем список b 5 раз
print(a)
print(b)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Сумма всех элементов списка =', sum(numbers))
numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
print('Минимальный элемент =', min(numbers))
print('Максимальный элемент =', max(numbers))
numbers = ['8', '9', '10', '11', '12']
print('Минимальный элемент =', min(numbers))
print('Максимальный элемент =', max(numbers))
names = ['Monica', 'Joey', 'Gunther', 'Chandler']
print('Минимальный элемент =', min(names))
print('Максимальный элемент =', max(names))
s = 'abcdefg' # Строка не изменяема
# s[1] = 'x'    # пытаемся изменить 2 символ (по индексу 1) строки TypeError: 'str' object does not support item assignment
books = ['1984', 'О дивный новый мир', '451 градус по Фаренгейту']
print(books[0][1]) # Двойной индекс - получаем символ
print(books[2][4:10])
artists = ['Malevich', 'Vasnetsov', 'Monet']
print(artists[0]) # Это элемент
print(artists[0:1]) # это новый список с одним элементом
browsers = ['Firefox', 'Chrome', 'Safari', 'Yandex'] # Сумма листов - это новый лист
print(browsers[2:4] + browsers[3:] + browsers[:1])
browsers = ['Firefox', 'Chrome', 'Safari', 'Yandex']
browsers[1:3] = ['Opera', 'Edge'] # Замена элементов
print(browsers)
browsers[1:4] = ['Opera', 'Edge'] # Замена элементов, срез заменяется другим срезом