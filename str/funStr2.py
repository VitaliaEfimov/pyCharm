s = 'foo goo moo'
print(s.count('oo')) # Ищем совпадения подстроки в строке. 3
print(s.count('oo', 0, 8))  # Подсчет с 0 по 7 символ. 2
s = '11111'
print(s.count('11')) # Считаются только не пересекающиеся последовательности. 2
s = 'foobar'
print(s.startswith('foo')) # Проверка начинается ли срока с подстроки. True
print(s.startswith('baz')) # False
s = 'foobar'
print(s.endswith('bar')) # Проверка кончается ли срока подстрокой. True
print(s.endswith('baz')) # False
s = 'это хорошй текст'
print(s.find('хорош')) # Выдает индекс начала подстроки в стоке. Если не найдено вернется -1. Результат: 4
s = 'foo bar foo baz foo qux'
print(s.find('foo')) # Выдает первое нахождение, поиск с начала 0
print(s.find('bar', 8, 16)) # -1
print(s.find('qu')) # 20
print(s.find('python')) # -1
s = "doc.pink.pdf"
print(s.rfind('.')) # Выдает индекс нахождения подстроки с конца строки. 8
print(s.rfind('.', 1, 7)) # Выдает индекс нахождения подстроки с конца подстроки. 3
s = "doc.pink.pdf"
print(s.index('.')) # Выдает индекс нахождения подстроки с начала строки. 3
print(s.index('.', 7, 11)) # Выдает индекс нахождения подстроки с начала подстроки. 8
# print(s.index(',')) # Если не нашли, то ошибка. ValueError: substring not found
s = "doc.pink.pdf"
print(s.rindex('.')) # Выдает индекс нахождения подстроки с конца строки. 8
print(s.rindex('.', 1, 7)) # Выдает индекс нахождения подстроки с конца подстроки. 3
# print(s.rindex(',')) # Если не нашли, то ошибка. ValueError: substring not found
s = '     foo bar foo baz foo qux      '
print(s.strip()) # Удаляем все пробелы. 'foo bar foo baz foo qux'
s = '     foo bar foo baz foo qux      '
print(s.lstrip()) # Убираем пробелы только в начале строки. 'foo bar foo baz foo qux      '
s = '      foo bar foo baz foo qux      '
print(s.rstrip()) # Убираем пробелы только в конце строки. '      foo bar foo baz foo qux'
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault')) # Заменяем подстроку другой подстрокой. 'grault bar grault baz grault qux'
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2)) # Можно задать количество замен с начала строки. 'grault bar grault baz foo qux'
s = '-+-+abc+-+-'
print(s.strip('+-')) # Можно задать символы для удаления. 'abc'
print(s.rstrip('+-')) # '-+-+abc'
print(s.lstrip('+-')) # 'abc+-+-'