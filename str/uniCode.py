num1 = ord('A') # Получение кода символа
num2 = ord('B')
num3 = ord('a')
print(num1, num2, num3) # 65 66 97
chr1 = chr(65) # Получение символа из кода
chr2 = chr(75)
chr3 = chr(110)
print(chr1, chr2, chr3) # A K n
print(ord('A'))
for i in range(26):
    print(chr(ord('A') + i), end='') # Вывод всех букв английского алфавита в верхнем регистре
print()
print(ord('a'))
for i in range(26):
    print(chr(ord('a') + i), end='') # Вывод всех букв английского алфавита в нижнем регистре
print()
print(ord('А'))
for i in range(32):
    print(chr(ord('А') + i), end='') # Вывод всех букв русского алфавита в нижнем регистре
print()
print(ord('а'))
for i in range(32):
    print(chr(ord('а') + i), end='') # Вывод всех букв русского алфавита в нижнем регистре
print()
print(ord('ё'), ord(' '), ord('Ё'), ord('6'))
# for i in range(4000): # Вывод всех символов с их кодом
#     print(f'{i} {chr(i)}')