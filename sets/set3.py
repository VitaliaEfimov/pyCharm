"""✅ Метод add() используется для добавления нового элемента в множество.

✅ Метод remove() удаляет элемент из множества с генерацией исключения (ошибки) в случае, если такого элемента нет.

✅ Метод discard() удаляет элемент из множества без генерации исключения (ошибки), если элемент отсутствует.

✅ Метод pop() удаляет и возвращает случайный элемент из множества с генерацией исключения (ошибки) при попытке удаления из пустого множества.

✅ Метод clear() удаляет все элементы из множества."""
numbers = {1, 1, 2, 3, 5, 8, 3}  # создаем множество

numbers.add(21)  # добавляем число 21 в множество
numbers.add(34)  # добавляем число 34 в множество

print(numbers) # {1, 2, 3, 34, 5, 21, 8}

numbers = set()  # создаем пустое множество

numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(1)

print(numbers) # {1, 2, 3}

numbers = set()  # создаем пустое множество

for i in range(10):
    numbers.add(i * i + 1)

print(numbers) # {1, 2, 65, 5, 37, 10, 17, 50, 82, 26}
numbers = {1, 2, 3, 4, 5}

numbers.remove(3) # параметр - элемент, не индекс!
# numbers.remove(10) # KeyError: 10 элемента нет в множестве
print(numbers) # {1, 2, 4, 5}

numbers = {1, 2, 3, 4, 5}

numbers.discard(3)
numbers.discard(10) # Ошибки нет, хоть элемента нет в множестве
print(numbers)

numbers = {1, 2, 3, 4, 5}

print('до удаления:', numbers) # до удаления: {1, 2, 3, 4, 5}
num = numbers.pop()                 # удаляет случайный элемент множества, возвращая его
print('удалённый элемент:', num) # удалённый элемент: 1
print('после удаления:', numbers) # после удаления: {2, 3, 4, 5}

numbers = {1, 2, 3, 4, 5}
numbers.clear()

print(numbers) # set()
myset = {'python'}
item = myset.pop()

print(item, len(myset)) # python 0

myset = set('python')
item = myset.pop()

print(item, len(myset)) # p 5

myset = set()
# item = myset.pop() # KeyError: 'pop from an empty set'
# print(item)

for i in range(10):
    if i % 2 == 0:
        myset.add('even')
    else:
        myset.add('odd')

print(len(myset))