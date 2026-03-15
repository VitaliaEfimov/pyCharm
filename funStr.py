s = 'foO BaR BAZ quX'
print(s.capitalize()) # Делаем первый символ с верхним регистром, остальные с маленьким. Результат: Foo bar baz qux
s = 'foo123#BAR#.'
print(s.capitalize()) # Все символы не относящиеся к буквам остаются без изменений. Результат: Foo123#bar#.
s = 'FOO Bar 123 baz qUX'
print(s.swapcase()) # Меняем регистр у букв на обратный. Результат: foo bAR 123 BAZ Qux
s = 'the sun also rises'
print(s.title()) # Первая буква каждого слова с большой буквы. Результат: The Sun Also Rises
s = "what's happened to ted's IBM stock?"
print(s.title()) # Не анализирует важность слов, не обрабатывает аббревиатуры и апострофы. Результат: What'S Happened To Ted'S Ibm Stock?
s = 'FOO Bar 123 baz qUX'
print(s.lower()) # Возвращает все символы в нижний регистр. Результат: foo bar 123 baz qux
s = 'FOO Bar 123 baz qUX'
print(s.upper()) # Возвращает все символы в верхний регистр. Результат: FOO BAR 123 BAZ QUX
s = 'ЭТО ХОРОШЙ ТЕКСТ'
print(s.lower().find('хорош')) # Выдает индекс начала подстроки в стоке. Если не найдено вернется -1. Результат: 4
s = '2132jdsGdk'
print(len(list(sub for sub in s if sub == sub.lower() and sub.isalpha()))) # Проверка сколько символов являются буквами в нижнем регистре. Результат: 5