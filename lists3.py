numbers = [1, 1, 2, 3, 5, 8, 13]  # Создаем список
numbers.append(21)  # Добавляем число 21 в конец списка
numbers.append(34)  # Добавляем число 34 в конец списка
print(numbers) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

numbers = []  # Создаем пустой список
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers) # [1, 2, 3]

# numbers = []  # создаем пустой список
# numbers[0] = 1 # IndexError: list assignment index out of range Нельзя в пустой список вставить элемент через индекс
# numbers[1] = 2
# numbers[2] = 3
# print(numbers)

odds = [1, 3, 5, 7]
numbers.extend(odds) # расширяем список
print(numbers) # [1, 2, 3, 1, 3, 5, 7]

words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']
words1.append('python') # Добавляет строку целиком
words2.extend('python') # Разбивает на элементы и добавляет каждый по отдельности
print(words1) # ['iq option', 'stepik', 'beegeek', 'python']
print(words2) # ['iq option', 'stepik', 'beegeek', 'p', 'y', 't', 'h', 'o', 'n']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[5]    # Удаляем элемент, имеющий индекс 5
print(numbers) # [1, 2, 3, 4, 5, 7, 8, 9] Список перестраивается

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[2:7]    # Удаляем элементы с 2 по 6 включительно
print(numbers) # [1, 2, 8, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2] # Удаляем четные элементы
print(numbers)

animals = ['cat', 'dog', 'snake']
new_animals = animals.append('bird')
print(animals) # ['cat', 'dog', 'snake', 'bird']
print(new_animals) # None

numbers = [4, 7, -2, 1, 6]
for num in numbers:
    num = num * 2 # Нельзя изменить элемент без прямого обращения к индексу
print(numbers) # [4, 7, -2, 1, 6]

numbers = [4, 7, -2, 1, 6]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2 # При прямом обращении присваивание срабатывает
print(numbers) # [8, 14, -4, 2, 12]