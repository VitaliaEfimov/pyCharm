print('a'.ljust(3)) # Добавление пробелов в конец строки, параметр - количество символов в получаемой строке
print('ab'.ljust(3))
print('abc'.ljust(3))
print('abcdefg'.ljust(3)) # Если символов больше пробелы не добавляются
print('a'.ljust(5, '*')) # Второй параметр - символ, вместо пробела
print('ab'.ljust(5, '$'))
print('abc'.ljust(5, '#'))
print('a'.rjust(3)) # Добавление пробелов в начало строки
print('ab'.rjust(3))
print('abc'.rjust(3))
print('abcdefg'.rjust(3)) # Если символов больше пробелы не добавляются
print('a'.rjust(5, '*')) # Второй параметр - символ, вместо пробела
print('ab'.rjust(5, '$'))
print('abc'.rjust(5, '#'))

rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print() # Вывод матрицы с выделенным местом для чисел - 6 символов

n = 8
matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8

for i in range(n):                    # заполняем главную диагональ единицами, а побочную двойками
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2

for r in range(n):                    # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print() # Вывод матрицы с диагоналями 1 - главная 2 - побочная