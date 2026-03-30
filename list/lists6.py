names = ['Gvido', 'Roman', 'Timur']
print(names) # ['Gvido', 'Roman', 'Timur']
names.insert(5, 'Anton') # Если заходим за допустимы индекс - убираем в конец списка
names.insert(-5, 'Anton') # Если заходим за допустимы индекс отрицательный - убираем в начало списка
print(names) # ['Anton', 'Gvido', 'Roman', 'Timur', 'Anton']
names.remove('Anton')
names.insert(0, 'Anders') # Вставляем элемент по соответствующему индексу, все элементы справа сдвигаются
print(names) # ['Anders', 'Gvido', 'Roman', 'Timur', 'Anton']
print(names.insert(3, 'Josef')) # None
print(names) # ['Anders', 'Gvido', 'Roman', 'Josef', 'Timur', 'Anton']
print(names.index('Timur')) # 4 Выводит индекс элемента в массиве
# print(names.index('Tim')) # Если элемента нет - ошибка. Лучше использовать с  in. ValueError: 'Tim' is not in list
print(names.remove('Timur')) # None Удаляем первый найденный элемент с начала. Для удаления всех элементов лучше использовать while и in
print(names) # ['Anders', 'Gvido', 'Roman', 'Josef', 'Anton']
# names.remove('Гречка') # Если элемента нет - ошибка ValueError: list.remove(x): x not in list
names = ['Gvido', 'Roman', 'Timur']
print(names.pop(1)) # Roman. Удаляем элемент с индексом 1. Можно без параметра, тогда будет удален и возвращен последний элемент
print(names)
names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
print(names.count('Timur')) # Получение количества переданного элемента в списке.
print(names.count('Gvido'))
print(names.count('Josef'))
names = ['Gvido', 'Roman', 'Timur']
print(names.reverse())
print(names) # Меняем порядок элементов в списке - не создаем копию, а меняем текущий список
names = ['Gvido', 'Roman', 'Timur']
names_copy = names.copy() # Создаем поверхностную копию списка names. Аналогично использованию среза names[:]
print(names)
print(names_copy)
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
print(a.sort()) # None Сортируем список по возрастанию
print('Отсортированный список:', a) # Отсортированный список: [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
a.sort(reverse=True)  # Сортируем по убыванию
print('Отсортированный список:', a) # Отсортированный список: [1000, 99, 45, 34, 12, 9, 8, 7, 6, 1, 0, -2, -3, -67]
a = ['бета', 'альфа', 'дельта', 'гамма']
a.sort()
print('Отсортированный список:', a) # Отсортированный список: ['альфа', 'бета', 'гамма', 'дельта']
a = ['бета', 'альфа', 'дельта', 'гамма']
print(sorted(a)) # ['альфа', 'бета', 'гамма', 'дельта'] Альтернативный вариант сортировки - метод возвращает отсортированный список
print('Не отсортированный список:', a) # Не отсортированный список: ['бета', 'альфа', 'дельта', 'гамма'] - сам список метод не меняет
n = [1, 2, 3, 4]
n.clear() # Очищаем список от всех элементов
print(n) # []
