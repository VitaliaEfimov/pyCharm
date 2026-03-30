s = 'Python is the most powerful language'
words = s.split() # Разбиваем строку на отдельные элементы и формируем список ориентируясь на пробелы
print(words) # ['Python', 'is', 'the', 'most', 'powerful', 'language']
numbers = '1 2 3 4'.split()
print(numbers) # ['1', '2', '3', '4']
ip = '192.168.1.24'
numbers = ip.split('.')    # явно указываем разделитель
print(numbers) # ['192', '168', '1', '24']
words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
s = ' '.join(words) # Собираем строку из списка слов
print(s) # 'Python is the most powerful language'
words = ['Мы', 'учим', 'язык', 'Python']
print('*'.join(words)) # Мы*учим*язык*Python
print('-'.join(words)) # Мы-учим-язык-Python
print('?'.join(words)) # Мы?учим?язык?Python
print('!'.join(words)) # Мы!учим!язык!Python
print('*****'.join(words)) # Мы*****учим*****язык*****Python
print('abc'.join(words)) # МыabcучимabcязыкabcPython
print('123'.join(words)) # Мы123учим123язык123Python
s = 'I love  Python' # Есть двойной пробел
words1 = s.split() # Игнорирует дублирование пробелов
words2 = s.split(' ') # Строгое разделение строк одним пробелом
print(words1) # ['I', 'love', 'Python']
print(words2) # ['I', 'love', '', 'Python']
# print([1, 2].split()) # Работаем только со строками AttributeError: 'list' object has no attribute 'split'
# numbers = [1, 2, 3, 4]  # список чисел
# s = '*'.join(numbers) # TypeError: sequence item 0: expected str instance, int found
# print(s)
s = '+'.join('pygen') # Работает и со строкой
print(s) # p+y+g+e+n
s = 'the earth'.split()
se = '**'
print(' '.join([se.join(word) for word in s]))